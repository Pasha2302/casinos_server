var isCreateCheckBox = false;

const allInlineBlocks = [];
const inlineBlockGroups = [
    {
        titleBlock: "GENERAL INFO",
        listIds: [
            "#bonus_amount-group", "#bonus_value-group",
            "#bonus_min_dep-group", "#day_of_week-group", "#bonus_expiration-group",
            "#promotion_period-group", "#sticky-group", "#bonus_max_win-group",
        ]
    },
    {
        titleBlock: "FREE SPINS",
        listIds: [
            "#free_spin_amount-group", "#one_spin-group", "#bonus_slot-group", "#wager-group",
        ]
    },
    {
        titleBlock: "WAGERING",
        listIds: [
            "#slots_wagering-group", "#turnover_bonus-group", "#wagering_bonus_plus_deposit-group",
            "#wagering-group", "#wagering_contribution-group",
        ]
    },
    {
        titleBlock: "RESTRICTIONS",
        listIds: [
            "#restriction_game-group", '#bonus_restriction_providers-set',
            "#restriction_country-group", "#restriction_rtp_game-group",
        ]
    },
    {
        titleBlock: "MAX BET",
        listIds: [
            "#max_bet-group", "#max_bet_automatic-group",
        ]
    },
    {
        titleBlock: "OTHER INFO",
        listIds: [
            "#buy_feature-group", "#special_note-group",
        ]
    },
]


function checkErrorFields(allBlocks) {
    for (let inlineBlock of allBlocks) {
        if (inlineBlock.find('.errorlist').length > 0) {
            inlineBlock.slideToggle();
        }
    };
}

function combiningBlocks(blockGroups) {
    // Добавляем каждый блок из списка ID к коллекции
    for (let dataObjBlock of blockGroups) {
        let inlineBlocks = $();
        for (let blockId of dataObjBlock.listIds) {
            inlineBlocks = inlineBlocks.add($(blockId));
        }

        // console.log("\nInline Blocks:", inlineBlocks)
        // Создаем новый контейнер div с заголовком-кнопкой:
        let containerDiv = $('<div class="container-group">'
        ).attr('id', dataObjBlock.titleBlock.toLowerCase().replace(' ', '-'));

        let titleButton = $('<button type="button" class="button-title">').text(dataObjBlock.titleBlock);

        // Стили для контейнера
        containerDiv.css({
            'width': 'auto',        // или любое другое значение
            'background-color': '#f0f0f0',
            'border': '1px solid #ccc',
            'padding': '10px',
            'margin': '10px', // отступы вокруг контейнера
            'display': 'block',
        });

        // Стили для кнопки-заголовка
        titleButton.css({
            'margin-bottom': '10px',         // Отступ снизу кнопки
            'padding': '10px 20px',           // Внутренний отступ кнопки: 10px сверху и снизу, 20px слева и справа
            'font-size': '18px',              // Размер шрифта текста внутри кнопки
            'color': '#fff',                  // Цвет текста внутри кнопки
            'border': 'none',                 // Уьрать границу кнопки
            'cursor': 'pointer',              // Изменяем указатель при наведении для обозначения кликабельности
            'border-radius': '5px',           // Радиус закругления углов кнопки
        });

        // Оборачиваем список блоков в блок контейнер:
        inlineBlocks.wrapAll(containerDiv);
        // Вставляем заголовок перед первым блоком
        titleButton.insertBefore(inlineBlocks.first());

        // Переставляем элементы в соответствии с порядком в listIds
        let checkBlock = []
        for (let i = 0; i < dataObjBlock.listIds.length; i++) {
            let currentId = dataObjBlock.listIds[i];
            let currentIndex = inlineBlocks.index(inlineBlocks.filter(currentId));
            let currenStrId = currentId.replace('#', '');

            if (!checkBlock.includes(currenStrId) & currenStrId !== inlineBlocks.eq(i).attr('id')) {
                checkBlock.push(currenStrId);
                checkBlock.push(inlineBlocks.eq(i).attr('id'));

                // console.log(currenStrId + ' // ' + inlineBlocks.eq(i).attr('id'));
                // inlineBlocks.eq(currentIndex).before(inlineBlocks[i]);
                inlineBlocks.eq(i).before(inlineBlocks.eq(currentIndex));
            };
        };

        // Скрыть блоки при изначальной загрузке и обновлении страницы
        inlineBlocks.hide();

        // Добавляем обработчик события для сворачивания и разворачивания блока
        titleButton.click(function () {
            inlineBlocks.slideToggle();
        });

        allInlineBlocks.push(inlineBlocks);
    };
}


