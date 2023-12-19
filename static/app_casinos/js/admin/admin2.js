(function($) {
    $(document).ready(function() {
        var countryInput = $('#id_blocked_countries');
        countryInput.after('<textarea id="id_country_names" name="country_names" rows="3" style="width: 100%;" placeholder="Enter country names separated by commas"></textarea>');

        countryInput.hide();

        $('#id_country_names').on('input', function() {
            var countryNames = $(this).val();
            countryInput.val(countryNames.split(',').map(function(item) {
                return item.trim();
            }));
        });
    });
})(django.jQuery);
