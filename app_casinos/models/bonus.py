from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import QuerySet

from django.utils.text import slugify
from app_casinos.models.casino import BaseCurrency, CHOICES_SOURCE, Game, Country, Provider
from app_casinos.models.casino import Casino
from app_casinos.description_model_fields import *


class DataAutoFillBonus(models.Model):
    name = models.CharField(max_length=255, unique=True)
    data = models.JSONField()

    class Meta:
        ordering = ["id"]
        verbose_name = "Bonus Data AutoFill"
        verbose_name_plural = "Bonus Data AutoFill"

    def __str__(self):
        return f"{str(self.name).title()} / data auto-fill"


class BonusType(models.Model):
    name = models.CharField(verbose_name="Name Bonus Type", max_length=255, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        verbose_name = "Bonus Type"
        verbose_name_plural = "Types of Bonuses"


class BonusAmount(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='bonus_amount', to_field='slug')
    value = models.IntegerField(verbose_name="(CAP) value", help_text=text_bonus_amount, null=True, blank=True,)
    symbol = models.ForeignKey(
        BaseCurrency, related_name='bonus_amount_symbol', on_delete=models.SET_NULL, null=True, blank=True,)
    unlimited = models.BooleanField(default=False)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    class Meta:
        ordering = ["id"]
        verbose_name = "Bonus Amount"
        verbose_name_plural = "Bonus Amount"

    def clean(self):
        check_selected_source = self.selected_source if self.selected_source != 'undefined' else False
        if not self.unlimited and not all((self.value, check_selected_source, self.symbol)):
            raise ValidationError('Values: (CAP) VALUE, SYMBOL and SELECTED SOURCE are required, or set to UNLIMITED.')
        if not check_selected_source:
            raise ValidationError('Be sure to specify the data source (Selected source)')


class BonusValue(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='bonus_value', to_field='slug', unique=True)
    value = models.IntegerField(null=True, verbose_name="Value %", help_text=text_bonus_value_percentage)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )
    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')


class BonusMinDep(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='bonus_min_dep', to_field='slug')
    min_value = models.IntegerField(null=True, verbose_name="Bonus min dep value", help_text=text_bonus_min_deposit)
    symbol = models.ForeignKey(BaseCurrency, related_name='bonus_min_dep', on_delete=models.SET_NULL, null=True,)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    class Meta:
        ordering = ["id"]
        verbose_name = "Bonus Min Deposit"
        verbose_name_plural = "Bonus Min Deposit"

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')


class BonusExpiration(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='bonus_expiration', to_field='slug', unique=True)
    days = models.IntegerField(
        null=True,
        verbose_name="Amount of Days",
        help_text=text_bonus_expiration,
        validators=[MinValueValidator(1), MaxValueValidator(30)],
        choices=[(i, i) for i in range(1, 31)]  # выбор от 1 до 30
    )
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')


class PromotionPeriod(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='promotion_period', to_field='slug', unique=True)
    start_date = models.DateField(
        verbose_name="Start Date", help_text=text_bonus_promotion_period, null=True, blank=True,)
    end_date = models.DateField(verbose_name="End Date", null=True, blank=True,)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def __str__(self):
        return f"Promotion period from {self.start_date} to {self.end_date}"

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')


class Sticky(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='sticky', to_field='slug', unique=True)
    sticky_value = models.BooleanField(default=False)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )
    class Meta:
        verbose_name = "Sticky Or Not Sticky"
        verbose_name_plural = "Sticky Or Not Sticky"
    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')


class BonusMaxWin(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='bonus_max_win', to_field='slug')
    max_value = models.IntegerField(
        null=True, blank=True, verbose_name="Bonus Max Win value", help_text=text_bonus_bonus_max_win)
    symbol = models.ForeignKey(
        BaseCurrency, related_name='bonus_max_win', on_delete=models.SET_NULL, null=True, blank=True)
    unlimited = models.BooleanField(default=False)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    class Meta:
        ordering = ["id"]
        verbose_name = "Bonus Max Win"
        verbose_name_plural = "Bonus Max Win"

    def clean(self):
        check_selected_source = self.selected_source if self.selected_source != 'undefined' else False
        if not self.unlimited and not all((self.max_value, check_selected_source, self.symbol)):
            raise ValidationError('Values: MAX VALUE, SYMBOL and SELECTED SOURCE are required, or set to UNLIMITED.')
        if not check_selected_source:
            raise ValidationError('Be sure to specify the data source (Selected source)')


class TurnoverBonus(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='turnover_bonus', to_field='slug', unique=True)
    choice = models.BooleanField(default=False, verbose_name="turnover bonus choice",) # help_text=text_bonus_turnover
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')


