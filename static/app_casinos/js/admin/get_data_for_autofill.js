'use strict';


{

    // function convertAttributesToObject(elementquerySelector) {
    //     let elm1 = document.querySelector(elementId);
    //     let attributes = Array.from(elm1.attributes);
    //     let attributesObj = attributes.reduce((acc, attr) => ({ ...acc, [attr.nodeName]: attr.nodeValue }), {});
    //     console.log(attributesObj);
    //     return attributesObj;
    // }

    function getDataOptionOne(checkBoxEvent, dataChechBox, _casinoKey) {
        const suffixIdRow = dataChechBox[_casinoKey][checkBoxEvent.id].suffixIdRow;
        const prefixIdValue = dataChechBox[_casinoKey][checkBoxEvent.id].prefixIdValue;

        const contentBlock = checkBoxEvent.closest('.module');
        const rows = contentBlock.querySelectorAll(`[class^="form-row"][class*="dynamic${suffixIdRow}"]`);

        for (let row of rows) {
            let valueElm = row.querySelector(`[id^="${prefixIdValue}"][id$="_value"]`);
            if (!valueElm) { valueElm = row.querySelector(`[id^="${prefixIdValue}"][id$="-value"]`); }

            let sumbolElm = $(row.querySelector(`[id^="${prefixIdValue}"][id$="-symbol"]`));
            let sourceValue = row.querySelector(`[id^="${prefixIdValue}"][id$="-selected_source"]`).value;
            let unlimitedElm = row.querySelector(`[id^="${prefixIdValue}"][id$="-unlimited"]`);

            let expirationDaysElm = row.querySelector(`[id^="${prefixIdValue}"][id$="-days"]`);

            let dataRow = {
                value: valueElm ? valueElm.value : null,
                symbol: {
                    id: Boolean(sumbolElm.val()) ? sumbolElm.val() : null,
                    text: Boolean(sumbolElm.text().trim()) ? sumbolElm.text().trim() : null,
                    selected: Boolean(sumbolElm.val()) ? true : null
                },
                source: sourceValue,
                unlimited: unlimitedElm ? unlimitedElm.checked : null,
                expirationDays: expirationDaysElm ? expirationDaysElm.value : null,
            };
            dataChechBox[_casinoKey][checkBoxEvent.id].data.push(dataRow)
        }
    }


    function getDataRtpGameGroup(checkBoxEvent, dataChechBox, _casinoKey) {
        const contentBlock = checkBoxEvent.closest('.module');
        const rows = contentBlock.querySelectorAll('[class^="form-row"][class*="dynamic-restriction_rtp_game"]');
        for (let row of rows) {
            let sourceValue = row.querySelector('[id^="id_restriction_rtp_game-"][id$="-selected_source"]').value;
            let rtpValue = row.querySelector('[id^="id_restriction_rtp_game-"][id$="-value"]').value;

            dataChechBox[_casinoKey][checkBoxEvent.id].data.push({ rtpValue: rtpValue, source: sourceValue })
        }
    }


    function getDataWageringBonusPlusDepositGroup(checkBoxEvent, dataChechBox, _casinoKey) {
        const contentBlock = checkBoxEvent.closest('.module');
        const rows = contentBlock.querySelectorAll('[class^="form-row"][class*="dynamic-wagering_bonus_plus_deposit"]');
        for (let row of rows) {
            let sourceValue = row.querySelector('[id^="id_wagering_bonus_plus_deposit-"][id$="-selected_source"]').value;
            let value1 = row.querySelector('#id_wagering_bonus_plus_deposit-0-bonus_plus_deposit').value;
            let value2 = row.querySelector('#id_wagering_bonus_plus_deposit-0-bonus_only').value;

            dataChechBox[_casinoKey][checkBoxEvent.id].data.push({ value1: value1, value2: value2, source: sourceValue })
        }
    }


    function getDataWageringContributionGroup(checkBoxEvent, dataChechBox, _casinoKey) {
        const contentBlock = checkBoxEvent.closest('.module');
        const rows = contentBlock.querySelectorAll('[class^="form-row"][class*="dynamic-wagering_contribution"]');
        for (let row of rows) {
            let sourceValue = row.querySelector('[id^="id_wagering_contribution-"][id$="-selected_source"]').value;
            let value = row.querySelector('[id^="id_wagering_contribution-"][id$="-value"]').value;
            let selectElm = $(row.querySelector('[id^="id_wagering_contribution"][id$="-contribution_description"]'));

            let dataRow = {
                value: value,
                selectElm: { id: selectElm.val(), text: selectElm.text().trim(), selected: true },
                source: sourceValue,
            };
            dataChechBox[_casinoKey][checkBoxEvent.id].data.push(dataRow)
        }
    }


    // ===============================================================================================================

    function getDataStickyGroup(checkBoxEvent, dataChechBox, _casinoKey) {
        const contentBlock = checkBoxEvent.closest('.module');
        const rows = contentBlock.querySelectorAll('[class^="form-row"][class*="dynamic-sticky"]');
        for (let row of rows) {
            let sourceValue = row.querySelector('[id^="id_sticky-"][id$="-selected_source"]').value;
            let statusValue = row.querySelector('[id^="id_sticky-"][id$="-sticky_value"]').checked;

            dataChechBox[_casinoKey][checkBoxEvent.id].data.push(
                { statusValue: statusValue, source: sourceValue, elmSuffixId: '-sticky_value' }
            )
        }
    }


    function getDataTurnoverBonusGroup(checkBoxEvent, dataChechBox, _casinoKey) {
        const contentBlock = checkBoxEvent.closest('.module');
        const rows = contentBlock.querySelectorAll('[class^="form-row"][class*="dynamic-turnover_bonus"]');
        for (let row of rows) {
            let sourceValue = row.querySelector('[id^="id_turnover_bonus-"][id$="-selected_source"]').value;
            let statusValue = row.querySelector('[id^="id_turnover_bonus-"][id$="-choice"]').checked;

            dataChechBox[_casinoKey][checkBoxEvent.id].data.push(
                { statusValue: statusValue, source: sourceValue, elmSuffixId: '-choice' }
            )
        }
    }


    function getDataMaxBetAutomaticGroup(checkBoxEvent, dataChechBox, _casinoKey) {
        const contentBlock = checkBoxEvent.closest('.module');
        const row = contentBlock.querySelector('#max_bet_automatic-0');
        let sourceValue = row.querySelector('#id_max_bet_automatic-0-selected_source').value;
        let statusValue = row.querySelector('#id_max_bet_automatic-0-automatic').checked;

        dataChechBox[_casinoKey][checkBoxEvent.id].data.push(
            { statusValue: statusValue, source: sourceValue, elmSuffixId: '-automatic' }
        )
    }


    function getDataBuyFeatureGroup(checkBoxEvent, dataChechBox, _casinoKey) {
        const contentBlock = checkBoxEvent.closest('.module');
        const row = contentBlock.querySelector('#buy_feature-0');
        let sourceValue = row.querySelector('#id_buy_feature-0-selected_source').value;
        let statusValue = row.querySelector('#id_buy_feature-0-choice').checked;

        dataChechBox[_casinoKey][checkBoxEvent.id].data.push(
            { statusValue: statusValue, source: sourceValue, elmSuffixId: '-choice' }
        )
    }

    //  <<<< ======================================================================================================= >>>>

    function getDataRestrictionGameGroup(checkBoxEvent, dataChechBox, _casinoKey) {
        const selectDataTo = window.SelectBox.cache['id_restriction_game-0-game_to'];
        const sourceValue = document.querySelector('#id_restriction_game-0-selected_source').value;

        dataChechBox[_casinoKey][checkBoxEvent.id].data = {
            selectDataTo: selectDataTo, sourceValue: sourceValue,
            idSelectBlockTo: 'id_restriction_game-0-game_to',
            idSourceValue: 'id_restriction_game-0-selected_source',
        }
    }

    function getDataRestrictionCountryGroup(checkBoxEvent, dataChechBox, _casinoKey) {
        const selectDataTo = window.SelectBox.cache['id_restriction_country-0-country_to'];
        const sourceValue = document.querySelector('#id_restriction_country-0-selected_source').value;

        dataChechBox[_casinoKey][checkBoxEvent.id].data = {
            selectDataTo: selectDataTo, sourceValue: sourceValue,
            idSelectBlockTo: 'id_restriction_country-0-country_to',
            idSourceValue: 'id_restriction_country-0-selected_source',
        }
    }

    //  <<<< ======================================================================================================= >>>>
    window.getDataAutoFillBonus = function (checkBoxEvent, dataChechBox, casinoKey) {
        const checkListId_1 = [
            'bonus_min_dep-group-check_id', 'bonus_max_win-group-check_id',
            'bonus_expiration-group-check_id', 'max_bet-group-check_id',
        ]
        dataChechBox[casinoKey][checkBoxEvent.id].data = [];
        // localStorage.setItem('dataChechBox', JSON.stringify(dataChechBox));

        if (checkBoxEvent.checked) {

            if (checkListId_1.includes(checkBoxEvent.id)) {
                getDataOptionOne(checkBoxEvent, dataChechBox, casinoKey);
            }
            else if (checkBoxEvent.id === 'restriction_rtp_game-group-check_id') {
                getDataRtpGameGroup(checkBoxEvent, dataChechBox, casinoKey);
            }
            else if (checkBoxEvent.id === 'wagering_bonus_plus_deposit-group-check_id') {
                getDataWageringBonusPlusDepositGroup(checkBoxEvent, dataChechBox, casinoKey);
            }
            else if (checkBoxEvent.id === 'wagering_contribution-group-check_id') {
                getDataWageringContributionGroup(checkBoxEvent, dataChechBox, casinoKey);
            }

            else if (checkBoxEvent.id === 'buy_feature-group-check_id') {
                getDataBuyFeatureGroup(checkBoxEvent, dataChechBox, casinoKey);
            }
            else if (checkBoxEvent.id === 'turnover_bonus-group-check_id') {
                getDataTurnoverBonusGroup(checkBoxEvent, dataChechBox, casinoKey);
            }
            else if (checkBoxEvent.id === 'max_bet_automatic-group-check_id') {
                getDataMaxBetAutomaticGroup(checkBoxEvent, dataChechBox, casinoKey);
            }
            else if (checkBoxEvent.id === 'sticky-group-check_id') {
                getDataStickyGroup(checkBoxEvent, dataChechBox, casinoKey);
            }

            else if (checkBoxEvent.id === 'restriction_game-group-check_id') {
                getDataRestrictionGameGroup(checkBoxEvent, dataChechBox, casinoKey);
            }
            else if (checkBoxEvent.id === 'restriction_country-group-check_id') {
                getDataRestrictionCountryGroup(checkBoxEvent, dataChechBox, casinoKey);
            }

        }

        window.apiAutoFill('PUT', casinoKey, dataChechBox[casinoKey]);
    }

}

// document.addEventListener('DOMContentLoaded', function () {
//     window.getDataAutoFillBonus();

// });
