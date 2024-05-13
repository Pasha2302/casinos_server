'use strict';

{
    function addDataBonusMinDip(_data) {
        const data = _data;
        // Ищем ближайший родительский элемент с указанным селектором
        const parentBlock = document.getElementById('bonus_min_dep-group-check_id').closest('.module');
        const addRow = parentBlock.querySelector('.add-row a');
        let elmRows = document.querySelectorAll('.form-row.dynamic-bonus_min_dep') //.slice(1,);

        elmRows.forEach((elm) => {
            let elmDelete = elm.querySelector('.inline-deletelink');
            console.log('elmDelete:', elmDelete);
            if (elmDelete) elmDelete.click();
            else {
                let minDipValueElm = document.querySelector(`[id^="id_bonus_min_dep-"][id$="-min_value"]`);
                let symbolElm = $(`[id^="id_bonus_min_dep-"][id$="-symbol"]`);
                let selectedSourceElm = document.querySelector(`[id^="id_bonus_min_dep-"][id$="-selected_source"]`);
                minDipValueElm.value = '';
                symbolElm.val(null).trigger('change');
                selectedSourceElm.value = 'undefined';
            }
        });

        let startIndex = Number(document.querySelector(`[id^="id_bonus_min_dep-"][id$="-min_value"]`).id.match(/\d+/)[0]);
        for (const [index, datas] of data.entries()) {
            let _Id = index + startIndex;
            // console.log('\datas, index, All data length:', datas, index, data.length);
            let minDipValueElm = document.querySelector(`[id^="id_bonus_min_dep-"][id*="${_Id}"][id$="-min_value"]`);
            let symbolElm = $(`[id^="id_bonus_min_dep-"][id*="${_Id}"][id$="-symbol"]`);
            let selectedSourceElm = document.querySelector(
                `[id^="id_bonus_min_dep-"][id*="${_Id}"][id$="-selected_source"]`
            );

            minDipValueElm.value = datas.value;
            symbolElm.select2('trigger', 'select', { data: datas.symbol });
            selectedSourceElm.value = datas.source;

            if (index + 1 >= data.length) break;
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
        console.log('Source Value:', sourceValue);
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


    window.setAutoFillBonus = function (casinoKey) {
        // const data = [
        //     { value: 120, symbol: { id: '140', text: 'CAD | Canadian dollar', selected: true }, source: 'support' },
        //     { value: 160, symbol: { id: '79', text: 'GMD | Gambian dalasi', selected: true }, source: 'support' },
        //     { value: 200, symbol: { id: '78', text: 'CUP | Cuban peso', selected: true }, source: 'support' },
        // ];
        const dataGame = [
            { id: '10367', text: '10000 Wonders 10k Ways' },
            { id: '13327', text: '10000 BC DoubleMax GigaBlox' },
            { id: '25468', text: 'Bargainista' },
            { source: 'support' },
        ];
        var dataChechBox = JSON.parse(localStorage.getItem("dataChechBox"));

        for (let key in dataChechBox[casinoKey]) {
            if (key === 'bonus_min_dep-group-check_id') {
                if (dataChechBox[casinoKey][key]) {
                    console.log("\nДобавить Данные!!!");
                    addDataBonusMinDip(dataChechBox[casinoKey][key].data)
                } else {
                    console.log("\nУдалить Данные!!!");
                    addDataBonusMinDip([]);
                };
            }

            if (key === 'restriction_game-group-check_id') {
                if (dataChechBox[casinoKey][key]) {
                    addDataBonusRestrictionGame(dataGame);
                } else {
                    addDataBonusRestrictionGame([]);
                };
            }
        }
    }

}
