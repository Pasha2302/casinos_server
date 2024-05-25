function calculateValue(value1, value2, resultValue, maxBet) {
  if (!maxBet) {
    return;
  }

  value1 = value1 !== "" ? value1 : 0;
  value2 = value2 !== "" ? value2 : 0;
  maxBet = maxBet !== "" ? maxBet : 0;

  // console.log("\nvalue1:", value1);
  // console.log("value2:", value2);
  // console.log("Calculate Value (resultBlock):", resultValue);
  resultValue.value = (
    (Number(value1) * Number(value2)) / Number(maxBet)
  ).toFixed(2);
}

const defineActiveField = () => {
  console.log("\n\nУстановка событий динамического вычисления ...");
  let maxBetValue = document.getElementById("id_max_bet-0-value");

  const bonusPlusDeposit_1 = document.getElementById("id_bonus_plus_deposit");
  const bonusPlusDeposit_2 = document.getElementById(
    "id_wagering_bonus_plus_deposit-0-bonus_plus_deposit"
  );
  const bonusPlusDepositForm = document.getElementsByClassName(
    "form-row field-calculation_bonus_deposit"
  )[0];
  let bonusPlusDepositValue = document.getElementById(
    "id_calculation_bonus_deposit"
  );

  const bonusOnly_1 = document.getElementById("id_bonus_only");
  const bonusOnly_2 = document.getElementById(
    "id_wagering_bonus_plus_deposit-0-bonus_only"
  );
  const bonusOnlyForm = document.getElementsByClassName(
    "form-row field-calculation_bonus_only"
  )[0];
  let bonusOnlyValue = document.getElementById("id_calculation_bonus_only");

  // Устанавливаем атрибут readonly для полей ввода
  bonusPlusDepositValue.setAttribute("readonly", true);
  bonusOnlyValue.setAttribute("readonly", true);

  bonusPlusDeposit_1.addEventListener("input", handleInput);
  bonusOnly_1.addEventListener("input", handleInput);
  bonusOnly_2.addEventListener("input", handleInput);
  bonusPlusDeposit_2.addEventListener("input", handleInput);
  maxBetValue.addEventListener("input", handleInput);

  handleInput();

  function handleInput() {
    if (bonusPlusDeposit_1.value !== "" || bonusPlusDeposit_2.value !== "") {
      bonusOnly_1.style.display = "none";
      bonusOnly_2.style.display = "none";
      bonusOnlyForm.style.display = "none";
      calculateValue(
        bonusPlusDeposit_1.value,
        bonusPlusDeposit_2.value,
        bonusPlusDepositValue,
        maxBetValue.value
      );
    } else if (bonusOnly_1.value !== "" || bonusOnly_2.value !== "") {
      bonusPlusDeposit_1.style.display = "none";
      bonusPlusDeposit_2.style.display = "none";
      bonusPlusDepositForm.style.display = "none";
      calculateValue(
        bonusOnly_1.value,
        bonusOnly_2.value,
        bonusOnlyValue,
        maxBetValue.value
      );
    } else {
      bonusPlusDeposit_1.style.display = "block";
      bonusPlusDeposit_2.style.display = "block";
      bonusPlusDepositForm.style.display = "block";

      bonusOnly_1.style.display = "block";
      bonusOnly_2.style.display = "block";
      bonusOnlyForm.style.display = "block";

      bonusPlusDepositValue.value = "";
      bonusOnlyValue.value = "";
    }
  }
};

const setcalculations = () => {
  const checkExist = setInterval(function () {
    let elements = document.querySelectorAll("#id_calculation_bonus_deposit");
    if (elements.length) {
      clearInterval(checkExist); // Остановить проверку, если элемент найден.
      defineActiveField();
      return;
    }
    console.log("Элемент <id: slots_wagering-group> не найден!");
  }, 600);
};

document.addEventListener("DOMContentLoaded", function () {
  // console.log('File [calculations_for_bonus.js] connected ...');
  defineActiveField();
});