function addBlocks() {
    $(".field-bonus_plus_freespins_value").parent().first().attr('id', 'calculations-fild_1');
    $(".field-calculation_bonus_only").parent().first().attr('id', 'calculations-fild_2');
    // $(".field-days").parent().first().attr('id', 'field-days_1');
    inlineBlockGroups.push(
        {
            titleBlock: "CALCULATIONS",
            listIds: [
                "#calculations-fild_1", "#calculations-fild_2",
            ]
        }
    );
}


// #other-info
function sortingBasicBlocks() {
    let calculationBlock = $('#calculations');
    let allContainerGroup = $('.container-group');

    allContainerGroup.eq(allContainerGroup.length - 1).after(calculationBlock.first());

    // $('.container-group').first().before( $("#turnover_bonus-group").first() );
    $('#calculations').first().before($('#other-info').first());

    $('#restrictions').first().before($('#free-spins').first());
    $('#general-info').first().after($('#free-spins').first());
    $('#restrictions').first().before($('#general-info').first());

    // $('#bonus_expiration-group').before( $('.field-days').parent().first() );
}


function setIdBlocksFieldSet() {
    let blocksFieldSet = $('.module.aligned ');
    // console.log(blocksFieldSet);
    for (let fieldSet of blocksFieldSet) {
        if (!fieldSet.hasAttribute('id') && fieldSet.querySelector('h2')) {
            let setId = fieldSet.querySelector('h2').innerText.toLowerCase().replace(/ /g, '_') + '-set';
            // console.log(`Set ID: ${setId}`);
            fieldSet.setAttribute('id', setId);
        }
    }
}


