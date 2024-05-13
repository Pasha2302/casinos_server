// Сохраняем стандартную функцию $.fn.select2
// var originalSelect2 = $.fn.select2;

{
    function testFunc1() {
        console.log('\n\ntestFunc Запущена! ...')

        const SelectFilter = window.SelectFilter

        SelectFilter.any_selected = function (field) {
            // Temporarily add the required attribute and check validity.
            // console.log('\n\nField: ', field);
            field.required = true;
            const any_selected = field.checkValidity();
            field.required = false;
            return any_selected;
        };
    };


    function testFunc2() {
        const select = $('#id_bonus_min_dep-0-symbol');
        // Добавляем обработчик события select2:results
        select.on('select2:results', function (event) {
            var results = event.params.data.results; // Получаем результаты запроса

            // Здесь вы можете использовать результаты запроса по вашему усмотрению
            // Например, обновить ваш список Select2 с новыми данными
            console.log('\nSelect2 results:', results)
        });

        // Также вы можете использовать событие select2:select
        select.on('select2:select', function (event) {
            var data = event.params.data; // Получаем выбранный элемент

            // Здесь вы можете использовать выбранный элемент по вашему усмотрению
            console.log('Select2 select:', data)
        });

        select.on('results:previous', function (event) {
            // var data = event.params.data;
            // Здесь вы можете использовать выбранный элемент по вашему усмотрению
            console.log('Select2 previous:', event.params)
        });

        // select.select2('trigger', 'query', { page: 3 });
        // select.select2('open');
        // select.select2('close');
        //При открытом списке:
        // select.select2('trigger', 'results:next');
        // select.select2('trigger', 'results:select');

        //установить значение:
        const dataS = { id: '4', text: 'MXN | Mexican peso', selected: true };
        const dataSUn = { id: '4' };
        select.select2('trigger', 'select', { data: dataS });

        setTimeout(() => {
            select.select2('trigger', 'unselect', { data: dataSUn });
        }, 10000)

    };

    // $(document).ready(function () {
    //     setTimeout(testFunc2, 6000);
    // });

}


function test3() {
    const selectId = $('#id_bonus_min_dep-0-symbol');
    const data = { id: '140', text: 'CAD | Canadian dollar', selected: true };
    // Очистка выбора
    selectId.val(null).trigger('change');
    // Установка выбора
    setTimeout(
        () => { selectId.select2('trigger', 'select', { data: data }); }, 4000
    )
    // select.select2('trigger', 'select', { data: data });

    // Уничтожение элемента управления Select2:
    // $(selectId).select2('destroy');
}



// $(document).ready(function () {

//     function wrapperFilter(element) {
//         // Вставить тег <div> перед <h2>
//         element.insertAdjacentHTML('beforebegin', '<div class="wrapper-filter_1 container"></div>');
//         document.querySelector('.wrapper-filter_1').appendChild(element) // Перемещаем h2 в div (оборачиваем h2 блоком div)
//     }

//     function waitForElementToLoad() {
//         var checkExist = setInterval(function () {
//             var element = document.querySelector('#restriction_game-0 .selector-available h2');
//             if (element) {
//                 clearInterval(checkExist); // Остановить проверку, если элемент найден
//                 wrapperFilter(element);
//             }
//         }, 500);
//     }

//     waitForElementToLoad();
//     setTimeout(test3, 6000);


// });


// BONUS MIN DEP VALUE
// BONUS MAX WIN VALUE
// BONUS EXPIRATION (AMOUNT OF DAYS)
// STICKY OR NOT STICKY
// TURNOVER BONUS
// WAGERING BONUS PLUS DEPOSIT
// WAGERING CONTRIBUTION
// BONUS RESTRICTION GAME
// BONUS RESTRICTION COUNTRY
// BONUS RESTRICTION RTP GAME
// BONUS MAX BET
// BONUS MAX BET AUTOMATIC
// BONUS BUY FEATURE


// const autocompleteBlocksIds = [
//     'bonus_min_dep-group', 'bonus_max_win-group',
//     'bonus_expiration-group', 'sticky-group',
//     'turnover_bonus-group', 'wagering_bonus_plus_deposit-group',
//     'wagering_contribution-group', 'restriction_game-group',
//     'restriction_country-group', 'restriction_rtp_game-group',
//     'max_bet-group', 'max_bet_automatic-group', 'buy_feature-group',
// ];


// setTimeout(
//     () => {
//         let casinoKey = $('#id_casino').select2('data')[0].id;
//         var dataChechBox = { listidCheckBoxs: [], };

//         if (localStorage.getItem('dataChechBox')) {
//             dataChechBox = JSON.parse(localStorage.getItem('dataChechBox'));
//         };

//         if (!dataChechBox[casinoKey]) dataChechBox[casinoKey] = {};
//         const autocompleteBlocksElms = autocompleteBlocksIds.map((value) => document.getElementById(value))

//         for (let elmAutoBlock of autocompleteBlocksElms) {
//             var checkBox = document.createElement('input');
//             let elmLable = document.createElement('lable');

//             let elmH2 = elmAutoBlock.querySelector('.module h2');
//             if (!elmH2) { console.log('!!! No H2 !!!', elmAutoBlock) }
//             let texth2 = elmH2.textContent.toLowerCase().replaceAll(' ', '_');

//             let idCheckBox = `${texth2}-check_id`;

//             if (!dataChechBox.listidCheckBoxs.includes(idCheckBox)) {
//                 dataChechBox.listidCheckBoxs.push(idCheckBox);
//             }

//             checkBox.setAttribute('type', 'checkbox');
//             checkBox.setAttribute('name', texth2);
//             checkBox.setAttribute('id', idCheckBox);
//             checkBox.setAttribute('class', 'check-save-block');
//             elmLable.setAttribute('for', idCheckBox)

//             elmH2.appendChild(checkBox);
//             elmH2.appendChild(elmLable);
//             elmLable.textContent = 'Save Data Block.'

//             // Добавляем обработчик события изменения состояния чекбокса
//             checkBox.addEventListener("change", function (event) {
//                 let eventTargetElm = event.target;
//                 let elmId = eventTargetElm.id
//                 // Получаем состояние чекбокса
//                 let isChecked = eventTargetElm.checked;

//                 dataChechBox = JSON.parse(localStorage.getItem("dataChechBox"));
//                 dataChechBox[casinoKey][elmId] = isChecked;

//                 localStorage.setItem('dataChechBox', JSON.stringify(dataChechBox));
//                 // Проверяем, установлена ли галочка в чекбоксе
//                 if (event.target.checked) {
//                     eventTargetElm.parentElement.style.backgroundColor = 'rgb(19 180 98)';
//                 } else {
//                     eventTargetElm.parentElement.style.backgroundColor = '';
//                 }
//             });
//         }

//         let checkData = JSON.parse(localStorage.getItem("dataChechBox"));
//         if (checkData !== null) {
//             dataChechBox.listidCheckBoxs.forEach(
//                 (valueId) => {
//                     let checkbox = document.getElementById(valueId);
//                     if (checkData[casinoKey]) {
//                         // console.log("\n\n!!! checkData[casinoKey]:", checkData[casinoKey]);
//                         checkbox.checked = (checkData[casinoKey][valueId] === true);
//                         if (checkbox.checked) checkbox.parentElement.style.backgroundColor = 'rgb(19 180 98)';
//                     }
//                 }
//             );
//         }

//         let jsonDataChechBox = JSON.stringify(dataChechBox);
//         localStorage.setItem('dataChechBox', jsonDataChechBox)

//     }, 6000
// )



// rgb(19 180 98)