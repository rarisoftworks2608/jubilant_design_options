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
