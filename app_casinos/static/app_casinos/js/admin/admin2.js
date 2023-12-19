(function($) {
    $(document).ready(function() {
        var countryInput = $('#id_blocked_countries');
        var countryNamesInput = $('<textarea id="id_country_names" name="country_names" rows="3" style="width: 20%;" placeholder="Enter country names separated by commas"></textarea>');

        countryInput.after(countryNamesInput);

        countryNamesInput.on('input', function() {
            var countryNames = $(this).val().toLowerCase().split(',').map(function(item) {
                return item.trim();
            });

            // Перебираем доступные страны и прячем те, которые не соответствуют введенным значениям
            $('#id_blocked_countries_from option').each(function() {
                var countryOption = $(this);
                var countryName = countryOption.text().toLowerCase();
                var isVisible = countryNames.length === 0 || countryNames.includes(countryName);
                countryOption.prop('hidden', !isVisible);
            });

            // Если поле ввода пусто, показываем все страны
            if (countryNames.length === 0) {
                $('#id_blocked_countries_from option').prop('hidden', false);
            }
        });
    });
})(jQuery);


