{

    function addEventPageList() {
        // Обработчик выбора страницы из списка
        document.getElementById("page-list").addEventListener("click", function (event) {
            var target = event.target;
            // console.log("\nTarget:", target);
            // console.log("Node Name:", target.nodeName);
            if (target && target.nodeName == "SELECT") {
                var pageNumber = target.value;
                var apiUrl = "/api/v1/game/?page=" + pageNumber;

                fetch(apiUrl, {
                    method: 'GET', // Используем метод GET для получения данных
                    headers: { 'X-CSRFToken': csrf_token },
                }).then(response => response.json()
                ).then(data => {
                    // Обновляем содержимое страницы с новыми данными
                    updatePageContent(data);
                }).catch(error => console.error("Ошибка при запросе:", error));
            }
        });
    }


    // Функция для создания всплывающего списка
    function createPageList(data) {
        let selectElement = document.getElementById("page-list");
        selectElement.innerHTML = ""; // Очищаем список перед обновлением

        let totalPages = Math.ceil(data.count / 250); // Предположим, что на каждой странице 250 элементов

        // Генерируем элементы списка для каждой страницы
        for (var i = 1; i <= totalPages; i++) {
            var optionItem = document.createElement("option");
            optionItem.textContent = i;
            optionItem.setAttribute("value", i);
            selectElement.appendChild(optionItem);
        }
    }


    // Функция для ожидания появления элемента с определенным id
    function waitForElementToLoad(data, elementId, callback) {
        var checkExist = setInterval(function () {
            var element = document.getElementById(elementId);
            if (element) {
                clearInterval(checkExist); // Остановить проверку, если элемент найден
                callback(data); // Вызвать функцию обратного вызова
                addEventPageList();
                // Обновляем содержимое страницы с данными первой страницы
                // updatePageContent(data);
            }
        }, 500); // Проверять наличие элемента каждые 100 миллисекунд
    }


    // Функция для отправки GET-запроса на первую страницу и обработки данных
    function fetchDataAndPopulatePageList() {
        const apiUrl = "/api/v1/game/?page=1";
        fetch(apiUrl, {
            method: 'GET', // Используем метод POST для отправки данных
            headers: { 'X-CSRFToken': csrf_token },
        }).then(response => response.json()
        ).then(data => {
            // Обновляем всплывающий список с номерами страниц
            waitForElementToLoad(data, 'page-list', createPageList)
        }).catch(error => console.error("Ошибка при запросе:", error));
    }


    // Функция для обновления содержимого блока выбора игр:
    function updatePageContent(data) {
        const SelectBox = window.SelectBox;

        var selectElement = document.getElementById('id_restriction_game-0-game_from');
        var selectElementEmpty = document.getElementById('id_restriction_game-__prefix__-game');
        const currentSelectBlock = document.querySelector('#id_restriction_game-0-game_to');
        var checkIds = [...currentSelectBlock.childNodes].map((node) => { return node.value });

        selectElement.innerHTML = '';
        selectElementEmpty.innerHTML = '';
        // console.log(`Game Count: ${data.count}`)
        // console.log(`Game Len: ${data.results.length}`)
        // console.log('-'.repeat(40));

        // Добавляем данные из полученного списка в виде элементов <option>
        for (let item of data.results) {
            let optionElement = document.createElement('option');
            let optionElementEmpty = document.createElement('option');

            if (checkIds.includes(String(item.id))) continue;

            optionElement.value = item.id; // Устанавливаем значение
            optionElement.textContent = item.name; // Устанавливаем текст
            optionElement.title = item.name; // Устанавливаем title

            optionElementEmpty.value = item.id;
            optionElementEmpty.textContent = item.name;

            selectElement.appendChild(optionElement); // Добавляем элемент <option> в <select>
            selectElementEmpty.appendChild(optionElementEmpty);
        };
        // Обновление списка игр, используя полученные данные
        SelectBox.init('id_restriction_game-0-game_from');
    }


    function main() {
        fetchDataAndPopulatePageList();
    }


    document.addEventListener('DOMContentLoaded', function () {
        // console.log("CSRFToken:", csrf_token);
        // Вызываем функцию после загрузки страницы
        setTimeout(main, 2000);
        window.updateGameData = updatePageContent;
    });

}
