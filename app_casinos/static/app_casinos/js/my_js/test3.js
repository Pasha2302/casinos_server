var isSendDataToServer = false;


function getDataServer(dataToSend) {
    try {
        fetch('/scroll/get_data/', {
            method: 'POST', // Используем метод POST для отправки данных
            body: JSON.stringify(dataToSend), // Преобразуем данные в формат JSON
            headers: { 'X-CSRFToken': csrf_token },

        }).then(response => {
            if (response.ok) { return response.json() }
            else { throw new Error('Ошибка при запросе на сервер: ' + response.statusText) }

        }).then(data => {
            console.log('Data Server:', data);

        }).catch(error => {
            console.error('Ошибка при запросе на сервер:', error.message);
        });

    } catch (error) { console.error('Ошибка при выполнении запроса:', error); }
}


function testFuncScroll() {
    console.log('\n\nTest Function');
    const blockScroll = document.querySelector('#test-22');

    blockScroll.addEventListener('scroll', function () {
        if (blockScroll.offsetHeight + blockScroll.scrollTop >= blockScroll.scrollHeight - 1 && !isSendDataToServer) {
            isSendDataToServer = true;

            console.log('\n\nЗагрузка данных с сервера! ...');
            console.log(
                `\n\t\tblockScroll.offsetHeight: ${blockScroll.offsetHeight}\n
                    blockScroll.scrollTop: ${blockScroll.scrollTop}\n
                    blockScroll.scrollHeight: ${blockScroll.scrollHeight}\n
                    blockScroll.offsetHeight + blockScroll.scrollTop: ${blockScroll.offsetHeight + blockScroll.scrollTop}`
            );
            getDataServer({ key1: 'value1', key2: 'value2' });

        }
    });
};



document.addEventListener('DOMContentLoaded', function () {
    console.log("CSRFToken:", csrf_token);
    testFuncScroll();

    // let elm = document.querySelector('#restriction_game-group');
    // elm.className = '';

});


let listName = ["Laurence", "Mike", "Larry", "Kim", "Joanne", "Laurence", "Mike", "Laurence", "Mike", "Laurence", "Mike"];
let listNumber = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
let listAss = ['a', 1, 'b', 'c', 4, 5, 'd', 7, 8, 9];

// listName.filter();
// listNumber.filter();
// listAss.filter();

const array = [
    "Laurence", "Mike", "Larry", "Kim", "Joanne",
    "Laurence", "Mike", "Laurence", "Mike", "Laurence", "Mike"
];

const uniqueArray = array.filter((value, index, _array) => {
    // Возвращаем true только для элементов, у которых индекс первого вхождения
    // равен текущему индексу, это гарантирует уникальность элементов
    return _array.indexOf(value) === index;
});

console.log(uniqueArray);