document.documentElement.classList.add("js");

const header = document.querySelector("[data-header]");
const revealItems = document.querySelectorAll(".reveal");

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 },
);

revealItems.forEach((item) => revealObserver.observe(item));

window.addEventListener(
  "scroll",
  () => header?.classList.toggle("scrolled", window.scrollY > 24),
  { passive: true },
);

for (const button of document.querySelectorAll("[data-copy-skill]")) {
  button.addEventListener("click", async () => {
    const prompt = document.getElementById(button.dataset.copySkill);
    if (!prompt) return;
    try {
      await navigator.clipboard.writeText(prompt.textContent.trim());
      button.textContent = "Copied";
    } catch {
      button.textContent = "Select and copy the text below";
    }
  });
}
