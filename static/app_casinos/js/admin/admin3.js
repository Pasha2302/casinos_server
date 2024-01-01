(function ($) {
  $(document).ready(function () {
    const SelectBox = window.SelectBox
    SelectBox.filter = function (id, text) {
      console.log("Select Filter [id]:", id)
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
  const buttons = document.querySelectorAll('.nav-button, .show-all-button');
  const fieldsets = document.querySelectorAll('.form-fieldset');
  const showAllButton = document.querySelector('.show-all-button');
  const formsetBlocks = document.querySelectorAll('.js-inline-admin-formset.inline-group');

  function hideFormsetBlocks() {
    formsetBlocks.forEach(function (formsetBlock) {
      formsetBlock.style.display = 'none';
    });
  }

  function setActiveButton(button) {
    buttons.forEach(function (btn) {
      btn.classList.remove('active');
    });
    button.classList.add('active');
  }

  buttons.forEach(function (button) {
    button.addEventListener('click', function () {
      let target = button.getAttribute('data-target');

      // Скрыть все блоки форм
      fieldsets.forEach(function (fieldset) {
        fieldset.style.display = 'none';
      });

      // Скрыть все блоки formset
      hideFormsetBlocks();

      // Показать выбранный блок форм
      if (document.getElementById(target)) {
        document.getElementById(target).style.display = 'block';

        // Установить активную кнопку
        setActiveButton(button);
      }
    });
  });

  showAllButton.addEventListener('click', function () {
    // Показать все блоки форм
    fieldsets.forEach(function (fieldset) {
      fieldset.style.display = 'block';
    });

    // Показать все блоки formset
    formsetBlocks.forEach(function (formsetBlock) {
      formsetBlock.style.display = 'block';
    });

    // Установить активную кнопку
    setActiveButton(showAllButton);
  });
});
