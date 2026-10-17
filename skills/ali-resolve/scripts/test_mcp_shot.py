import unittest,tempfile,json
from pathlib import Path
from unittest.mock import patch
import mcp_shot
class ReceiptTests(unittest.TestCase):
    def test_uncertain_submit_cannot_duplicate(self):
        with tempfile.TemporaryDirectory() as d:
            folder=Path(d);receipt=folder/'shot.json'
            receipt.write_text(json.dumps({'state':'prepared','anchor_hashes':{},'payload':{'project_id':'project'}}))
            request={'projectId':'project','providerId':'hailuo_h3_mlx','modelId':'H3','prompt':'test','variationCount':1}
            with patch.object(mcp_shot,'call',side_effect=TimeoutError('uncertain')):
                with self.assertRaises(TimeoutError):mcp_shot.submit(folder,request)
            self.assertEqual(json.loads(receipt.read_text())['state'],'mcp_submission_pending')
            with patch.object(mcp_shot,'call') as call:
                with self.assertRaises(RuntimeError):mcp_shot.submit(folder,request)
                call.assert_not_called()
    def test_project_mismatch_rejected_before_mutation(self):
        with tempfile.TemporaryDirectory() as d:
            folder=Path(d);(folder/'shot.json').write_text(json.dumps({'state':'prepared','anchor_hashes':{},'payload':{'project_id':'original'}}))
            with patch.object(mcp_shot,'call') as call:
                with self.assertRaises(RuntimeError):mcp_shot.submit(folder,{'projectId':'other'})
                call.assert_not_called()
