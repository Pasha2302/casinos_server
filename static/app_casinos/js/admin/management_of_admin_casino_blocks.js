{

    function add_block_descriptions() {
        const text_casino_withdrawal_limit = "Daily, weekly, and monthly withdrawal limits in EUR. If, for example, there are no weekly limits, please leave the field empty.";
        const text_casino_min_wagering = "The minimum wagering or rollover requirement indicates the number of times a deposit must be played through (typically 1x-3x) before being eligible for withdrawal from the casino";
        const text_casino_other_social_bonuses = "If the casino has social bonuses in Twitter, Telgram, etc., please check the box";

        const blockWithdrawalLimit = $('#withdrawal_limit-group');
        const descriptionWithdrawalLimit = $(`<br><div class="help">${text_casino_withdrawal_limit}</div>`);
        blockWithdrawalLimit.find('h2').eq(0).after($(descriptionWithdrawalLimit));


        const blockMinWagering = $('#min_wagering-group');
        const descriptionMinWagering = $(`<br><div class="help">${text_casino_min_wagering}</div>`);
        blockMinWagering.find('h2').eq(0).after($(descriptionMinWagering));

        const blockSocialBonuses = $('#social_bonuses-group');
        const descriptionSocialBonuses = $(`<br><div class="help">${text_casino_other_social_bonuses}</div>`);

        const label = $('<label class="vCheckboxLabel">Social Bonus</label>');
        blockSocialBonuses.find('.field-choice > input[id^="id_social_bonuses-"]').first().after(label);
        label.after($(descriptionSocialBonuses));
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


    function movingBlocks() {
        $('.field-sisters_casinos').first().after($('#casino_license-set').first());
        $('#casino_license-set').first().after($('#games_info-set').first());

        $('.form-row.field-theme').first().hide();

        $('.form-row.field-link_bonuses').first().after($('#bonuses-group').first());
        $('#bonuses-group').first().after($('#social_bonuses-group').first());

        $('.form-row.field-tournaments').first().after($('#images-group').first());
        $('#payments-set').first().after($('#account_data-group').first());

        $('#min_dep-group').first().after($('#additional_options-set').first());
        $('#additional_options-set').first().after($('#other_info-set').first());

        // $('#social_bonuses-group').find('h2').remove();
    }


    function setBlockStyleToReadOnly() {
        // Получаем все элементы с классом .readonly
        var readonlyElements = document.querySelectorAll('.readonly');
        // Перебираем массив найденных элементов
        readonlyElements.forEach(function (readonlyElement) {
            // Находим родительский блок для текущего элемента
            var parentFieldset = readonlyElement.closest('.form-row');
            // Проверяем, найден ли родительский блок
            if (parentFieldset) {
                // Если найден, то устанавливаем стили для него
                parentFieldset.style.backgroundColor = '#ffffcc';
            }
        });
    }


    function main() {
        setIdBlocksFieldSet();
        movingBlocks();
        add_block_descriptions();
        setBlockStyleToReadOnly();
    }


    $(document).ready(function () {
        // setTimeout(main, 2000);
        main();
    });

}
// "<ul class="errorlist"><li>Ensure that there are no more than 1 digit before the decimal point.</li></ul>"