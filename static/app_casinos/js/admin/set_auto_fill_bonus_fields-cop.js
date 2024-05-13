'use strict';


// function settingFieldAttributes(checkBoxId) {
//     const dataAttributes = {};
//     if (checkBoxId === 'bonus_min_dep-group-check_id') {
//         dataAttributes.parentBlock = document.getElementById(checkBoxId).closest('.module');
//         dataAttributes.addRow = dataAttributes.parentBlock.querySelector('.add-row a');

//         dataAttributes.value = dataAttributes.parentBlock.querySelector(`[id^="id_"][id$="value"]`);
//         dataAttributes.symbol = $(dataAttributes.parentBlock).find(`[id^="id_bonus_"][id$="-symbol"]`).eq(0);
//         dataAttributes.source = dataAttributes.parentBlock.querySelector(`[id^="id_bonus_"][id$="-selected_source"]`);
//     }
//     console.log("\nData Attributes:", dataAttributes);
// }


{
    // <<< ========================================================================================================== >>> //


    function addExpirationDays(parentRow, _data) {
        let expirationDaysElm = parentRow.querySelector(`[id^="id_bonus_"][id$="-days"]`);
        let selectedSourceElm = parentRow.querySelector(`[id^="id_bonus_"][id$="-selected_source"]`);
        expirationDaysElm.value = _data.expirationDays;
        selectedSourceElm.value = _data.source;
    }


    function optionOne(data, parentRow) {
        if (data.expirationDays) {
            addExpirationDays(parentRow, data);
        } else {
            let valueElm = parentRow.querySelector(`[id^="id_bonus_"][id$="_value"]`);
            let symbolElm = $(parentRow).find(`[id^="id_bonus_"][id$="-symbol"]`).eq(0);
            let selectedSourceElm = parentRow.querySelector(`[id^="id_bonus_"][id$="-selected_source"]`);

            valueElm.value = data.value;
            symbolElm.select2('trigger', 'select', { data: data.symbol });
            selectedSourceElm.value = data.source;

            if (data.unlimited !== null) {
                let unlimitedElm = parentRow.querySelector('[id^="id_bonus_"][id$="-unlimited"]');
                unlimitedElm.checked = data.unlimited;
            }
        }
    }


    function optionTwo() {

    }


    function addDataBonus(_data, checkBoxId) {
        const datas = _data;
        // Ищем ближайший родительский элемент с указанным селектором
        console.log("\nCheck Box ID:", checkBoxId);
        const parentBlock = document.getElementById(checkBoxId).closest('.module');
        const addRow = parentBlock.querySelector('.add-row a');
        const elmRows = parentBlock.querySelectorAll('[class^="form-row dynamic-bonus_"]');

        elmRows.forEach((elm) => {
            let elmDelete = elm.querySelector('.inline-deletelink');
            if (elmDelete) elmDelete.click();
        });

        addRow.click();
        for (const [index, data] of datas.entries()) {
            let parentRows = parentBlock.querySelectorAll('[class^="form-row dynamic-bonus_"]');
            let countNewRows = parentRows.length
            let parentRow = parentRows[index];

            firstOption(data, parentRow);
            if (countNewRows === datas.length) break;
            addRow.click();
        }
    }


    function addDataBonusMaxWin(_data) {

    }


    function addDataBonusRestrictionGame(_data) {
        const data = _data;
        const selectedSourceElm = document.querySelector('#id_restriction_game-0-selected_source');
        let selectElementTo = document.getElementById('id_restriction_game-0-game_to');

        if (!data[0]) {
            selectElementTo.innerHTML = '';
            selectedSourceElm.value = 'undefined';
            window.SelectBox.init('id_restriction_game-0-game_to');
            return;
        };

        const sourceValue = data.pop().source;
        selectedSourceElm.value = sourceValue;
        selectElementTo.innerHTML = '';

        for (const datas of data) {
            let optionElement = document.createElement('option');

            optionElement.value = datas.id; // Устанавливаем значение
            optionElement.textContent = datas.text; // Устанавливаем текст
            optionElement.title = datas.text; // Устанавливаем title
            selectElementTo.appendChild(optionElement); // Добавляем элемент <option> в <select>
        }

        window.SelectBox.init('id_restriction_game-0-game_to');
    }


    window.setAutoFillBonus2 = function (casinoKey) {
        // const data = [
        //     { value: 120, symbol: { id: '140', text: 'CAD | Canadian dollar', selected: true }, source: 'support' },
        //     { value: 160, symbol: { id: '79', text: 'GMD | Gambian dalasi', selected: true }, source: 'support' },
        //     { value: 200, symbol: { id: '78', text: 'CUP | Cuban peso', selected: true }, source: 'support' },
        // ];
        // const dataGame = [
        //     { id: '10367', text: '10000 Wonders 10k Ways' },
        //     { id: '13327', text: '10000 BC DoubleMax GigaBlox' },
        //     { id: '25468', text: 'Bargainista' },
        //     { source: 'support' },
        // ];

        const checkListId_1 = [
            'bonus_min_dep-group-check_id', 'bonus_max_win-group-check_id', 'bonus_expiration-group-check_id',
        ]
        var dataChechBox = JSON.parse(localStorage.getItem("dataChechBox"));

        for (let key in dataChechBox[casinoKey]) {

            if (checkListId_1.includes(key)) {
                if (dataChechBox[casinoKey][key].isChecked) {
                    console.log("\nДобавить Данные!!!");
                    settingFieldAttributes(key);
                    addDataBonus(dataChechBox[casinoKey][key].data, key)
                } else {
                    console.log("\nУдалить Данные!!!");
                    addDataBonus([], key);
                };
            }

            if (key === 'restriction_game-group-check_id') {
                if (dataChechBox[casinoKey][key].isChecked) {
                    addDataBonusRestrictionGame(dataGame);
                } else {
                    addDataBonusRestrictionGame([]);
                };
            }
        }
    }

}
