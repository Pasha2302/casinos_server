'use strict';

const $ = django.jQuery;


let observers = {};


function newFilter() {
    const checkIdsCurrency = ['id_licenses_from', 'id_licenses_to'];
    const SelectBox = window.SelectBox;

    if (!SelectBox) return;

    SelectBox.filter = function (id, text) {
        if (id === 'id_restriction_game-0-game_from') return;
        console.log("\nSelect Filter [id]:", id)
        // -------------------------------------------------------
        const inputTokens = text.toLowerCase().split(',').map((t) => t.trim());
        console.log('inputTokens:', inputTokens);

        for (const node of SelectBox.cache[id]) {
            if (inputTokens[0] === '') {
                // console.log('\n Отображаю все записи.');
                node.displayed = 1;
                continue;
            }

            node.displayed = 0;
            // const node_texts = node.text.toLowerCase().split('|').map((t) => t.trim());
            const node_text = node.text.toLowerCase();
            for (const token of inputTokens) {

                if (!checkIdsCurrency.includes(id)) {
                    let regex = new RegExp(`(?:^|\\s|[^\\p{L}])${escapeRegExp(token)}(?:$|\\s|[^\\p{L}])`, 'ui');
                    if (regex.test(node_text)) {
                        node.displayed = 1;
                        break;
                    };
                } else {
                    if (node_text.includes(token)) {
                        node.displayed = 1;
                        break;
                    }
                }
            };
        };

        SelectBox.redisplay(id);
    };
    // Функция для экранирования спецсимволов в регулярном выражении
    function escapeRegExp(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); // $& означает всю совпавшую строку
    }
};


function deleteTags() {
    // console.log("\n\nУдаляю лишние Теги ...")
    const elmsHelpTimeZone = document.querySelectorAll('.help.timezonewarning');
    const elmD = document.querySelector('#add_id_day_of_week-0-days');
    if (elmD) elmD.remove();

    // const deleteLinks = document.querySelectorAll('.inline-deletelink');
    const searchElmsH3 = document.querySelectorAll(".inline-related");
    const searchElmsP = document.querySelectorAll("td[class='original']");

    const timezoneWarning = document.querySelectorAll('.timezonewarning');
    if (timezoneWarning) timezoneWarning.forEach((element) => {
        if (element) element.remove();
    })

    elmsHelpTimeZone.forEach(element => element.remove());

    searchElmsP.forEach(element => {
        let pElement = element.querySelector('p');
        if (pElement) {
            element.removeChild(pElement);
        }
    });

    searchElmsH3.forEach(element => {
        let h3Element = element.querySelector('h3');
        if (h3Element) {
            element.removeChild(h3Element);
        }
    });

    // deleteLinks.forEach(element => element.remove());
};

// ======================================================================================================================= //

function capitalizeEveryWord(str) {
    return str.replace(/\b\w/g, function (match) {
        return match.toUpperCase();
    });
}


function getValuesAndCountElm(idBlock) {
    let listValuesObj = document.getElementById(idBlock).querySelector('select[class="filtered"]').querySelectorAll('option');
    let listValuesStr = [];

    for (let valueObj of listValuesObj) {
        let dataText = valueObj.innerHTML.split('|')[0].trim();
        listValuesStr.push(dataText);
    };
    // console.log("List Values Objects:", listValuesObj, typeof listValuesObj);
    // console.log("List Values String:", listValuesStr, typeof listValuesStr);
    return {
        valuesStr: listValuesStr.join(','),
        count: listValuesStr.length,
    }
}


// Функция для копирования выбранных элементов в буфер обмена:
function eventBtnInfoFilter(event) {
    let eventBlockId = event.target.attributes.data.nodeValue;
    let valuesAndCount = getValuesAndCountElm(eventBlockId);
    let btnText = event.target.innerText;
    var messageContainer;
    // Делаем кнопку неактивной
    $(event.target).prop('disabled', true);

    navigator.clipboard.writeText(valuesAndCount.valuesStr)
        .then(() => {
            messageContainer = $('<span>', {
                class: 'copy-message success',
                text: ' (Copied to clipboard)'
            });
        })
        .catch(err => {
            messageContainer = $('<span>', {
                class: 'copy-message error',
                text: ' (Copy error)'
            });
        })
        .finally(() => {
            // Добавляем сообщение к кнопке
            $(event.target).append(messageContainer);

            // Удаляем сообщение через 3 секунды
            setTimeout(() => {
                messageContainer.fadeOut(() => {
                    messageContainer.remove();
                });
                // Делаем кнопку снова активной
                $(event.target).prop('disabled', false);
            }, 3000);
        });
}


