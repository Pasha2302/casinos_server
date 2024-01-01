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
  const buttons = document.querySelectorAll('.nav-button');

  function setActiveButton(button) {
    buttons.forEach(function (btn) { btn.classList.remove('active'); });
    button.classList.add('active');
  }

  buttons.forEach(function (button) {
    button.addEventListener('click', function () {
        // Установить активную кнопку
        setActiveButton(button);
    })
  });
});
