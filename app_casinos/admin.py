import json

from django import forms
from django.db import transaction
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from app_casinos.inline_models_admin import *


@admin.register(AccountData)
class AccountDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'log')
    list_display_links = ('id', 'log')

@admin.register(ClassicCurrency)
class ClassicCurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol')
    list_display_links = ('id', 'name')

@admin.register(CryptoCurrency)
class CryptoCurrenciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'symbol', 'name')
    list_display_links = ('id', 'symbol')
    search_fields = ('symbol',)
#GH9nZiqEdzRQ6n4

@admin.register(Country)
class BlockedCountryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('id', 'name', )

@admin.register(GameType)
class GameTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('id', 'name', )

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('id', 'name', )

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ('id', 'name', )

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_display_links = ('name', )
    search_fields = ('name',)

# ----------------------------------------------------------------------

@admin.register(WithdrawalLimit)
class WithdrawalLimitAdmin(admin.ModelAdmin):
    list_display = ('id', 'daily', 'weekly', 'monthly')
    list_display_links = ('id', 'daily')
    search_fields = ('daily',)


@admin.register(Bonus)
class BonusesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    autocomplete_fields = ('casino',)

#
@admin.register(LicensingAuthority)
class LicensingAuthorityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'validator_url')
    list_display_links = ('id', 'name')

    # inlines = (LicensesInline,)
    exclude = ('slug', )

# ==================================================================================================================== #

class BlockedCountriesWidget(forms.TextInput):
    def value_from_datadict(self, data, files, name):
        value = data.get(name, '')
        return value.split(',')

class CustomCasinoAdminForm(forms.ModelForm):
    country_names = forms.CharField(widget=BlockedCountriesWidget, required=False, help_text='Enter country names separated by commas')

    class Meta:
        model = Casino
        fields = '__all__'


@admin.register(Casino)
class CasinoAdmin(admin.ModelAdmin):
    class Media:
        js = ('app_casinos/js/admin/admin2.js',)
        css = {
            'all': ('app_casinos/css/admin/admin.css',),
        }

    readonly_fields = ('slug', )            # Поле только для чтения
    list_display = ('id', 'name', 'url')
    list_display_links = ('id', 'name')

    fieldsets = (
        ('Basic Information', {
            'fields': ('slug', 'name', 'url', 'link_casino_guru', 'link_tc',
                       'link_bonus_tc', 'link_bonuses', 'owner', 'established',
                       'language_website', 'language_live_chat', 'blocked_countries', 'licenses',),
        }),

        ('Other Info', {
            'fields': (
                'using_vpn', 'sportsbook', 'bonus_hunt_active_bonus',
                'live_chat_competence', 'special_notes',
            )
        }),

        ('Payments', {
            'fields': ('classic_currency', 'crypto_currencies', 'payment_methods',)
        }),

        ('Games Info', {
            'fields': ('game_types', 'game_providers', 'games',)
        }),

        ('Responsible Gambling Tools', {
            'fields': ('wager_limit', 'loss_limit', 'session_limit', 'self_exclusion',
                       'cool_off', 'reality_check', 'self_assessment', 'withdrawal_lock',
                       'tournaments'),
        }),
    )

    filter_horizontal = (
        "game_types", "game_providers", "games",
        "classic_currency", "crypto_currencies", "payment_methods",
        "licenses", "blocked_countries", "language_website", "language_live_chat"
    )

    inlines = [
        BonusesInline, WithdrawalLimitInline, SisterCasinoInline,
        MinWageringInline, MinDepInline, AccountDataInline,
    ]
    search_fields = ('name',)

    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)
    #
    #     country_names = form.cleaned_data.get('country_names', '')
    #     country_names_list = [name.strip() for name in country_names.split(',') if name.strip()]
    #
    #     if country_names_list:
    #         countries = [Country.objects.get_or_create(name=name)[0] for name in country_names_list]
    #         obj.blocked_countries.set(countries)

    # change_form_template = 'admin/casino_change_form.html'
    #
    # @csrf_exempt
    # def import_countries_view(self, request, object_id=None, form_url='', extra_context=None):
    #     print(f"\n{self=}")
    #     print(f"\n{object_id=}")
    #     if request.method == 'POST':
    #         print(request.POST)
    #         data_client = request.POST.get('data')
    #         if data_client:
    #             try:
    #                 datas = [d.strip() for d in json.loads(data_client)['countries']]
    #                 print(datas)
    #                 models_casino: Casino = self.model
    #                 print(f"\n\n{models_casino.blocked_countries}\n")
    #                 object_country = models_casino.blocked_countries.crea
    #                 object_country.name = 'sss'
    #                 models_casino.blocked_countries.add()
    #                 # Добавить данные в модель Country
    #
    #                 return JsonResponse({'message': 'Data imported successfully'})
    #             except json.JSONDecodeError as e:
    #                 return JsonResponse({'error': 'Invalid JSON format'})
    #
    #     return JsonResponse({'error': 'Invalid request'})
    #
    # # def get_urls(self):
    # #     urls = super().get_urls()
    # #     custom_urls = [
    # #         path('<path:object_id>/import-countries/', self.import_countries_view, name='import_countries'),
    # #     ]
    # #     return custom_urls + urls
    # def get_urls(self):
    #     urls = super().get_urls()
    #     custom_urls = [
    #         path(r"add/import-countries/", self.import_countries_view, name='import_countries'),
    #     ]
    #     return custom_urls + urls


    # def get_queryset(self, request):
    #     return super().get_queryset(request).prefetch_related('bonuses')
    #
    # class Media:
    #     css = {
    #         'all': ('app_casinos/css/admin/admin.css',),
    #     }
    #
    # exclude = ["licenses"]




# class CountryInline(admin.TabularInline):
#     model = Casino.blocked_countries.through  # Use the intermediary model
#
#
# class CustomCasinoAdminForm(forms.ModelForm):
#     country_names = forms.CharField(widget=forms.Textarea, required=False,
#                                     help_text='Enter country names separated by commas')
#
#     class Meta:
#         model = Casino
#         fields = '__all__'
#
# @admin.register(Casino)
# class CasinoAdmin(admin.ModelAdmin):
#     form = CustomCasinoAdminForm
#     inlines = [CountryInline]
#
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#
#         country_names = form.cleaned_data.get('country_names', '')
#         country_names_list = [name.strip() for name in country_names.split(',') if name.strip()]
#
#         if country_names_list:
#             countries = [Country.objects.get_or_create(name=name)[0] for name in country_names_list]
#             obj.blocked_countries.set(countries)