from django.contrib import admin

from app_casinos.all_models.bonus_model import (BonusAmount, BonusValue, BonusMinDep, BonusExpiration,
                                                PromotionPeriod, Sticky, BonusMaxWin, TurnoverBonus, FreeSpinAmount,
                                                OneSpin, BonusSlot, Wager, Wagering, WageringContribution,
                                                BonusRestrictionGame, BonusRestrictionCountry,
                                                BonusRestrictionRtpGame, BonusMaxBet, BonusMaxBetAutomatic,
                                                BonusBuyFeature, BonusSpecialNote, )
from app_casinos.forms import PromotionPeriodForm


class BonusSpecialNoteInline(admin.TabularInline):
    model = BonusSpecialNote
    extra = 1
    can_delete = False
    fields = ('description',)

class BonusBuyFeatureInline(admin.TabularInline):
    model = BonusBuyFeature
    extra = 1
    can_delete = False
    fields = ('choice', 'selected_source',)

class BonusMaxBetAutomaticInline(admin.TabularInline):
    model = BonusMaxBetAutomatic
    extra = 1
    can_delete = False
    fields = ('automatic', 'selected_source',)

class BonusMaxBetInline(admin.TabularInline):
    model = BonusMaxBet
    extra = 1
    can_delete = False
    fields = ('value', 'symbol', 'selected_source',)
    autocomplete_fields = ('symbol',)

class BonusRestrictionRtpGameInline(admin.TabularInline):
    model = BonusRestrictionRtpGame
    extra = 1
    can_delete = False
    fields = ('value', 'selected_source')

class BonusRestrictionGameInline(admin.TabularInline):
    model = BonusRestrictionGame
    extra = 1
    can_delete = False
    fields = ('game', 'selected_source')
    filter_horizontal = ('game', )

class BonusRestrictionCountryInline(admin.TabularInline):
    model = BonusRestrictionCountry
    extra = 1
    can_delete = False
    fields = ('country', 'selected_source')
    filter_horizontal = ('country', )

class WageringContributionInline(admin.TabularInline):
    model = WageringContribution
    extra = 1
    can_delete = False
    fields = ('contribution_description', 'value', 'selected_source',)
    autocomplete_fields = ('contribution_description',)

class WageringInline(admin.StackedInline):
    model = Wagering
    extra = 1
    can_delete = False
    fields = ('tbwr', 'tbwe', 'selected_source')

class WagerInline(admin.TabularInline):
    model = Wager
    extra = 1
    can_delete = False
    fields = ('value', 'selected_source')

class BonusSlotInline(admin.TabularInline):
    model = BonusSlot
    extra = 1
    can_delete = False
    fields = ('slots', 'selected_source')
    filter_horizontal = ('slots', )

class OneSpinInline(admin.TabularInline):
    model = OneSpin
    extra = 1
    can_delete = False
    fields = ('value', 'selected_source')

class FreeSpinAmountInline(admin.TabularInline):
    model = FreeSpinAmount
    extra = 1  # Количество пустых форм для добавления новых акций
    can_delete = False
    fields = ('value', 'selected_source')

class TurnoverBonusInline(admin.TabularInline):
    model = TurnoverBonus
    extra = 1  # Количество пустых форм для добавления новых акций
    can_delete = False
    fields = ('turnover_value', 'selected_source')

class BonusMaxWinInline(admin.TabularInline):
    model = BonusMaxWin
    extra = 1
    can_delete = False
    fields = ('max_value', 'symbol', 'selected_source',)
    autocomplete_fields = ('symbol',)

class StickyInline(admin.TabularInline):
    model = Sticky
    extra = 1  # Количество пустых форм для добавления новых акций
    can_delete = False
    fields = ('sticky_value', 'selected_source')

class PromotionPeriodInline(admin.TabularInline):
    model = PromotionPeriod
    form = PromotionPeriodForm
    extra = 1  # Количество пустых форм для добавления новых акций
    can_delete = False
    fields = ('start_date', 'end_date', 'selected_source')

class BonusExpirationInline(admin.TabularInline):
    model = BonusExpiration
    extra = 1
    can_delete = False
    fields = ('days', 'selected_source',)

class BonusMinDepInline(admin.TabularInline):
    model = BonusMinDep
    extra = 1
    can_delete = False
    fields = ('min_value', 'symbol', 'selected_source',)
    autocomplete_fields = ('symbol',)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        try:
            obj_min_dip = obj.bonus_min_dep
            if len(obj_min_dip.all()) > 0: formset.extra = 0
        except Exception as err_extra: print(f"[file -> inline_models_admin.py] err_extra: {err_extra}")

        return formset

class BonusValueInline(admin.TabularInline):
    model = BonusValue
    extra = 1
    can_delete = False
    fields = ('value', 'selected_source',)

class BonusAmountInline(admin.TabularInline):
    model = BonusAmount
    extra = 1

    can_delete = False
    fields = ('value', 'symbol', 'selected_source',)
    autocomplete_fields = ('symbol',)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        try:
            obj_min_dip = obj.bonus_amount
            if len(obj_min_dip.all()) > 0: formset.extra = 0
        except Exception as err_extra: print(f"[file -> inline_models_admin.py] err_extra: {err_extra}")

        return formset
