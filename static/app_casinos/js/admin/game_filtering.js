{
  function getDataOnRequestFromFilter(dataFilter, parentBlock) {
    const url = "/api/v1/game-filter/";
    const data = { data_filter: dataFilter };
    console.log("Введенные данные:", data);
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrf_token,
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Ошибка сети");
        }
        return response.json();
      })
      .then((data) => {
        console.log("Успешный ответ от сервера:", data);
        window.updateGameData({ results: data }, parentBlock);
      })
      .catch((error) => {
        console.error("Произошла ошибка:", error);
      });
  }

  const setEventButtonFilter = (elementButton) => {
    // Добавляем новый обработчик события ввода
    elementButton.addEventListener("click", (event) => {
      const target = event.target;
      // Ищем ближайшего родителя с определенным классом
      const parentBlock = target.closest(".selector");
      const parentInputFilter = target.closest(".selector-available");

      const elementinput = parentInputFilter.querySelector(
        'input[id$="_input"]'
      );

      // if (event.key === 'Enter' && this.value.trim() !== '') {
      if (elementinput.value.trim() !== "") {
        let inputValue = elementinput.value.split(",").map((t) => t.trim());
        elementinput.value = "";

        // Блокируем кнопку:
        elementButton.setAttribute("disabled", "disabled");
        setTimeout(() => {
          elementButton.removeAttribute("disabled");
        }, 3000);

        getDataOnRequestFromFilter(inputValue, parentBlock);
      }
    });
  };

  function getDataFromGamesFilter() {
    // Получаем ссылку на элемент
    const elementsButtons = document.querySelectorAll(".send-filter-data");
    elementsButtons.forEach( (elm) => setEventButtonFilter(elm));

  }

  function main() {
    const checkExist = setInterval(function () {
      let elements = document.querySelectorAll(".send-filter-data");
      if (elements.length) {
        clearInterval(checkExist); // Остановить проверку, если элемент найден.
        getDataFromGamesFilter();
        return;
      }
      console.log("Элемент <id: slots_wagering-group> не найден!");
    }, 600);
  }

  document.addEventListener("DOMContentLoaded", function () {
    main();
    window.setEventButtonFilter = setEventButtonFilter;
  });
}
