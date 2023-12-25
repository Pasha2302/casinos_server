(function ($) {
  $(document).ready(function () {
    const SelectBox = window.SelectBox
    SelectBox.filter = function (id, text) {
      const tokens = text.toLowerCase().split(',').map((t) => t.trim());
      for (const node of SelectBox.cache[id]) {
        if (tokens.lenght === 0) {
          node.displayed = 1;
          continue;
        }
        node.displayed = 0;
        const node_text = node.text.toLowerCase();
        for (const token of tokens) {
          if (node_text.includes(token)) {
            node.displayed = 1;
            break;
          }
        }
      }
      SelectBox.redisplay(id);
    }
  });
})(jQuery);



document.addEventListener('DOMContentLoaded', function () {
  const buttons = document.querySelectorAll('.nav-button');
  const fieldsets = document.querySelectorAll('.form-fieldset');
  const showAllButton = document.querySelector('.show-all-button');

  buttons.forEach(function (button) {
    button.addEventListener('click', function () {
      let target = button.getAttribute('data-target');

      // Скрыть все блоки
      fieldsets.forEach(function (fieldset) {
        fieldset.style.display = 'none';
      });

      // Показать выбранный блок
      document.getElementById(target).style.display = 'block';
    });
  });

  showAllButton.addEventListener('click', function () {
    // Показать все блоки
    fieldsets.forEach(function (fieldset) {
      fieldset.style.display = 'block';
    });
  });
});