// Функция для отслеживания изменений в дочерних элементах <select>
function observeSelectChildren(blockId) {
    // let selectElement = document.getElementById(blockId).querySelector('select[class="filtered"]');
    let selectElement = document.querySelector('#' + blockId + ' select.filtered');
    let prevLength = selectElement.options.length;
    // console.log(selectElement);
    let observer = new MutationObserver(function (mutations) {
        for (let mutation of mutations) {
            // console.log('Тип мутации:', mutation.type);
            // console.log('Цель мутации:', mutation.target);
            // console.log('Мутация:', mutation);
            // Проверяем, были ли добавлены или удалены дочерние элементы
            if (mutation.type === 'childList') {
                let newLength = selectElement.options.length;
                if (newLength !== prevLength) {
                    // console.log('Количество элементов в блоке изменилось:', newLength);
                    let btn = $(`button[data="${blockId}"]`);
                    btn.text(btn.text().replace(/Count \(\d+\)/, `Count (${newLength})`));
                    prevLength = newLength; // Обновляем предыдущее значение
                    break; // Выходим из цикла после первого изменения
                }
            }
        }
    });
    // observer.observe(selectElement, { childList: true, subtree: true });
    observer.observe(selectElement, { childList: true, subtree: false });
    observers[blockId] = observer; // сохраняем экземпляр наблюдателя
}


// Функция для прекращения прослушивания изменений для всех блоков
function stopObservingAllBlocks() {
    for (let blockId in observers) {
        observers[blockId].disconnect();
    }
}


function addButtonToCopyData() {
    let blocksChosen = document.querySelectorAll('.selector-chosen');
    if (blocksChosen.length === 0) return;

    for (let blockChosen of blocksChosen) {
        let blockId = blockChosen.attributes.id.nodeValue;
        if (blockId === 'id_restriction_game-0-game_selector_chosen') continue;

        let valuesAndCount = getValuesAndCountElm(blockId);
        let btnInfoFilter = $(`<button type="button" class="btn-info-filter" data="${blockId}">`);
        let textH2 = capitalizeEveryWord(blockChosen.querySelector('h2').innerText.replace('Chosen', '').trim());
        // console.log("\nBlock Chosen ID:", blockId);
        btnInfoFilter.text(`${textH2} Count (${valuesAndCount.count})`);

        $(blockChosen).first().find('a').before(btnInfoFilter);
        btnInfoFilter.on('click', eventBtnInfoFilter);
    };

    // После добавления всех кнопок запускаем наблюдение за изменениями
    for (let blockChosen of blocksChosen) {
        let blockId = blockChosen.attributes.id.nodeValue;
        observeSelectChildren(blockId);
    };

    $('.submit-row').find('input[type="submit"], a').each(function () {
        // Добавляем обработчик события для каждой кнопки сохранения или удаления.
        $(this).on('click', function (event) {
            stopObservingAllBlocks();
            // console.log('Кнопка нажата:', event.target.value);
        });
    });

}


function setClass() {
    const elmsDelete = $('th:contains("Delete?")');
    elmsDelete.addClass('delete-use');
    // console.log(elmsDelete);
}


function func1() {
    const blocks = $('.inline-related.tabular fieldset.module');

    for (let block of blocks) {
        let elmsTh = $(block).find('th');
        for (let i = 0; i < elmsTh.length; i++) {
            if (elmsTh[i].classList.contains('column-selected_source')) {
                elmsTh[i - 1].style.width = '100%';
                // console.log(elmsTh[i]);
            };
        };
        // console.log('\n', elmsTh.length);
        // console.log(elmsTh[2].classList);
        // console.log('=='.repeat(40))
    };
}


function formatNumbers() {
    const integerFields = document.querySelectorAll('input[type="number"]');
    integerFields.forEach(field => {
        const value = field.value;
        if (/^-?\d+e-\d+$/.test(value)) { // Проверяем, соответствует ли значение формату экспоненты
            const [base, exponent] = value.split('e-'); // Разбиваем значение на основание и экспоненту
            const result = '0.' + '0'.repeat(exponent - 1) + base; // Составляем строку с добавлением нулей и точки
            field.value = result; // Устанавливаем новое значение поля
        }

        field.addEventListener('input', function () {
            // Получаем значение поля и преобразуем его в число
            let value2 = parseInt(this.value);
            if (value2 < 0) {
                // Убираем знак "-"
                this.value = Math.abs(value2);
            }
        });
    });
}


$(document).ready(function () {
    const setIntervalId = setInterval(() => {
        const checkElement = document.querySelector('#bonuses-group');
        const checkElement2 = document.querySelector('#slots_wagering-group');
        const checkElement3 = document.querySelector('#level_loyalty-group');
        if (checkElement || checkElement2 || checkElement3) {
            clearInterval(setIntervalId);

            newFilter();
            deleteTags();
            addButtonToCopyData();
            setClass();
            func1();
            formatNumbers();
        }
    }, 300)

});

