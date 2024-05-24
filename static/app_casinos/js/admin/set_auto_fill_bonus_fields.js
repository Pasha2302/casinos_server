'use strict';


{
    // <<< ========================================================================================================== >>> //
    function addDataBonusMtoM(_datas) {
        if (!_datas.data.selectDataTo || _datas.data.selectDataTo.length === 0) {
            const selectElementTo = document.querySelector(`[id^="${_datas.prefixIdValue}"][id$="_to"]`);
            const selectedSourceElm = document.querySelector(`[id^="${_datas.prefixIdValue}"][id$="-selected_source"]`);
            selectElementTo.innerHTML = '';
            selectedSourceElm.value = 'undefined';
            window.SelectBox.init(selectElementTo.id);
            return;
        };

        const datas = _datas.data;
        let selectedSourceElm = document.getElementById(datas.idSourceValue);
        let selectElementTo = document.getElementById(datas.idSelectBlockTo);
        let selectElementFrom = document.getElementById('id_restriction_game-0-game_from');

        selectedSourceElm.value = datas.sourceValue;
        selectElementTo.innerHTML = '';
        selectElementFrom.innerHTML = '';

        for (const data of datas.selectDataTo) {
            let optionElement = document.createElement('option');

            optionElement.value = data.value; // Устанавливаем значение
            optionElement.textContent = data.text; // Устанавливаем текст
            optionElement.title = data.text; // Устанавливаем title
            optionElement.displayed = data.displayed;
            selectElementTo.appendChild(optionElement); // Добавляем элемент <option> в <select>
        }

        window.SelectBox.init(datas.idSelectBlockTo);
    }


    function addRtpGameGroup(_data, parentRow, prefixIdValue) {
        let selectedSourceElm = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="-selected_source"]`);
        let value = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="-value"]`);
        value.value = _data.rtpValue;
        selectedSourceElm.value = _data.source;
    }


    function addWageringBonusPlusDeposit(_data, parentRow, prefixIdValue) {
        let selectedSourceElm = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="-selected_source"]`);
        let value1 = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="-bonus_plus_deposit"]`);
        let value2 = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="-bonus_only"]`);

        value1.value = _data.value1;
        value2.value = _data.value2;
        selectedSourceElm.value = _data.source;
    }


    function addWageringContribution(_data, parentRow, prefixIdValue) {
        let valueElm = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="-value"]`);
        let symbolElm = $(parentRow).find(`[id^="${prefixIdValue}"][id$="-contribution_description"]`).eq(0);
        let selectedSourceElm = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="-selected_source"]`);

        valueElm.value = _data.value;
        symbolElm.select2('trigger', 'select', { data: _data.selectElm });
        selectedSourceElm.value = _data.source;
    }


    function addExpirationDays(_data, parentRow, prefixIdValue) {
        let expirationDaysElm = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="-days"]`);
        let selectedSourceElm = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="-selected_source"]`);
        expirationDaysElm.value = _data.expirationDays;
        selectedSourceElm.value = _data.source;
    }


    function optionOne(_data, parentRow, prefixIdValue) {
        if (_data.expirationDays) {
            addExpirationDays(_data, parentRow, prefixIdValue);
        } else {
            let valueElm = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="_value"]`);
            if (!valueElm) { valueElm = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="-value"]`); }

            let symbolElm = $(parentRow).find(`[id^="${prefixIdValue}"][id$="-symbol"]`).eq(0);
            let selectedSourceElm = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="-selected_source"]`);
            try {
                valueElm.value = _data.value;
            } catch (error) {
                console.error("\nПроизошла ошибка:", error);
                console.error("Input Data:", _data);
            }

            symbolElm.select2('trigger', 'select', { data: _data.symbol });
            selectedSourceElm.value = _data.source;
            if (_data.unlimited !== null) {
                let unlimitedElm = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="-unlimited"]`);
                unlimitedElm.checked = _data.unlimited;
            }
        }
    }


    function optionTwo(_data, parentRow, prefixIdValue) {
        let statusValue = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="${_data.elmSuffixId}"]`);
        let sourceValue = parentRow.querySelector(`[id^="${prefixIdValue}"][id$="-selected_source"]`);
        statusValue.checked = _data.statusValue;
        sourceValue.value = _data.source;
    }


    function addDataBonus(_data, checkBoxId) {
        const datas = _data.data;
        const suffixIdRow = _data.suffixIdRow;
        const prefixIdValue = _data.prefixIdValue;
        const checkListId_1 = [
            'bonus_min_dep-group-check_id', 'bonus_max_win-group-check_id',
            'bonus_expiration-group-check_id', 'max_bet-group-check_id',
        ];
        const checkListId_2 = [
            'turnover_bonus-group-check_id', 'max_bet_automatic-group-check_id',
            'sticky-group-check_id', 'buy_feature-group-check_id'
        ];

        // Ищем ближайший родительский элемент с указанным селектором
        const parentBlock = document.getElementById(checkBoxId).closest('.module');
        const addRow = parentBlock.querySelector('.add-row a');
        const elmRows = parentBlock.querySelectorAll(`[class^="form-row dynamic${suffixIdRow}"]`);

        elmRows.forEach((elm) => {
            let elmDelete = elm.querySelector('.inline-deletelink');
            if (elmDelete) elmDelete.click();
        });
        if (elmRows[0]) { addRow.click(); }

        for (const [index, data] of datas.entries()) {
            let parentRows = parentBlock.querySelectorAll(`[class^="form-row dynamic${suffixIdRow}"]`);
            let countNewRows = parentRows.length
            let parentRow = parentRows[index];
            // -------------------------------------------------------------------------------------------------------------

            if (checkListId_1.includes(checkBoxId)) { optionOne(data, parentRow, prefixIdValue); }
            else if (checkListId_2.includes(checkBoxId)) { optionTwo(data, parentRow, prefixIdValue) }

            else if (checkBoxId === 'wagering_contribution-group-check_id') {
                addWageringContribution(data, parentRow, prefixIdValue)
            }
            else if (checkBoxId === 'wagering_bonus_plus_deposit-group-check_id') {
                addWageringBonusPlusDeposit(data, parentRow, prefixIdValue)
            }
            else if (checkBoxId === 'restriction_rtp_game-group-check_id') {
                addRtpGameGroup(data, parentRow, prefixIdValue)
            }
            else { break; }

            if (countNewRows === datas.length) break;
            addRow.click();
        }
    }


    window.setAutoFillBonus2 = function (casinoKey) {
        const checkListId_3 = ['restriction_game-group-check_id', 'restriction_country-group-check_id'];
        // var dataChechBox = JSON.parse(localStorage.getItem("dataChechBox"));
        let dataChechBox = {};

        window.apiAutoFill('GET', casinoKey)
            .then(response => {
                if (response.data) { dataChechBox[casinoKey] = response.data };

                for (let key in dataChechBox[casinoKey]) {
                    if (checkListId_3.includes(key)) {
                        addDataBonusMtoM(dataChechBox[casinoKey][key]);
                    } else {
                        addDataBonus(dataChechBox[casinoKey][key], key);
                    }
                }
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
            
    }
}