// =============================================================================== >>>>>>>>
function createDataCheckBox(casinoKey) {
    const autocompleteBlocksIds = [
        'bonus_min_dep-group', 'bonus_max_win-group',
        'bonus_expiration-group', 'sticky-group',
        'turnover_bonus-group', 'wagering_bonus_plus_deposit-group',
        'wagering_contribution-group', 'restriction_game-group',
        'restriction_country-group', 'restriction_rtp_game-group',
        'max_bet-group', 'max_bet_automatic-group', 'buy_feature-group',
    ];
    const listidCheckBoxs = [];
    var dataChechBox = {};
    dataChechBox[casinoKey] = {};

    const autocompleteBlocksElms = autocompleteBlocksIds.map((value) => {
        if (!dataChechBox[casinoKey][`${value}-check_id`]) {
            let suffixIdRow = '-' + value.replace('-group', '');
            let prefixIdValue = 'id_' + value.replace('group', '');

            dataChechBox[casinoKey][`${value}-check_id`] = { isChecked: false };
            dataChechBox[casinoKey][`${value}-check_id`]['data'] = [];
            dataChechBox[casinoKey][`${value}-check_id`]['suffixIdRow'] = suffixIdRow;
            dataChechBox[casinoKey][`${value}-check_id`]['prefixIdValue'] = prefixIdValue;
        }
        if (!listidCheckBoxs.includes(`${value}-check_id`)) { listidCheckBoxs.push(`${value}-check_id`); }
        return document.getElementById(value);
    });

    if (!isCreateCheckBox) {
        for (let elmAutoBlock of autocompleteBlocksElms) {
            const checkBox = document.createElement('input');
            const elmLable = document.createElement('lable');
            const elmH2 = elmAutoBlock.querySelector('.module h2');

            if (!elmH2) { console.log('!!! No H2 !!!', elmAutoBlock) }
            const texth2 = elmH2.textContent.toLowerCase().replaceAll(' ', '_');
            const idCheckBox = `${elmAutoBlock.id}-check_id`;

            checkBox.setAttribute('type', 'checkbox');
            checkBox.setAttribute('name', texth2);
            checkBox.setAttribute('id', idCheckBox);
            checkBox.setAttribute('class', 'check-save-block');
            elmLable.setAttribute('for', idCheckBox);

            elmH2.appendChild(checkBox);
            elmH2.appendChild(elmLable);
            elmLable.textContent = 'Save Data Block.';

            // <<<< =============== Добавляем обработчик события изменения состояния чекбокса  =============== >>>>
            checkBox.addEventListener("change", function (event) {
                const eventTargetElm = event.target;
                const checkBoxId = eventTargetElm.id
                const _casinoKey = $('#id_casino').select2('data')[0].id;

                dataChechBox[_casinoKey][checkBoxId].isChecked = eventTargetElm.checked;
                window.getDataAutoFillBonus(eventTargetElm, dataChechBox, _casinoKey);
                // Проверяем, установлена ли галочка в чекбоксе
                if (eventTargetElm.checked) { eventTargetElm.parentElement.style.backgroundColor = 'rgb(19 180 98)'; }
                else { eventTargetElm.parentElement.style.backgroundColor = ''; }
            });
        }
        isCreateCheckBox = true;
    }

    window.apiAutoFill('GET', casinoKey)
        .then(response => {
            if (response.data) { dataChechBox[casinoKey] = response.data }
            else { window.apiAutoFill('POST', casinoKey, dataChechBox[casinoKey]) };
            // console.log("\nRes API <'GET', casinoKey> check Casino In Db:", response);
            // console.log("\ndataChechBox:", dataChechBox);

            console.log('\n\nПроверка установленых Чек-Боксов ...', dataChechBox);
            listidCheckBoxs.forEach((valueId) => {
                const checkbox = document.getElementById(valueId);
                if (dataChechBox[casinoKey] && dataChechBox[casinoKey][valueId].isChecked) {
                    checkbox.checked = true;
                    if (checkbox.checked) { checkbox.parentElement.style.backgroundColor = 'rgb(19 180 98)' };
                } else {
                    checkbox.checked = false;
                    checkbox.parentElement.style.backgroundColor = '';
                }
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}


// =============================================================================== //
function checkingCurrentPage(casinoKey) {
    const regex = /bonus\/add\//;
    if (regex.test(window.location.href)) {
        // console.log("\nСтраница находится на адресе, содержащем 'bonus/add/'");
        // window.setAutoFillBonus(casinoKey);
        setTimeout(() => {
            deleteTags();
        }, 2000);

        window.setAutoFillBonus2(casinoKey);
    }
}


function createWhenChangingCasino() {
    $('#id_casino').on('select2:select', function (e) {
        const _data = e.params.data;
        console.log(_data);

        if (_data) { createDataCheckBox(_data.id); };  // _data.id: casinoKey
        checkingCurrentPage(_data.id);
        setcalculations();
    });
}


function setDataChechBox() {
    if ($('#id_casino').select2('data')[0]) {
        const _casinoKey = $('#id_casino').select2('data')[0].id;
        createDataCheckBox(_casinoKey);
        // checkingCurrentPage();
    }
}


const createElementsPagination = (targetElement, indexId) => {
    // Находим элемент, в который нужно встроить блок кода:
    // let targetElement = document.querySelector('#restriction_game-0 .selector-available h2');

    // Создаем элементы <select>, <label> и <button> с нужными атрибутами и текстом
    let selectElement = document.createElement('select');
    let labelElement = document.createElement('label');
    let buttonElement = document.createElement('button');

    selectElement.setAttribute('id', 'page-list' + `-${indexId}`);
    selectElement.setAttribute('class', 'page-list');

    buttonElement.setAttribute('id', 'send-filter-data' + `-${indexId}`);
    buttonElement.setAttribute('class', 'send-filter-data');
    buttonElement.setAttribute('type', 'button');
    buttonElement.textContent = 'Send Filter';

    // Устанавливаем атрибуты и текст для label
    labelElement.textContent = 'Page:';
    labelElement.setAttribute('for', 'page-list' + `-${indexId}`);
    labelElement.setAttribute('class', 'select-game-label');

    // Вставляем элементы в DOM
    targetElement.appendChild(labelElement);
    targetElement.appendChild(selectElement);
    selectElement.insertAdjacentElement('afterend', buttonElement);
}


const createPagination = () => {
    const slotBlock = document.querySelector('#slots_wagering-group');
    const restrictionGame = document.querySelector('#restriction_game-0 .selector-available h2');
    const slotsFormsElms = slotBlock.querySelectorAll('.form-row.dynamic-slots_wagering .field-slot .selector-available h2');
    const listTargetElementsFilter = [restrictionGame, ...slotsFormsElms];
    listTargetElementsFilter.forEach( (s, i) => createElementsPagination(s, i) );
}


// =============================================================================== //

$(document).ready(function () {
    const setIntervalId = setInterval(() => {
        const checkElement = document.querySelector('#slots_wagering-group');
        if (checkElement) {
            clearInterval(setIntervalId);

            addBlocks();
            setIdBlocksFieldSet();

            combiningBlocks(inlineBlockGroups);
            sortingBasicBlocks();

            checkErrorFields(allInlineBlocks);

            createWhenChangingCasino();
            createPagination();
            setDataChechBox();
        }
    }, 300)
    
});
