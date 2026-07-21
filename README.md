# ALi Imagine Landing Page

This directory is a complete static site. It has no package install, build step,
or absolute asset paths.

## Add it to another website

Copy the entire `landing` directory into the target website. Open
`landing/index.html` directly, or serve the directory from any static host.

Keep `index.html`, `styles.css`, `app.js`, and `assets/` together.

## GitHub Pages

The repository workflow at `.github/workflows/pages.yml` publishes this exact
directory. In GitHub, open **Settings → Pages** and set **Source** to
**GitHub Actions** once. Pushes to `main` that change `landing/` then update the
site automatically.

Expected URL:

```text
https://tomislavrupic.github.io/ALi-Imagine-site/
```

## Release link

The main download buttons point to the latest GitHub Release. Publish the DMG
as a release asset to keep the landing page stable across future versions.