# ----------------------------------------- FREE SPIN ----------------------------------------------------------------- #
class FreeSpinAmount(models.Model):
    bonus = models.OneToOneField(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='free_spin_amount', to_field='slug')
    value = models.IntegerField(
        null=True, verbose_name="Free Spins value", blank=True,) # help_text=text_bonus_free_spins_amount
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )


class OneSpin(models.Model):
    bonus = models.OneToOneField(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='one_spin', to_field='slug')
    value = models.FloatField(
        null=True, verbose_name="One Spin value", blank=True,) # help_text=text_bonus_free_spins_one_spin_value
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )


class Wager(models.Model):
    bonus = models.OneToOneField(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='wager', to_field='slug')
    value = models.IntegerField(
        null=True, verbose_name="Wager value", blank=True,) # help_text=text_bonus_free_spins_wager
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )


class BonusSlot(models.Model):
    bonus = models.OneToOneField(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='bonus_slot', to_field='slug')
    game = models.ManyToManyField(
        Game, related_name='bonus_game', verbose_name='Game Slot', blank=True,)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )


# ----------------------------------------- WAGERING ----------------------------------------------------------------- #
class Wagering(models.Model):
    bonus = models.OneToOneField(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='wagering', to_field='slug')
    tbwr = models.TextField(
        null=True, blank=True, verbose_name="Turnover bonus wagering requirement",
        help_text=text_bonus_wagering_turnover_requirement
    )
    tbwe = models.TextField(
        null=True, blank=True, verbose_name="Turnover bonus wagering example",
        help_text=text_bonus_wagering_turnover_example
    )
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')


class WageringBonusPlusDeposit(models.Model):
    bonus = models.OneToOneField(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='wagering_bonus_plus_deposit', to_field='slug')
    bonus_plus_deposit = models.IntegerField(
        null=True, blank=True, verbose_name="(Wagering) Bonus + Deposit", help_text=text_bonus_wagering_bonus_deposit
    )
    bonus_only = models.IntegerField(
        null=True, blank=True, verbose_name="(Wagering) Bonus Only", help_text=text_bonus_wagering_bonus_only
    )
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def __str__(self):
        return ''

    def clean(self):
        # print(f"\n\nWagering Bonus Plus Deposit:\n{self.bonus_plus_deposit=}\n{self.bonus_only=}")
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')
        if not self.bonus_plus_deposit and not self.bonus_only:
            raise ValidationError('At least one value must be specified (Bonus Only or Bonus + Deposit)')

# ----------------------------------------- WAGERING CONTRIBUTION ---------------------------------------------------- #

class SlotsWageringContribution(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE,
        related_name='slots_wagering', to_field='slug', null=True, blank=True
    )
    slot = models.ManyToManyField(Game, related_name='bonus_slots_wagering',)
    value = models.IntegerField(verbose_name="Wagering Contribution value %", null=True, blank=True)


class WageringContributionValue(models.Model):
    description = models.CharField(verbose_name="Wagering Contribution Description",max_length=255, default=None)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ["id"]


class WageringContribution(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='wagering_contribution', to_field='slug')
    contribution_description = models.ForeignKey(
        "WageringContributionValue", related_name='wagering_contribution',
        on_delete=models.SET_NULL, null=True,) # help_text=text_bonus_wagering_contribution
    value = models.IntegerField(null=True, verbose_name="Wagering Contribution value %")
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    class Meta:
        ordering = ["id"]
        verbose_name = "Wagering Contribution"
        verbose_name_plural = "Wagering Contribution"

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

# -------------------------------------------------------------------------------------------------------------------- #
# ======================================= RESTRICTIONS =============================================================== #
class BonusRestrictionGame(models.Model):
    bonus = models.OneToOneField(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='restriction_game', to_field='slug')
    game = models.ManyToManyField(Game, related_name='bonus_restriction_game',)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')


class BonusRestrictionCountry(models.Model):
    bonus = models.OneToOneField(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='restriction_country', to_field='slug')
    country = models.ManyToManyField(
        Country, related_name='bonus_restriction_country', null=True, blank=True,) #help_text=text_bonus_country_restriction
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')


class BonusRestrictionRtpGame(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True,
        related_name='restriction_rtp_game', to_field='slug', unique=True
    )
    value = models.FloatField(
        verbose_name="Games with RTP higher than %", null=True, blank=True,) #help_text=restriction_rtp_game-group
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')
# .................................................................................................................... #


