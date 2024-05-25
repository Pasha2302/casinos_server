import re
from django.contrib import admin
from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html

from app_casinos.forms import (CountryDataValidationForm, BonusAdminForm, RichTextEditorWidget,)
from app_casinos.inline_models.inline_models_bonus import (
    BonusAmountInline, BonusValueInline, BonusMinDepInline,
    BonusExpirationInline, PromotionPeriodInline, StickyInline,
    BonusMaxWinInline, TurnoverBonusInline,
    FreeSpinAmountInline, OneSpinInline, BonusSlotInline,
    WagerInline, WageringInline, WageringContributionInline,
    BonusRestrictionGameInline, BonusRestrictionCountryInline,
    BonusRestrictionRtpGameInline, BonusMaxBetInline,
    BonusMaxBetAutomaticInline, BonusBuyFeatureInline,
    BonusSpecialNoteInline, WageringBonusPlusDepositInline,
    DayOfWeekInline, SlotsWageringContributionInline,
)

from app_casinos.inline_models.inline_models_casino import (
    CasinoImageInline, MinWageringInline, MinDepInline,
    BonusInline, WithdrawalLimitInline, AccountDataInline, SocialBonusInline,
)
from app_casinos.inline_models.inline_models_loyalty_program import (
    PointAccumulationInline, CashbackInline, LevelUpBonusInline, LevelLoyaltyInline, LoyaltyProgramInline,
    WithdrawalsInline, SpecialPrizeInline, GiftsInline, LoyaltyBonusInline
)

from app_casinos.models.bonus import (
    Bonus, BonusType, WageringContributionValue,
    WageringContribution, BonusSlot, BonusRestrictionGame, BonusSubtype, Day, BonusMinDep, DataAutoFillBonus,
    SlotsWageringContribution
)
from app_casinos.models.casino import (
    Casino, WithdrawalLimit, SisterCasino,
    MinDep, Country, Language, AccountData, GameType,
    Provider, Game, ClassicCurrency, CryptoCurrency, LicensingAuthority,
    CasinoImage, BaseCurrency, AffiliatesProgram, PaymentMethod, Affiliate,
    CasinoTheme
)
from app_casinos.models.loyalty_program import LoyaltyProgram, LevelLoyalty, CashbackPeriod, CashbackType
from django.utils.safestring import mark_safe

from app_casinos.models.state_program import StateProgram


@admin.register(StateProgram)
class StateProgramAdmin(admin.ModelAdmin):
    pass


@admin.register(DataAutoFillBonus)
class DataAutoFillBonusAdmin(admin.ModelAdmin):
    pass


@admin.register(CashbackPeriod)
class CashbackPeriodAdmin(admin.ModelAdmin):
    pass


@admin.register(CashbackType)
class CashbackTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(LevelLoyalty)
class LevelLoyaltyAdmin(admin.ModelAdmin):
    change_form_template = 'admin/loyalty_prog_change_form.html'
    list_display = ('id', 'display_casino_name', 'level',)
    list_display_links = ('id', 'display_casino_name',)
    search_fields = ('program__casino__name', 'level')

    inlines = (
        PointAccumulationInline, CashbackInline, LevelUpBonusInline, WithdrawalsInline, SpecialPrizeInline,
        GiftsInline, LoyaltyBonusInline,
    )

    @admin.display(description="Casino Name")
    def display_casino_name(self, obj: LevelLoyalty):
        if obj.program and obj.program.casino: return obj.program.casino.name


@admin.register(LoyaltyProgram)
class LoyaltyProgramAdmin(admin.ModelAdmin):
    change_form_template = 'admin/loyalty_prog_change_form.html'
    # form = ''

    list_display = ('id', 'display_casino_name', 'link', )
    list_display_links = ('id', 'display_casino_name', )
    search_fields = ('casino__name', )
    autocomplete_fields = ('casino', )

    inlines = (
        LevelLoyaltyInline,
    )
    fieldsets = (
        ('Loyalty Program', {
            'fields': ('casino', 'link', 'loyalty_understandable', 'vip_manager', 'loyalty_rank')
        }),
    )

    @admin.display(description="Casino Name")
    def display_casino_name(self, obj: LoyaltyProgram):
        if obj.casino: return obj.casino.name



