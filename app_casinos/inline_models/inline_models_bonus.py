from django.contrib import admin

from app_casinos.models.bonus import (
    BonusAmount, BonusValue, BonusMinDep, BonusExpiration,
    PromotionPeriod, Sticky, BonusMaxWin, TurnoverBonus, FreeSpinAmount,
    OneSpin, BonusSlot, Wager, Wagering, WageringContribution,
    BonusRestrictionGame, BonusRestrictionCountry,
    BonusRestrictionRtpGame, BonusMaxBet, BonusMaxBetAutomatic,
    BonusBuyFeature, BonusSpecialNote, WageringBonusPlusDeposit, DayOfWeek
)
from app_casinos.forms import PromotionPeriodForm, BonusRestrictionGameInlineForm
from django.forms.models import BaseInlineFormSet

from app_casinos.models.casino import Game


class DayOfWeekInline(admin.TabularInline):
    model = DayOfWeek
    # extra = 1
    can_delete = True
    fields = ('days', 'selected_source',)
    autocomplete_fields = ('days', )


class BonusSpecialNoteInline(admin.TabularInline):
    model = BonusSpecialNote
    extra = 1
    can_delete = True
    fields = ('description',)

class BonusBuyFeatureInline(admin.TabularInline):
    model = BonusBuyFeature
    extra = 1
    can_delete = True
    fields = ('choice', 'selected_source',)

class BonusMaxBetAutomaticInline(admin.TabularInline):
    model = BonusMaxBetAutomatic
    extra = 1
    can_delete = True
    fields = ('automatic', 'selected_source',)

class BonusMaxBetInline(admin.TabularInline):
    model = BonusMaxBet
    extra = 1
    can_delete = True
    fields = ('value', 'symbol', 'selected_source',)
    autocomplete_fields = ('symbol',)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        try:
            max_bet = obj.max_bet
            if len(max_bet.all()) > 0: formset.extra = 0
        except Exception as err_extra: print(f"[file -> inline_models_admin.py] err_extra: {err_extra}")
        return formset

class BonusRestrictionRtpGameInline(admin.TabularInline):
    model = BonusRestrictionRtpGame
    extra = 1
    can_delete = True
    fields = ('value', 'selected_source')


class BonusRestrictionGameInline(admin.TabularInline):
    # formset = BonusRestrictionGameInlineFormSet
    model = BonusRestrictionGame
    form = BonusRestrictionGameInlineForm
    can_delete = True
    fields = ('game', 'selected_source')
    filter_horizontal = ('game', )
    # autocomplete_fields = ('game', )
    # raw_id_fields = ("game", )
    # prefetch_related = ('game',)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        # Получаем queryset всех выбранных игр для данного бонуса
        # print(f"\n\nRequest GET: {request.GET}\n Request POST: {request.POST}")
        print(f"ARGS:{request.POST=} /// {request.GET=} || {obj=} || {kwargs=}")
        print(f"\n\n<get_formset> Object (obj): {obj}")
        print("base_fields['game'].queryset:", formset.form.base_fields['game'].queryset)
        print("kwargs:", kwargs)
        if request.POST:
            data_game = request.POST.getlist('restriction_game-0-game')
            print("data_game:", data_game, type(data_game))
            formset.form.base_fields['game'].queryset = Game.objects.filter(id__in=data_game)
            # selected_games = BonusRestrictionGame.objects.filter(bonus=obj).values_list('game', flat=True)
            # formset.form.base_fields['game'].queryset = Game.objects.filter(id__in=selected_games)
        return formset


class BonusRestrictionCountryInline(admin.TabularInline):
    model = BonusRestrictionCountry
    extra = 1
    can_delete = True
    fields = ('country', 'selected_source')
    filter_horizontal = ('country', )


class WageringContributionInline(admin.TabularInline):
    model = WageringContribution
    extra = 1
    can_delete = True
    fields = ('contribution_description', 'value', 'selected_source',)
    autocomplete_fields = ('contribution_description',)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        try:
            wagering_contribution = obj.wagering_contribution
            if len(wagering_contribution.all()) > 0: formset.extra = 0
        except Exception as err_extra: print(f"[file -> inline_models_admin.py] err_extra: {err_extra}")
        return formset

class WageringInline(admin.StackedInline):
    model = Wagering
    extra = 1
    can_delete = True
    fields = ('tbwr', 'tbwe', 'selected_source')

class WageringBonusPlusDepositInline(admin.TabularInline):
    model = WageringBonusPlusDeposit
    extra = 1
    can_delete = True
    fields = ('bonus_plus_deposit', 'bonus_only', 'selected_source')

class WagerInline(admin.TabularInline):
    model = Wager
    extra = 1
    can_delete = True
    fields = ('value', 'selected_source')

class BonusSlotInline(admin.TabularInline):
    model = BonusSlot
    extra = 1
    can_delete = True
    fields = ('game', 'selected_source')
    autocomplete_fields = ('game',)
    # filter_horizontal = ('game', )

class OneSpinInline(admin.TabularInline):
    model = OneSpin
    extra = 1
    can_delete = True
    fields = ('value', 'selected_source')

class FreeSpinAmountInline(admin.TabularInline):
    model = FreeSpinAmount
    extra = 1  # Количество пустых форм для добавления новых акций
    can_delete = True
    fields = ('value', 'selected_source')

class TurnoverBonusInline(admin.TabularInline):
    model = TurnoverBonus
    extra = 1  # Количество пустых форм для добавления новых акций
    can_delete = True
    fields = ('choice', 'selected_source')

class BonusMaxWinInline(admin.TabularInline):
    model = BonusMaxWin
    extra = 1
    can_delete = True
    fields = ('max_value', 'symbol', 'unlimited', 'selected_source',)
    autocomplete_fields = ('symbol',)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        try:
            bonus_max_win = obj.bonus_max_win
            # print(f"\nBonus Max Win: {obj.bonus_max_win=}")
            if len(bonus_max_win.all()) > 0: formset.extra = 0
        except Exception as err_extra: print(f"[file -> inline_models_admin.py] err_extra: {err_extra}")
        return formset

class StickyInline(admin.TabularInline):
    model = Sticky
    extra = 1  # Количество пустых форм для добавления новых акций
    can_delete = True
    fields = ('sticky_value', 'selected_source')

class PromotionPeriodInline(admin.TabularInline):
    model = PromotionPeriod
    form = PromotionPeriodForm
    extra = 1  # Количество пустых форм для добавления новых акций
    can_delete = True
    fields = ('start_date', 'end_date', 'selected_source')

class BonusExpirationInline(admin.TabularInline):
    model = BonusExpiration
    extra = 1
    can_delete = True
    fields = ('days', 'selected_source',)

class BonusMinDepInline(admin.TabularInline):
    model = BonusMinDep
    extra = 1
    # can_delete = True
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
    can_delete = True
    fields = ('value', 'selected_source',)

class BonusAmountInline(admin.TabularInline):
    model = BonusAmount
    extra = 1

    can_delete = True
    fields = ('value', 'symbol', 'unlimited', 'selected_source',)
    autocomplete_fields = ('symbol',)

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        try:
            bonus_amount = obj.bonus_amount
            if len(bonus_amount.all()) > 0: formset.extra = 0
        except Exception as err_extra: print(f"[file -> inline_models_admin.py] err_extra: {err_extra}")

        return formset
