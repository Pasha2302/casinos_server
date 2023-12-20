(function ($) {
    $(document).ready(function () {
        const SelectBox = window.SelectBox
        SelectBox.filter = function (id, text) {
            const tokens = text.toLowerCase().split(',');
            for (const node of SelectBox.cache[id]) {
                if (tokens.lenght === 0) {
                    node.displayed = 1;
                    continue;
                }
                node.displayed = 0;
                const node_text = node.text.toLowerCase();
                for (const token of tokens) {
                    if (node_text.includes(token)) {
                        node.displayed = 1;
                        break;
                    }
                    // if (!node_text.includes(token)) {
                    //     node.displayed = 0;
                    //     break; // Once the first token isn't found we're done
                    // }
                }
            }
            SelectBox.redisplay(id);
        }
    });
})(jQuery);
