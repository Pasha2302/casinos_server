document.addEventListener("DOMContentLoaded", function () {
    // Загрузка DOM

    // Найдите блок по классу
    var blockedCountriesBlock = document.querySelector('.field-blocked_countries');

    // Создать форму
    var formHtml = `
      <form method="post" id="country_form">
          {% csrf_token %}
          <div class="submit-row">
              <label for="data-input">Enter Data (comma-separated):</label>
              <textarea id="data-input" name="data" rows="4" cols="50"></textarea>
              <input type="button" value="Submit Data" class="custom-button" onclick="submitData()">
          </div>
      </form>
    `;

    // Форму в блок
    blockedCountriesBlock.insertAdjacentHTML('beforeend', formHtml);
});

function submitData() {
    // Получаем данные из текстового поля
    var inputData = document.getElementById('data-input').value;

    // Разбиваем введенные данные по запятой и создаем массив
    var dataArray = inputData.split(',');

    // Формируем JSON объект
    var jsonData = { "countries": dataArray };

    // Создаем объект FormData и добавляем данные в него
    const formData = new FormData();
    formData.append('data', JSON.stringify(jsonData));

    // Получаем полный URL с учетом домена и протокола
    const url = window.location.href;

    // Используем AJAX для отправки данных без перезагрузки страницы
    fetch(url + 'import-countries/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
        },
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            // Опционально: обновите интерфейс, если это необходимо
        })
        .catch(error => {
            console.error('Error:', error);
        });

    // Очищаем поле ввода
    document.getElementById('data-input').value = '';
}


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