# ==================================================================================================================== #
@admin.register(SlotsWageringContribution)
class SlotsWageringContributionAdmin(admin.ModelAdmin):
    list_display = ('id', 'bonus', 'value')
    list_display_links = ('bonus', )
    search_fields = ('bonus', 'slot__name')
    autocomplete_fields = ('slot', )


@admin.register(BonusRestrictionGame)
class BonusRestrictionGameAdmin(admin.ModelAdmin):
    list_display = ('id', 'bonus', 'selected_source')
    list_display_links = ('bonus', )
    search_fields = ('bonus', 'game__name')
    autocomplete_fields = ('game', )


@admin.register(BonusSlot)
class BonusSlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'bonus', 'selected_source')
    list_display_links = ('bonus', )
    search_fields = ('bonus', 'game__name')
    autocomplete_fields = ('game', )

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

@admin.register(BonusSubtype)
class BonusSubtypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    search_fields = ('name',)

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    fields =  ("day", )
    search_fields = ('day',)


@admin.register(BonusMinDep)
class BonusMinDepAdmin(admin.ModelAdmin):
    list_display = ('id', 'bonus', 'min_value', 'symbol', 'selected_source')
    fields =  ('bonus', 'min_value', 'symbol', 'selected_source')
    list_display_links = ('bonus', 'min_value', 'symbol', 'selected_source')


@admin.register(Bonus)
class BonusAdmin(admin.ModelAdmin):
    change_form_template = 'admin/bonus_change_form.html'
    form = BonusAdminForm

    list_display = ('id', 'name', 'display_casino_name', 'bonus_type', 'link')
    list_display_links = ('id', 'name')
    search_fields = ('casino__name', 'bonus_type__name')
    autocomplete_fields = ('casino', 'bonus_type',)
    # readonly_fields = ('calculation_bonus_deposit', 'calculation_bonus_only')
    readonly_fields = ('get_url_casino', 'get_url_bonus_tc')

    inlines = (
        BonusAmountInline, BonusValueInline, BonusMinDepInline, BonusExpirationInline,
        PromotionPeriodInline, StickyInline, BonusMaxWinInline, TurnoverBonusInline, DayOfWeekInline,

        FreeSpinAmountInline, OneSpinInline, BonusSlotInline, WagerInline,
        WageringInline, WageringBonusPlusDepositInline, WageringContributionInline, SlotsWageringContributionInline,

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
            'fields': (
                'casino', 'get_url_casino', 'get_url_bonus_tc',
                'link', 'bonus_type', 'bonus_subtype', 'name', 'bonus_rank',
            )
        }),

        # ('DAILY AVAILABILITY', {'fields': ('days',)}),
        ('BONUS RESTRICTION PROVIDERS', {'fields': ('game_providers',)}),

        ('TOTAL BONUS AMOUNT', {
            'fields': ('bonus_plus_deposit', 'bonus_only', 'bonus_plus_freespins_value')
        }),
        ('AMOUNT OF BETS FOR WAGERING', {
            'fields': ('calculation_bonus_deposit', 'calculation_bonus_only',)
        }),

    )
    filter_horizontal = ("bonus_subtype", "game_providers", )
    # Это обеспечивает быстрый и грязный способ переопределения некоторых опций Field для использования в админке:
    formfield_overrides = {
        models.TextField: {"widget": RichTextEditorWidget},
    }

    def get_url_bonus_tc(self, obj: Bonus):
        link_bonus_tc = obj.casino.link_bonus_tc
        return mark_safe(f'<a href="{link_bonus_tc}" target="_blank">{link_bonus_tc}</a>')
    get_url_bonus_tc.short_description = 'URL Bonus T&C'

    def get_url_casino(self, obj: Bonus):
        casino_link = obj.casino.url
        return mark_safe(f'<a href="{casino_link}" target="_blank">{casino_link}</a>')
    get_url_casino.short_description = 'URL Casino'

    @admin.display(description="Casino Name")
    def display_casino_name(self, obj: Bonus):
        if obj.casino: return  obj.casino.name
# ==================================================================================================================== #
# ==================================================================================================================== #

