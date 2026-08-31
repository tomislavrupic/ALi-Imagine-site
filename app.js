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

document.querySelectorAll("[data-copy-address]").forEach((button) => {
  button.addEventListener("click", async () => {
    const address = button.getAttribute("data-copy-address");
    const status = document.querySelector("[data-copy-status]");
    if (!address) return;

    try {
      await navigator.clipboard.writeText(address);
      button.textContent = "COPIED";
      if (status) status.textContent = "ADDRESS COPIED";
      window.setTimeout(() => {
        button.textContent = "COPY CA";
        if (status) status.textContent = "";
      }, 2200);
    } catch {
      if (status) status.textContent = "SELECT + COPY THE ADDRESS ABOVE";
    }
  });
});
