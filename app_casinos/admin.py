# import json

from django import forms
# from django.contrib.admin.widgets import FilteredSelectMultiple
# from django.core.exceptions import ValidationError
# from django.http import HttpResponseRedirect
# from django.shortcuts import redirect
# from django.utils.html import format_html
from django.forms import widgets
from django.utils.html import format_html_join

# from django.utils.text import slugify

# from django.db import transaction
# from django.http import JsonResponse
# from django.urls import path
# from django.views.decorators.csrf import csrf_exempt

from app_casinos.inline_models_admin import *
from app_casinos.models import AffiliatesProgram


@admin.register(AffiliatesProgram)
class AffiliatesProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('name', )


@admin.register(CasinoImage)
class CasinoImageAdmin(admin.ModelAdmin):
    list_display = ('casino', 'image', )
    list_display_links = ('casino', )


@admin.register(AccountData)
class AccountDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'log')
    list_display_links = ('id', 'log')

@admin.register(SisterCasino)
class SisterCasinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(ClassicCurrency)
class ClassicCurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol')
    list_display_links = ('id', 'name')

@admin.register(CryptoCurrency)
class CryptoCurrenciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'symbol', 'name')
    list_display_links = ('id', 'symbol')
    search_fields = ('symbol',)


# class ModelDataValidationForm(forms.ModelForm):
#     def clean(self):
#         cleaned_data = super().clean()
#         instance = getattr(self, 'instance', None)

        # if instance:
        #     name, name2 = cleaned_data.get('name'), cleaned_data.get('name2')
        #     print(f"\nPostForm: {name=}, {name2=}")
        #     if name2: return cleaned_data
        #     # Проверяем, существует ли запись с таким слагом
        #     if name:
        #         slug = slugify(name)
        #         if Country.objects.filter(slug=slug).exists():
        #             raise forms.ValidationError({'name': "Record with this name already exists"})

        # return cleaned_data

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    # form = ModelDataValidationForm
    readonly_fields = ('slug',)
    list_display = ('id', 'name', 'name2', 'name3')
    list_display_links = ('name', 'name2', 'name3')
    search_fields = ('name',)


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
    search_fields = ('name',)

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
from django_select2.forms import Select2Widget, ModelSelect2Widget


class FilterAffiliateProgramAdminForm(forms.ModelForm):
    class Meta:
        model = Casino
        fields = ['affiliate_program']

    affiliate_program = forms.ModelChoiceField(
        queryset=AffiliatesProgram.objects.all(),
        widget=Select2Widget(),
    )



@admin.register(Casino)
class CasinoAdmin(admin.ModelAdmin):
    form = FilterAffiliateProgramAdminForm
    class Media:
        # js = ('app_casinos/js/admin/admin3.js',)
        # css = {
        #     'all': ('app_casinos/css/admin/admin.css',),
        # }

        js = (
            'https://code.jquery.com/jquery-3.6.4.min.js',  # Подключение jQuery
            'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/js/select2.min.js',  # Подключение Select2
            'app_casinos/js/admin/admin3.js',
        )
        css = {
            'all': (
                'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/css/select2.min.css',
                # Подключение стилей Select2
                'app_casinos/css/admin/admin.css',
            ),
        }

    # Поле только для чтения
    readonly_fields = (
        'slug', 'owner', 'established',
        'games', 'game_providers',
        'payment_methods',
    )

    list_display = ('display_images', 'name', 'url')
    list_display_links = ('display_images', 'name')

    inlines = [
        CasinoImageInline, BonusesInline, WithdrawalLimitInline, SisterCasinoInline,
        MinWageringInline, MinDepInline, AccountDataInline,  # GameInline
    ]

    fieldsets = (

        ('AFFILIATES', {
            'fields': (
                'affiliate_program', 'link_affiliate_program', 'link_affiliate',
            )
        }),

        ('BASIC INFORMATION', {
            'fields': ('name', 'link_loyalty', 'url', 'link_casino_guru', 'link_tc',
                       'link_bonus_tc', 'link_bonuses', 'owner', 'established',
                       'live_chat_competence', 'special_notes',
                       ),
        }),

        ('LANGUAGES', {
            'fields': (
                'language_website', 'language_live_chat',
            )
        }),

        ('RESTRICTED COUNTRIES', {
            'fields': (
                'blocked_countries',
            )
        }),

        ('CASINO LICENSE', {
            'fields': (
                'licenses',
            )
        }),

        ('OTHER INFO', {
            'fields': (
                'using_vpn', 'sportsbook', 'bonus_hunt_active_bonus', 'tournaments'
            )
        }),

        ('PAYMENTS', {
            'fields': ('classic_currency', 'crypto_currencies', 'payment_methods',)
        }),

        ('GAMES INFO', {
            'fields': ('game_types', 'game_providers', 'games') # 'games',
        }),

        ('RESPONSIBLE GAMBLING TOOLS', {
            'fields': ('wager_limit', 'loss_limit', 'session_limit', 'self_exclusion',
                       'cool_off', 'reality_check', 'self_assessment', 'withdrawal_lock',
                       ),
        }),
    )


    # list_filter = ('',)
    autocomplete_fields = ('games',)
    filter_horizontal = (
        "game_types", #"game_providers",# "games",
        "classic_currency", "crypto_currencies", #"payment_methods",
        "licenses", "blocked_countries", "language_website", "language_live_chat"
    )

    search_fields = ('name',)

    def display_images(self, obj):
        # Возвращает HTML-код для отображения изображений в списке объектов
        return format_html('<img src="{}" width="50" height="50" />',
                           obj.images.first().image.url) if obj.images.exists() else None


    # def save_model(self, request, obj, form, change):
    #     try:
    #         account_data = obj.withdrawal_limit
    #     except Exception as err:
    #         print(err)
    #         # super().save_model(request, obj, form, change)
    #     else:
    #         print('\nunlimited: ', obj.withdrawal_limit.unlimited)


    # def save_model(self, request, obj, form, change):
    #     print(f"{change=}")
    #     change = False
    #     try:
    #         account_data = obj.withdrawal_limit
    #     except Exception as err:
    #         self.message_user(request, "Please fill in all fields in Withdrawal limit.", level='ERROR')
    #         # raise forms.ValidationError("Record with this name already exists")
    #         print(f"{request.path=}")
    #         return HttpResponseRedirect(request.path)
    #
    #     super().save_model(request, obj, form, change)


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