{

    function getDataOnRequestFromFilter(dataFilter) {
        const url = "/api/v1/game-filter/"
        const data = {data_filter: dataFilter};
        console.log('Введенные данные:', data);
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf_token,
            },
            body: JSON.stringify(data)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка сети');
            }
            return response.json();
        })
        .then(data => {
            console.log('Успешный ответ от сервера:', data);
            window.updateGameData({results: data});
        })
        .catch(error => {
            console.error('Произошла ошибка:', error);
        });
    }


    function getDataFromGamesFilter() {
        // Получаем ссылку на элемент
        let elementButton = document.getElementById('send-filter-data');
        let elementinput = document.getElementById('id_restriction_game-0-game_input');

        // Добавляем новый обработчик события ввода
        elementButton.addEventListener('click', function (event) {
            // if (event.key === 'Enter' && this.value.trim() !== '') {
            if (elementinput.value.trim() !== '') {
                let inputValue = elementinput.value.split(',').map((t) => t.trim());
                elementinput.value = '';

                // Блокируем кнопку:
                elementButton.setAttribute('disabled', 'disabled');
                setTimeout(() => {
                    elementButton.removeAttribute('disabled');
                }, 3000);
                
                getDataOnRequestFromFilter(inputValue);
            }
        });
    }


    function main() {
        let checkExist = setInterval(function () {
            let element = document.getElementById('send-filter-data');
            if (element) {
                clearInterval(checkExist); // Остановить проверку, если элемент найден
                getDataFromGamesFilter();
                return;
            }
            console.log('Элемент <id: send-filter-data> не найден!');
        }, 600);
    }


    document.addEventListener('DOMContentLoaded', function () {
        main();
    });

}
