// ── Navbar scroll effect ──
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 20);
});

// ── Mobile menu toggle ──
const navToggle = document.getElementById('navToggle');
const navLinks  = document.getElementById('navLinks');

if (navToggle) {
  navToggle.addEventListener('click', () => {
    navLinks.classList.toggle('open');
    const spans = navToggle.querySelectorAll('span');
    navLinks.classList.contains('open')
      ? (spans[0].style.transform = 'rotate(45deg) translate(5px,5px)',
         spans[1].style.opacity   = '0',
         spans[2].style.transform = 'rotate(-45deg) translate(5px,-5px)')
      : (spans[0].style.transform = '',
         spans[1].style.opacity   = '',
         spans[2].style.transform = '');
  });

  // Close on outside click
  document.addEventListener('click', e => {
    if (!navbar.contains(e.target)) {
      navLinks.classList.remove('open');
    }
  });
}

// ── Scroll-reveal for project cards ──
const observer = new IntersectionObserver(
  entries => entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.style.opacity   = '1';
      e.target.style.transform = 'translateY(0)';
    }
  }),
  { threshold: 0.12 }
);

document.querySelectorAll('.project-card, .feature-card, .step').forEach(el => {
  el.style.opacity   = '0';
  el.style.transform = 'translateY(24px)';
  el.style.transition = 'opacity .45s ease, transform .45s ease';
  observer.observe(el);
});

// ── Auto-dismiss flash messages after 5s ──
document.querySelectorAll('.flash').forEach(flash => {
  setTimeout(() => {
    flash.style.transition = 'opacity .4s ease';
    flash.style.opacity    = '0';
    setTimeout(() => flash.remove(), 400);
  }, 5000);
});
