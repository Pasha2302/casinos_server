const $ = django.jQuery;


const inlineBlockGroups = [
    {
        titleBlock: "GENERAL INFO",
        listIds: [
            "#bonus_amount-group", "#bonus_value-group",
            "#bonus_min_dep-group", "#bonus_expiration-group",
            "#promotion_period-group", "#sticky-group", "#bonus_max_win-group", "#turnover_bonus-group"
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
            "#wagering-group", "#wagering_contribution-group",
        ]
    },
    {
        titleBlock: "RESTRICTION",
        listIds: [
            "#restriction_game-group", "#restriction_country-group", "#restriction_rtp_game-group",
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

function combiningBlocks() {
    
    // Добавляем каждый блок из списка ID к коллекции
    for (let dataObjBlock of inlineBlockGroups) {
        let inlineBlocks = $();
        for (let blockId of dataObjBlock.listIds) {
            inlineBlocks = inlineBlocks.add($(blockId));
        }
        console.log("\nInline Blocks:", inlineBlocks)
        // Создаем новый контейнер div с заголовком-кнопкой:
        let containerDiv = $('<div class="container-group">');
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

        // Добавляем обработчик события для сворачивания и разворачивания блока
        titleButton.click(function() {
            inlineBlocks.slideToggle();
        });
    }
}


$(document).ready(function () {
    console.log('File [moving_blocks_to_change_form.js] connected ...');

    combiningBlocks();
});
