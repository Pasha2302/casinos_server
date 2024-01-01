from django.contrib import admin
from django.db import models

from django.contrib.admin import SimpleListFilter
from django.urls import reverse
from django.utils.html import format_html

from app_casinos.forms import (ModelDataValidationForm, BonusAdminForm, RichTextEditorWidget)
from app_casinos.inline_models.inline_models_bonus import (BonusAmountInline, BonusValueInline, BonusMinDepInline,
                                                           BonusExpirationInline, PromotionPeriodInline, StickyInline,
                                                           BonusMaxWinInline, TurnoverBonusInline,
                                                           FreeSpinAmountInline, OneSpinInline, BonusSlotInline,
                                                           WagerInline, WageringInline, WageringContributionInline,
                                                           BonusRestrictionGameInline, BonusRestrictionCountryInline,
                                                           BonusRestrictionRtpGameInline, BonusMaxBetInline,
                                                           BonusMaxBetAutomaticInline, BonusBuyFeatureInline,
                                                           BonusSpecialNoteInline, )

from app_casinos.inline_models.inline_models_casino import CasinoImageInline, MinWageringInline, MinDepInline, BonusesInline, \
    WithdrawalLimitInline, AccountDataInline, SisterCasinoInline

from app_casinos.all_models.bonus_model import Bonus, BonusType, BonusSubtype, WageringContributionValue, \
    WageringContribution
from app_casinos.all_models.models import (Casino, WithdrawalLimit, SisterCasino,
                                MinDep, Country, Language, AccountData, GameType,
                                Provider, Game, ClassicCurrency, CryptoCurrency, LicensingAuthority,
                                CasinoImage, BaseCurrency, AffiliatesProgram, PaymentMethod)


@admin.register(BonusSubtype)
class BonusTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    search_fields = ('name',)

@admin.register(BonusType)
class BonusTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    search_fields = ('name',)

@admin.register(WageringContributionValue)
class WageringContributionValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', )
    list_display_links = ('description', )
    search_fields = ('description',)

@admin.register(WageringContribution)
class WageringContributionAdmin(admin.ModelAdmin):
    list_display = ('id', 'bonus', 'contribution_description', 'value', 'selected_source')
    list_display_links = ('bonus', )
    search_fields = ('contribution_description',)

@admin.register(Bonus)
class BonusesAdmin(admin.ModelAdmin):
    change_form_template = 'admin/bonus_change_form.html'
    form = BonusAdminForm

    list_display = ('id', 'name', 'link', 'display_casino_name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    autocomplete_fields = ('casino', 'bonus_type')

    inlines = (
        BonusAmountInline, BonusValueInline, BonusMinDepInline, BonusExpirationInline,
        PromotionPeriodInline,StickyInline, BonusMaxWinInline, TurnoverBonusInline,

        FreeSpinAmountInline, OneSpinInline, BonusSlotInline, WagerInline,
        WageringInline, WageringContributionInline,
        BonusRestrictionGameInline, BonusRestrictionCountryInline, BonusRestrictionRtpGameInline,
        BonusMaxBetInline, BonusMaxBetAutomaticInline,
        BonusBuyFeatureInline, BonusSpecialNoteInline,
    )
    fieldsets = (
        ('BONUS', {
            # Строка необязательного дополнительного текста,
            # который будет отображаться в верхней части каждого набора полей под заголовком набора полей:
            # "description": "<p>Какой-то текст!</p>",
            # [classes] Список или кортеж, содержащий дополнительные классы CSS для применения к набору полей:
            "classes": ("extrapretty", ), # "wide", "collapse", "extrapretty"
            'fields': ('casino', 'bonus_type', 'bonus_subtypes', 'link', 'name', 'social_bonuses')
        }),

        ('TOTAL BONUS AMOUNT', {
            'fields': ('bonus_plus_deposit', 'bonus_only', 'bonus_plus_freespins_value')
        }),

    )
    filter_horizontal = ("bonus_subtypes", )
    # Это обеспечивает быстрый и грязный способ переопределения некоторых опций Field для использования в админке:
    formfield_overrides = {
        models.TextField: {"widget": RichTextEditorWidget},
    }

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        print(f"\n\nField Sets:\n{fieldsets}")
        return fieldsets
    def get_inlines(self, request, obj):
        inlines = super().get_inlines(request, obj)
        print(f"\n\nInlines:\n{inlines}")
        print(f"\n\nOne InLine Object [dict]:\n{inlines[0].__dict__}")
        return inlines


    @admin.display(description="Casino Name")
    def display_casino_name(self, obj: Bonus):
        if obj.casino: return  obj.casino.name
# ==================================================================================================================== #
# ==================================================================================================================== #

@admin.register(MinDep)
class MinDepAdmin(admin.ModelAdmin):
    list_display = ('id', 'min_value', 'selected_source')
    list_display_links = ('min_value', )
    fields = ('min_value', 'symbol', 'selected_source', 'casino')
    autocomplete_fields = ('symbol',)


@admin.register(AffiliatesProgram)
class AffiliatesProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    search_fields = ('name',)

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name', )


@admin.register(CasinoImage)
class CasinoImageAdmin(admin.ModelAdmin):
    list_display = ('casino', 'image', )
    list_display_links = ('casino', )


@admin.register(AccountData)
class AccountDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'login')
    list_display_links = ('id', 'login')

