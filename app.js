document.documentElement.classList.add("js");

const header = document.querySelector("[data-header]");
const revealItems = document.querySelectorAll(".reveal");
const video = document.querySelector("[data-warp-video]");
const videoToggle = document.querySelector("[data-video-toggle]");

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

videoToggle?.addEventListener("click", async () => {
  if (!video) return;
  if (video.paused) {
    await video.play();
    videoToggle.textContent = "PAUSE EVOLVE";
    videoToggle.setAttribute("aria-label", "Pause DREAM WARP preview");
  } else {
    video.pause();
    videoToggle.textContent = "PLAY EVOLVE";
    videoToggle.setAttribute("aria-label", "Play DREAM WARP preview");
  }
});
