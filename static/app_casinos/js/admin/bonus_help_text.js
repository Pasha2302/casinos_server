// text_bonus_value_percentage = "Bonus value in percentage. So, for example if it says '200% up to 200 EUR' then bonus value is 200%";
// text_bonus_availability = "For example, if the bonus is only available on Tuesday, please select 'Tuesday' from the dropdown menu";
// text_bonus_expiration = "This means that the player has X days to wager his bonus. Otherwise it will be canceled, etc."
// text_bonus_game_restriction = "Pick slots that you can't play with active bonus"
// text_bonus_rtp_restriction = "Some slots are not allowed for bonus wagering due to high RTP"
// text_bonus_country_restriction = "Pick countries that can't receive this bonus"
// text_bonus_free_spins_amount = "Number of free spins that you can get by activating this bonus"
// text_bonus_free_spins_one_spin_value = "The value of one free spin. Usually around 0.1 EUR"
// text_bonus_free_spins_slot_availability = "Slots where you can use free spins"
// text_bonus_free_spins_wager = "Wagering amount for free spins"
// text_bonus_turnover = "If the bonus is of the turnover type, please tick the box"
// text_bonus_wagering_contribution = "Usually slots are 100% and everything else (roulette, blackjack, etc) is 0% or 5%"
// text_bonus_max_bet = "Maximum bet allowed by T&C"
// text_bonus_max_bet_automatic = "In some casinos max bet is restricted automatically meaning that you can't place a bigger bet than allowed if you have an active bonus. However, in some casinos this is not automatically restricted and customer can easily make a mistake by placing a higher bet and thus canceling his bonus and winnings from it."
// text_bonus_other_bonus_buy = "For example - Can I buy 'Buy Feature' in Money Train 3 with an active welcome bonus? My winnings won't be canceled?"
// text_bonus_other_special_notes = "Something worth mentioning. For example - Bonus is available only via Skrill deposit"

const helpTextData = [
    {
        helpText: "Bonus value in percentage. So, for example if it says '200% up to 200 EUR' then bonus value is 200%",
        blockId: '#bonus_value-group'
    },
    {
        helpText: "For example, if the bonus is only available on Tuesday, please select 'Tuesday' from the dropdown menu",
        blockId: '#day_of_week-group'
    },
    {
        helpText: "This means that the player has X days to wager his bonus. Otherwise it will be canceled, etc.",
        blockId: '#bonus_expiration-group'
    },
    {
        helpText: "Pick slots that you can't play with active bonus",
        blockId: '#restriction_game-group'
    },
    {
        helpText: "Some slots are not allowed for bonus wagering due to high RTP",
        blockId: '#restriction_rtp_game-group'
    },
    {
        helpText: "Pick countries that can't receive this bonus",
        blockId: '#restriction_country-group'
    },
    {
        helpText: "Number of free spins that you can get by activating this bonus",
        blockId: '#free_spin_amount-group'
    },
    {
        helpText: "The value of one free spin. Usually around 0.1 EUR",
        blockId: '#one_spin-group'
    },
    {
        helpText: "Slots where you can use free spins",
        blockId: '#bonus_slot-group'
    },
    {
        helpText: "Wagering amount for free spins",
        blockId: '#wager-group'
    },
    {
        helpText: "If the bonus is of the turnover type, please tick the box",
        blockId: '#turnover_bonus-group'
    },
    {
        helpText: "Usually slots are 100% and everything else (roulette, blackjack, etc) is 0% or 5%",
        blockId: '#wagering_contribution-group'
    },
    {
        helpText: "Maximum bet allowed by T&C",
        blockId: '#max_bet-group'
    },
    {
        helpText: "In some casinos max bet is restricted automatically meaning that you can't place a bigger bet than allowed if you have an active bonus. However, in some casinos this is not automatically restricted and customer can easily make a mistake by placing a higher bet and thus canceling his bonus and winnings from it.",
        blockId: '#max_bet_automatic-group'
    },
    {
        helpText: "For example - Can I buy 'Buy Feature' in Money Train 3 with an active welcome bonus? My winnings won't be canceled?",
        blockId: '#buy_feature-group'
    },
    {
        helpText: "Something worth mentioning. For example - Bonus is available only via Skrill deposit",
        blockId: '#special_note-group'
    },
];


function setData(data) {
    const description = $(`<br><div class="help">${data.helpText}</div>`);
    const block = $(data.blockId);

    block.find('h2').eq(0).after($(description));
    // blockValuePercentage.find('h2').eq(0).after($(descriptionValuePercentage));
};


function setHelpText() {
    // console.log('\n\nHELP TEXT START ...\n');
    for (let i = 0; i < helpTextData.length; i++) {
        setData(helpTextData[i]);
    };
};


$(document).ready(function () {
    // setTimeout(setHelpText, 2000);
    setHelpText();
});
