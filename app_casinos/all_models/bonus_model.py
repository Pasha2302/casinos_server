from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import QuerySet

from app_casinos.all_models.models import save_slug, BaseCurrency, CHOICES_SOURCE, Game, Country
from app_casinos.all_models.models import Casino


class BonusSubtype(models.Model):
    name = models.CharField(verbose_name="Name Bonus Subtype", max_length=255, default=None)
    def __str__(self):
        return self.name

class BonusType(models.Model):
    name = models.CharField(verbose_name="Name Bonus Type",max_length=255, default=None)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["id"]
        verbose_name = "Bonus Type"
        verbose_name_plural = "Types of Bonuses"

class BonusAmount(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='bonus_amount', to_field='slug')
    value = models.IntegerField(null=True, verbose_name="(CAP) value")
    symbol = models.ForeignKey(BaseCurrency, related_name='bonus_amount_symbol', on_delete=models.SET_NULL, null=True,)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )
    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

class BonusValue(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='bonus_value', to_field='slug', unique=True)
    value = models.IntegerField(null=True, verbose_name="Value %")
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )
    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

class BonusMinDep(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='bonus_min_dep', to_field='slug')
    min_value = models.IntegerField(null=True, verbose_name="Bonus min dep value")
    symbol = models.ForeignKey(BaseCurrency, related_name='bonus_min_dep', on_delete=models.SET_NULL, null=True,)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )
    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')


class BonusExpiration(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='bonus_expiration', to_field='slug', unique=True)
    days = models.IntegerField(
        null=True,
        verbose_name="Amount of Days",
        validators=[MinValueValidator(1), MaxValueValidator(30)],
        choices=[(i, i) for i in range(1, 31)]  # Это создает выбор от 1 до 30
    )
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

class PromotionPeriod(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='promotion_period', to_field='slug', unique=True)
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date")
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

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

class BonusMaxWin(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='bonus_max_win', to_field='slug')
    max_value = models.IntegerField(null=True, verbose_name="Bonus Max Win value")
    symbol = models.ForeignKey(BaseCurrency, related_name='bonus_max_win', on_delete=models.SET_NULL, null=True, )
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

class TurnoverBonus(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='turnover_bonus', to_field='slug', unique=True)
    turnover_value = models.BooleanField(default=False)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

class FreeSpinAmount(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='free_spin_amount', to_field='slug', unique=True)
    value = models.IntegerField(null=True, verbose_name="Free Spins value")
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

class OneSpin(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='one_spin', to_field='slug', unique=True)
    value = models.FloatField(null=True, verbose_name="One Spin value")
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

class Wager(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='wager', to_field='slug', unique=True)
    value = models.IntegerField(null=True, verbose_name="Wager value")
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

class BonusSlot(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='bonus_slot', to_field='slug', unique=True)
    slots = models.ManyToManyField(Game, related_name='bonus_slots')
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

class Wagering(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='wagering', to_field='slug', unique=True)
    tbwr = models.TextField(null=True, blank=True, verbose_name="Turnover bonus wagering requirement")
    tbwe = models.TextField(null=True, blank=True, verbose_name="Turnover bonus wagering example")
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

# -------------------------------------------------------------------------------------------------------------------- #
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
        "WageringContributionValue", related_name='wagering_contribution', on_delete=models.SET_NULL, null=True,)
    value = models.IntegerField(null=True, verbose_name="Wagering Contribution value %")
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')
# -------------------------------------------------------------------------------------------------------------------- #
# ======================================= RESTRICTIONS =============================================================== #
class BonusRestrictionGame(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='restriction_game', to_field='slug', unique=True)
    game = models.ManyToManyField(Game, related_name='bonus_restriction_game')
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

class BonusRestrictionCountry(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True,
        related_name='restriction_country', to_field='slug', unique=True
    )
    country = models.ManyToManyField(Country, related_name='bonus_restriction_country')
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

class BonusRestrictionRtpGame(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True,
        related_name='restriction_rtp_game', to_field='slug', unique=True
    )
    value = models.FloatField(null=True, verbose_name="Games with RTP higher than %")
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')
# .................................................................................................................... #

class BonusMaxBet(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='max_bet', to_field='slug')
    value = models.IntegerField(null=True, blank=True, verbose_name="Bonus Max Bet value")
    symbol = models.ForeignKey(
        BaseCurrency, related_name='bonus_max_bet', on_delete=models.SET_NULL, null=True, blank=True)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

class BonusMaxBetAutomatic(models.Model):
    bonus = models.ForeignKey(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='max_bet_automatic', to_field='slug', unique=True)
    automatic = models.BooleanField(default=False)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    def clean(self):
        if self.selected_source == 'undefined':
            raise ValidationError('Be sure to specify the data source (Selected source)')

class BonusBuyFeature(models.Model):
    bonus = models.OneToOneField(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='buy_feature', to_field='slug')
    choice = models.BooleanField(default=False)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

class BonusSpecialNote(models.Model):
    bonus = models.OneToOneField(
        "Bonus", on_delete=models.CASCADE, null=True, related_name='special_note', to_field='slug')
    description = models.TextField(verbose_name="Special Note", null=True, blank=True)

# ******************************************************************************************************************** #

class Bonus(models.Model):
    casino = models.ForeignKey(
        Casino, on_delete=models.CASCADE, null=True, related_name='bonuses', to_field='slug')

    slug = models.SlugField(verbose_name="Bonus Slug", unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(verbose_name="Bonus Name",max_length=255, default=None)
    link = models.URLField(verbose_name="Bonus URL", null=True, blank=True)

    bonus_type = models.ForeignKey(
        "BonusType", null=True, on_delete=models.SET_NULL, default=None, related_name="bonus")
    bonus_subtypes = models.ManyToManyField("BonusSubtype", related_name='bonus', blank=True,)
    social_bonuses = models.BooleanField(default=False)

    bonus_plus_deposit = models.IntegerField(null=True, verbose_name="Bonus + Deposit")
    bonus_only = models.IntegerField(null=True, verbose_name="Bonus Only")
    bonus_plus_freespins_value = models.IntegerField(null=True, blank=True, verbose_name="Bonus + Freespins value")

    objects: QuerySet = models.Manager()

    def save(self, *args, **kwargs):
        save_slug(self, super(), additionally=None, *args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Bonuses"