@admin.register(SisterCasino)
class SisterCasinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

# ==================================================================================================================== #
@admin.register(BaseCurrency)
class BaseCurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol')
    list_display_links = ('id', 'name')
    search_fields = ('symbol',)

@admin.register(ClassicCurrency)
class ClassicCurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol')
    list_display_links = ('id', 'name')

@admin.register(CryptoCurrency)
class CryptoCurrenciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'symbol', 'name')
    list_display_links = ('id', 'symbol')
    search_fields = ('symbol',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    form = ModelDataValidationForm
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

@admin.register(LicensingAuthority)
class LicensingAuthorityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'validator_url')
    list_display_links = ('id', 'name')

    # inlines = (LicensesInline,)
    exclude = ('slug', )

# ==================================================================================================================== #

class SoldOutFilter(SimpleListFilter):
    title = "Name Casino"
    parameter_name = "name"

    def lookups(self, request, model_admin):
        return [
            ("yes", "Yes"),
            ("no", "No"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "yes":
            return queryset.filter(name=0)
        else:
            return queryset.exclude(name=0)

@admin.register(Casino)
class CasinoAdmin(admin.ModelAdmin):
    save_on_top = True
    change_form_template = 'admin/casino_change_form.html'
    # form = FilterAffiliateProgramAdminForm
    # class Media:
    #     js = (
    #         'https://code.jquery.com/jquery-3.6.4.min.js',  # Подключение jQuery
    #         'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/js/select2.min.js',  # Подключение Select2
    #         # 'app_casinos/js/admin/admin3.js',
    #     )
    #     css = {
    #         'all': (
    #             # Подключение стилей Select2
    #             'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/css/select2.min.css',
    #             # 'app_casinos/css/admin/admin.css',
    #         ),
    #     }

    # Поле только для чтения
    readonly_fields = (
        'slug', 'owner', 'established',
        'games', 'game_providers',
        'payment_methods',
    )

    list_display = ('display_images', 'name', 'url', 'test_text')  # 'my_func' 'display_affiliate_program',
    list_display_links = ('display_images', 'name')

    inlines = (
        CasinoImageInline, BonusesInline, WithdrawalLimitInline, SisterCasinoInline,
        MinWageringInline, MinDepInline, AccountDataInline,  # GameInline
    )
    autocomplete_fields = ('affiliate_program',)
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
            'fields': ('game_types', 'game_providers', 'games')
        }),

        ('RESPONSIBLE GAMBLING TOOLS', {
            'fields': ('wager_limit', 'loss_limit', 'session_limit', 'self_exclusion',
                       'cool_off', 'reality_check', 'self_assessment', 'withdrawal_lock',
                       ),
        }),
    )


    # list_filter = ('',)
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


    def my_func(self, obj, *args, **kwargs):
        # print(f"\nMy Func: {obj=}")
        # print(f"{args=}\n{kwargs=}\n")
        return False

    def test_text(self, *args):
        print(f"\n\nTest Text args: {args}")
        return format_html("<string>{}</string>", 'Какой-то текст!')

    def display_affiliate_program(self, obj: Casino):
        print(f"\n[display_affiliate_program] obj type: {type(obj)}")
        print(f"\n[display_affiliate_program] self dict:")
        for data_self in self.__dict__:
            print(f"{data_self}")
            print('--' * 60)
        print(f"\nForm Fields Overrides:\n{self.formfield_overrides}")
        print(f"\nForm Fields Overrides Keys:\n{self.formfield_overrides.keys()}")
        print("Form Fields Overrides Values:")
        for key_formfield_overrides in self.formfield_overrides:
            print('..' * 60)
            print(self.formfield_overrides[key_formfield_overrides])

        if obj.affiliate_program:
            link = reverse("admin:app_casinos_affiliatesprogram_change", args=[obj.affiliate_program.id])
            return format_html('<a href="{}">{}</a>', link, obj.affiliate_program)

    display_affiliate_program.short_description = "Affiliate Program"
    # my_func.short_description = "Verified"
    # my_func.boolean = True

    # def get_fieldsets(self, request, obj=None):
    #     fieldsets = super().get_fieldsets(request, obj=obj)
    #     # Добавьте новый блок в форме
    #     fieldsets += (
    #         ('Дополнительные данные', {
    #             'fields': ('slug',)
    #         }),
    #     )
    #     return fieldsets

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
