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
