{
  function addEventPageList(selElm) {
    // Обработчик выбора страницы из списка
    selElm.addEventListener("click", function (event) {
      var target = event.target;
      console.log("\nTarget:", target);
      // console.log("Node Name:", target.nodeName);
      if (target && target.nodeName == "SELECT") {
        var pageNumber = target.value;
        var apiUrl = "/api/v1/game/?page=" + pageNumber;

        fetch(apiUrl, {
          method: "GET",
          headers: { "X-CSRFToken": csrf_token },
        })
          .then((response) => response.json())
          .then((data) => {
            // Ищем ближайшего родителя с определенным классом
            const parentWithClass = target.closest(".selector");
            // Обновляем содержимое страницы с новыми данными
            updatePageContent(data, parentWithClass);
          })
          .catch((error) => console.error("Ошибка при запросе:", error));
      }
    });
  }

  // Функция для создания всплывающего списка
  function createPageList(data) {
    const selectsElements = document.querySelectorAll(".page-list");

    for (let selectElement of selectsElements) {
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
    return selectsElements;
  }

  // Функция для ожидания появления элемента с определенным id.
  function waitForElementToLoad(data, elementId, createPageList) {
    var checkExist = setInterval(function () {
      var element = document.querySelector(elementId);
      if (element) {
        clearInterval(checkExist); // Остановить проверку, если элемент найден
        const selectsElements = createPageList(data); // Вызвать функцию обратного вызова
        selectsElements.forEach((selElm) => addEventPageList(selElm));

        // Обновляем содержимое страницы с данными первой страницы
        // updatePageContent(data);
      }
    }, 500); // Проверять наличие элемента каждые 100 миллисекунд
  }

  // Функция для отправки GET-запроса на первую страницу и обработки данных
  function fetchDataAndPopulatePageList() {
    const apiUrl = "/api/v1/game/?page=1";
    fetch(apiUrl, {
      method: "GET", // Используем метод POST для отправки данных
      headers: { "X-CSRFToken": csrf_token },
    })
      .then((response) => response.json())
      .then((data) => {
        // Обновляем всплывающий список с номерами страниц
        waitForElementToLoad(data, ".page-list", createPageList);
      })
      .catch((error) => console.error("Ошибка при запросе:", error));
  }

  // Функция для обновления содержимого блока выбора игр:
  function updatePageContent(data, parentBlock) {
    const SelectBox = window.SelectBox;

    const selectElement = parentBlock.querySelector('select[id$="_from"]');
    const currentSelectBlock = parentBlock.querySelector('select[id$="_to"]');

    // const currentSelectBlock = document.querySelector("#id_restriction_game-0-game_to");

    var checkIds = [...currentSelectBlock.childNodes].map((node) => {
      return node.value;
    });

    selectElement.innerHTML = "";
    // selectElementEmpty.innerHTML = "";
    // console.log(`Game Count: ${data.count}`)
    // console.log(`Game Len: ${data.results.length}`)
    // console.log('-'.repeat(40));

    // Добавляем данные из полученного списка в виде элементов <option>
    for (let item of data.results) {
      let optionElement = document.createElement("option");
      let optionElementEmpty = document.createElement("option");

      if (checkIds.includes(String(item.id))) continue;

      optionElement.value = item.id; // Устанавливаем значение
      optionElement.textContent = item.name; // Устанавливаем текст
      optionElement.title = item.name; // Устанавливаем title

      optionElementEmpty.value = item.id;
      optionElementEmpty.textContent = item.name;

      selectElement.appendChild(optionElement); // Добавляем элемент <option> в <select>
      //   selectElementEmpty.appendChild(optionElementEmpty);
    }
    // Обновление списка игр, используя полученные данные
    // SelectBox.init("id_restriction_game-0-game_from");
    SelectBox.init(selectElement.id);
    SelectBox.init(currentSelectBlock.id);
  }


  const setEventAddAnotherSlots = () => {
    const slotBlock = document.querySelector("#slots_wagering-group");
    const elmAddSlots = slotBlock.querySelector('tr[class="add-row"] a');
    console.log("\nElmAdd Slots:", elmAddSlots);

    elmAddSlots.addEventListener("click", (ev) => {
      // Ищем ближайшего родителя с определенным классом
      const selectorAvailableBlocks = ev.target
        .closest("#slots_wagering-group")
        .querySelectorAll(
          ".form-row.dynamic-slots_wagering .field-slot .selector-available h2"
        );

      console.log("\nParent Block H2:", selectorAvailableBlocks);
      for (let block of selectorAvailableBlocks) {
        if (!block.querySelector(".send-filter-data")) {
          createElementsPagination(block, selectorAvailableBlocks.length);
          fetchDataAndPopulatePageList();
          window.setEventButtonFilter(block.querySelector(".send-filter-data"));
        }
      }
    });
  };


  function main() {
    fetchDataAndPopulatePageList();
    setEventAddAnotherSlots();
  }

  document.addEventListener("DOMContentLoaded", function () {
    // console.log("CSRFToken:", csrf_token);
    // Вызываем функцию после загрузки страницы
    setTimeout(main, 2000);
    window.updateGameData = updatePageContent;
  });
}
