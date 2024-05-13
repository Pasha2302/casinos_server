{

    function hideBlocks(blocks) {
        blocks.forEach(function (block) {
            block.style.display = 'none';
        });
    }


    function setActiveButton(showAllButton, buttons, targetButton) {
        buttons.forEach(function (btn) {
            btn.classList.remove('active');
            showAllButton.classList.remove('active');
        });
        targetButton.classList.add('active');
    }


    function showSelectedFormBlock(showAllButton, buttons, fieldsetsBlocks, formsetBlocks, target, button) {
        // Скрыть все блоки форм
        hideBlocks(fieldsetsBlocks);
        // Скрыть все блоки formset
        hideBlocks(formsetBlocks);
        // Показать выбранный блок форм
        if (document.getElementById(target)) {
            let targetBlock = document.getElementById(target);
            let parentTargetBlock = targetBlock.parentNode;
            let targetChildren = parentTargetBlock.children;

            if (parentTargetBlock.classList.contains('module') && parentTargetBlock.classList.contains('aligned')) {
                // console.log('Дочерние блоки:', targetChildren);
                parentTargetBlock.style.display = 'block';
                for (let child of targetChildren) {
                    child.style.display = 'none';
                };
                targetBlock.style.display = 'block';
            } else {
                targetBlock.style.display = 'block';
            }
            // Установить активную кнопку
            setActiveButton(showAllButton, buttons, button);
        }
    }


    function performPageVerification(button) {
        let checkPageElm = document.getElementById('view_id_casino');
        console.log("Проверка страницы: ", checkPageElm);

        if (checkPageElm) {
            var buttonData = { buttonClass: button.getAttribute('class'), dataTarget: button.getAttribute('data-target') };
            saveButtonDataToLocalStorage(buttonData); // Сохраняем данные о нажатой кнопке в localStorage
            checkPageElm.click();
        };
    }


    function navigationLogic() {
        const fieldsetElement = document.querySelector('fieldset');
        if (fieldsetElement) {
            if (!fieldsetElement.hasAttribute('id')) {
                fieldsetElement.setAttribute('id', 'affiliate-set');
            }
        }

        const buttons = document.querySelectorAll('.nav-button-affiliates, .nav-button-bonus, .nav-button-loyalty');
        const showAllButton = document.querySelector('.nav-button-casino');
        const fieldsetsBlocks = document.querySelectorAll('.module.aligned ');
        const formsetBlocks = document.querySelectorAll('.js-inline-admin-formset.inline-group');

        formsetBlocks.forEach((block) => {
            // console.log(`\nID Formset Blocks: ${block.getAttribute('id')}`);
            if (block.getAttribute('id') === 'loyalty_program-group') {
                block.style.display = 'none';
            }
        });

        buttons.forEach(function (button) {
            button.addEventListener('click', function () {
                let target = button.getAttribute('data-target');
                console.log("Target:", target);

                if (performPageVerification(button)) return;
                showSelectedFormBlock(showAllButton, buttons, fieldsetsBlocks, formsetBlocks, target, button);

            });
        });

        showAllButton.addEventListener('click', function () {
            if (performPageVerification(showAllButton)) return;
            // Показать все блоки форм
            fieldsetsBlocks.forEach(function (fieldset) {
                let targetChildren = fieldset.children;
                fieldset.style.display = 'block';
                for (let child of targetChildren) {
                    // Показать все елементы (кроме .field-theme)
                    if (!child.classList.contains('field-theme')) {
                        child.style.display = 'block';
                    } else {
                        child.style.display = 'none';
                    }
                };
            });
            // Показать все блоки formset (кроме #loyalty_program-group)
            formsetBlocks.forEach(function (formsetBlock) {
                if (formsetBlock.getAttribute('id') !== 'loyalty_program-group') {
                    formsetBlock.style.display = 'block';
                } else {
                    formsetBlock.style.display = 'none';
                }
            });
            // Установить активную кнопку
            setActiveButton(showAllButton, buttons, showAllButton);
        });
    };


    // Функция для сохранения данных о нажатой кнопке в localStorage
    function saveButtonDataToLocalStorage(buttonData) {
        localStorage.setItem('buttonData', JSON.stringify(buttonData));
    }


    // Функция для получения данных о нажатой кнопке из localStorage
    function getButtonDataFromLocalStorage() {
        let buttonData = localStorage.getItem('buttonData');
        return buttonData ? JSON.parse(buttonData) : null;
    }

    // Функция для удаления данных о нажатой кнопке из localStorage
    function removeButtonDataFromLocalStorage() {
        localStorage.removeItem('buttonData');
    }


    function clickSaveButton(btn) {
        btn.click();
    }

    // Функция для ожидания появления элемента с определенным id
    function waitForElementToLoad(btn, elementId, callback) {
        let checkExist = setInterval(function () {
            let element = document.getElementById(elementId);
            if (element) {
                clearInterval(checkExist); // Остановить проверку, если элемент найден
                callback(btn); // Вызвать функцию обратного вызова
            }
        }, 100); // Проверять наличие элемента каждые 100 миллисекунд
    }

    document.addEventListener('DOMContentLoaded', function () {
        // console.log('Страница загружена ...')
        let buttonDataStorage = getButtonDataFromLocalStorage(); // Получаем данные о нажатой кнопке из localStorage

        navigationLogic();

        if (buttonDataStorage) {
            // console.log('Данные о нажатой кнопке:', buttonDataStorage);
            const buttonStorageClass = document.querySelector(`.${buttonDataStorage.buttonClass}`);
            const dataTargetId = buttonDataStorage.dataTarget
            // console.log('Button Local Storage Class:', buttonStorageClass);
            waitForElementToLoad(buttonStorageClass, dataTargetId, clickSaveButton);
            removeButtonDataFromLocalStorage(); // После использования можно удалить данные из localStorage
        } else {
            // console.log('Нет данных о нажатой кнопке в localStorage.');
        }
    });

}