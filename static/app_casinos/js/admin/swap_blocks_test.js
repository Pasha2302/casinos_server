function swapBlocks() {
    let inlineBlocks = $();
    // Добавляем каждый блок из списка ID к коллекции
    for (let dataObjBlock of dataBlocks) {
        for (let blockId of dataObjBlock.listIds) {
            inlineBlocks.add($(blockId));
        }
    }

    // Проверяем, что у нас есть хотя бы два блока, прежде чем менять их местами
    if (inlineBlocks.length >= 2) {
        // Получаем первый и второй блоки
        let firstBlock = inlineBlocks.eq(0);
        let secondBlock = inlineBlocks.eq(1);

        console.log("Before change:");
        console.log("First block:", firstBlock.text().replace(/\s+/g, ' ').trim());
        console.log("Second block:", secondBlock.text().replace(/\s+/g, ' ').trim());

        // Полностью меняем местами блоки в DOM
        secondBlock.insertBefore(firstBlock);

        console.log("\nAfter change:");
        console.log("First block:", firstBlock.text().replace(/\s+/g, ' ').trim());
        console.log("Second block:", secondBlock.text().replace(/\s+/g, ' ').trim());

    }
}
