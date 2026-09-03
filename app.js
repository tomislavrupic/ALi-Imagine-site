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
