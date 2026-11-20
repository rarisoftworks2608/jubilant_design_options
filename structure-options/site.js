// Mobile menu + project filters for the structure-options mockups
document.querySelectorAll('.menu-btn').forEach(function (b) {
  b.addEventListener('click', function () {
    document.body.classList.toggle('menu-open');
    b.setAttribute('aria-expanded', document.body.classList.contains('menu-open'));
  });
});
document.querySelectorAll('.pills').forEach(function (bar) {
  var scope = bar.parentElement;
  bar.querySelectorAll('.pill').forEach(function (p) {
    p.addEventListener('click', function () {
      bar.querySelectorAll('.pill').forEach(function (x) { x.classList.remove('on'); });
      p.classList.add('on');
      var f = p.getAttribute('data-f');
      scope.querySelectorAll('[data-cat]').forEach(function (c) {
        c.style.display = (f === 'all' || c.getAttribute('data-cat') === f) ? '' : 'none';
      });
    });
  });
});

// Opening intro on the home page: logo in the middle, then the curtain lifts (once per visit)
(function () {
  var root = document.documentElement, loader = document.getElementById('loader');
  if (!loader) return;
  if (!root.classList.contains('intro')) { loader.remove(); return; }
  var done = false;
  function finish() {
    if (done) return; done = true;
    loader.classList.add('done');
    setTimeout(function () { root.classList.remove('intro'); }, 450);
    setTimeout(function () { loader.remove(); }, 1400);
  }
  function go() { setTimeout(finish, 2000); }
  if (document.readyState === 'complete') go(); else addEventListener('load', go, { once: true });
  setTimeout(finish, 4500); // fail-safe: never leave the page hidden behind the intro
})();