class BonusMaxBet(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='max_bet', to_field='slug')
    value = models.IntegerField(
        null=True, blank=True, verbose_name="Bonus Max Bet value",) # help_text=text_bonus_max_bet
    symbol = models.ForeignKey(
        BaseCurrency, related_name='bonus_max_bet', on_delete=models.SET_NULL, null=True, blank=True)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    class Meta:
        ordering = ["id"]
        verbose_name = "Bonus Max Bet"
        verbose_name_plural = "Bonus Max Bet"

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')


class BonusMaxBetAutomatic(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='max_bet_automatic', to_field='slug', unique=True)
    automatic = models.BooleanField(default=False, blank=True) # help_text=text_bonus_max_bet_automatic
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', blank=True)

    # def clean(self):
    #     if self.selected_source == 'undefined':
    #         raise ValidationError('Be sure to specify the data source (Selected source)')


class BonusBuyFeature(models.Model):
    bonus = models.OneToOneField(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='buy_feature', to_field='slug')
    choice = models.BooleanField(
        default=False, verbose_name="bonus buy feature choice",) #help_text=text_bonus_other_bonus_buy
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )


class BonusSpecialNote(models.Model):
    bonus = models.OneToOneField(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='special_note', to_field='slug')
    description = models.TextField(
        verbose_name="Special Note", null=True, blank=True,) # help_text=text_bonus_other_special_notes


class BonusSubtype(models.Model):
    name = models.CharField(
        verbose_name="Name Bonus Subtype", max_length=255, default=None)

    def __str__(self):
        return self.name


class Day(models.Model):
    day =  models.CharField(verbose_name="Day",max_length=10, default=None, unique=True)

    def __str__(self):
        return self.day


class DayOfWeek(models.Model):
    bonus = models.OneToOneField(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='day_of_week', to_field='slug')
    days = models.ManyToManyField(
        'Day', null=True, blank=True,
        related_name='day_of_week', help_text=text_bonus_availability
    )
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    class Meta:
        ordering = ["id"]
        verbose_name = "Daily Availability"
        verbose_name_plural = "Daily Availability"

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')
# ******************************************************************************************************************** #
# ******************************************************************************************************************** #

class Bonus(models.Model):
    casino = models.ForeignKey(
        Casino, on_delete=models.CASCADE, null=True,
        related_name='bonuses', to_field='slug', verbose_name='Casino Name'
    )

    slug = models.SlugField(verbose_name="Bonus Slug", unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(verbose_name="Bonus Name",max_length=255, default=None, help_text=text_bonus_name)
    bonus_rank = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Bonus Rank', null=True)
    link = models.URLField(verbose_name="Bonus URL", null=True, blank=True, help_text=text_bonus_url)

    game_providers = models.ManyToManyField(Provider, verbose_name="Providers", related_name='bonus', blank=True)
    bonus_type = models.ForeignKey(
        "BonusType", null=True, on_delete=models.SET_NULL,
        default=None, related_name="bonus", help_text=text_bonus_type
    )
    bonus_subtype = models.ManyToManyField(
        "BonusSubtype", related_name='bonus', blank=True, verbose_name="Bonus Subtype", help_text=text_bonus_subtype)

    bonus_plus_deposit = models.IntegerField(
        null=True, blank=True, verbose_name="Bonus + Deposit", help_text=text_bonus_calculations_bonus_deposit
    )
    bonus_only = models.IntegerField(
        null=True, blank=True, verbose_name="Bonus Only", help_text=text_bonus_calculations_bonus_only)
    bonus_plus_freespins_value = models.IntegerField(
        null=True, blank=True, verbose_name="Bonus + Freespins value",
        help_text=text_bonus_calculations_bonus_freespins
    )

    calculation_bonus_deposit = models.FloatField(
        null=True, blank=True,
        verbose_name="Amount of Bets Calculation (Bonus+Deposit)",
        help_text=text_bonus_calculations_amount_bonus_deposit
    )
    calculation_bonus_only = models.FloatField(
        null=True, blank=True,
        verbose_name="Amount of Bets Calculation (Bonus Only)",
        help_text=text_bonus_calculations_amount_bonus_only
    )

    objects: QuerySet = models.Manager()

    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Bonuses"

    # def clean(self):
    #     print(f"\n\nBonus:\n{self.calculation_bonus_deposit=}\n{self.calculation_bonus_only=}")
    #     if not self.bonus_plus_deposit and not self.bonus_only:
    #         raise ValidationError('At least one value must be specified (Bonus Only or Bonus + Deposit)')

    def save(self, *args, **kwargs):
        additionally = ''
        try:
            if self.casino.name: additionally = self.casino.name
        except Exception as err: print(err)

        if not self.slug: self.slug = slugify(f"{self.name} {additionally}".strip())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} / {self.casino.name}"