@admin.register(MinDep)
class MinDepAdmin(admin.ModelAdmin):
    list_display = ('id', 'min_value', 'unlimited', 'selected_source')
    list_display_links = ('min_value', )
    fields = ('min_value', 'symbol', 'unlimited', 'selected_source', 'casino')
    autocomplete_fields = ('symbol',)


@admin.register(AffiliatesProgram)
class AffiliatesProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('name', )
    search_fields = ('name',)

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name', )


@admin.register(CasinoImage)
class CasinoImageAdmin(admin.ModelAdmin):
    list_display = ('casino', 'image', )
    list_display_links = ('casino', )


@admin.register(AccountData)
class AccountDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'user_name')
    list_display_links = ('id', 'login', 'user_name')

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
    search_fields = ('name', 'symbol')

@admin.register(CryptoCurrency)
class CryptoCurrenciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'symbol', 'name')
    list_display_links = ('id', 'symbol')
    search_fields = ('symbol',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    form = CountryDataValidationForm
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

@admin.register(Affiliate)
class AffiliateAdmin(admin.ModelAdmin):
    search_fields = ('affiliate_program',)

@admin.register(CasinoTheme)
class CasinoThemeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
# ==================================================================================================================== #


@admin.register(Casino)
class CasinoAdmin(admin.ModelAdmin):
    save_on_top = True
    change_form_template = 'admin/casino_change_form.html'
    # Поле только для чтения
    readonly_fields = (
        'slug', 'owner', 'established',
        'games', 'game_providers',
        'payment_methods', 'sisters_casinos',
    )

    list_display = ('name', 'url', 'shortened_notes', 'is_pars_data', )  # 'display_images',
    list_display_links = ('name', 'url', )  # 'display_images',

    inlines = (
        LoyaltyProgramInline, CasinoImageInline, BonusInline, WithdrawalLimitInline,
        MinWageringInline, MinDepInline, AccountDataInline, SocialBonusInline,
    )

    class Media:
        js = ('app_casinos/js/admin/casino_parser.js',)
        css = { 'all': ('app_casinos/css/admin/casino_parser.css',) }

    autocomplete_fields = ('affiliate', 'theme')
    fieldsets = (

        ('AFFILIATES', {
            'fields': ('affiliate',)
        }),

        ('BASIC INFORMATION', {
            'fields': ('name', 'casino_rank', 'theme', 'link_loyalty', 'url', 'link_casino_guru', 'link_tc',
                       'link_bonus_tc', 'link_bonuses',
                        'sportsbook', 'tournaments',
                       'owner', 'established', 'sisters_casinos',
                       ),
        }),

        ('OTHER INFO', {
            'fields': (
                'live_chat_competence', 'special_notes',
            )
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

        ('ADDITIONAL OPTIONS', {
            'fields': (
                'vpn_usage', 'bonus_hunt_with_active_bonus',
            )
        }),

        ('PAYMENTS', {
            'fields': ('classic_currency', 'crypto_currencies', 'payment_methods',)
        }),

        ('GAMES INFO', {
            'fields': ('game_types', 'game_providers', 'games')
        }),

        ('RESPONSIBLE GAMBLING TOOLS', {
            'fields': ('deposit_limit', 'wager_limit', 'loss_limit', 'session_limit',
                       'self_exclusion', 'gamstop_self_exclusion', 'cool_off', 'reality_check',
                       'self_assessment', 'withdrawal_lock',
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

    def shortened_notes(self, obj):
        max_length = 255
        if obj.special_notes:
            if len(obj.special_notes) > max_length: return f'{obj.special_notes[:max_length]}...'
            else: return obj.special_notes
        else: return ''

    shortened_notes.short_description = 'Special Notes'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        comp = re.compile(r'\bbonuses-\d+-name\b')
        # obj = self.get_object(request, object_id)
        if request.POST:
            keys_bonuses_name = [k for k in request.POST if re.search(comp, k)]
            bonuses_names = [request.POST.get(k) for k in keys_bonuses_name if request.POST.get(k)]

            if len(bonuses_names) != len(set(bonuses_names)):
                message = "DUPLICATE BONUS NAMES ARE NOT ALLOWED !"
                self.message_user(request, message, level='ERROR')
                return HttpResponseRedirect(reverse('admin:app_casinos_casino_change', args=(object_id,)))

        return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)

