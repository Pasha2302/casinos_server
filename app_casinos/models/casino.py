from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import QuerySet, Case, When, Value, IntegerField
from django.utils.text import slugify
from app_casinos.description_model_fields import *

CHOICES_SOURCE = [
    ('undefined', 'Undefined'),
    ('terms_and_conditions', 'Terms & Conditions'),
    ('support', 'Support'),
    ('website', 'Website'),
    ('common_sense', 'Common Sense'),
]

def save_slug(self, _super, additionally=None, *args, **kwargs):
    if additionally is None: additionally = ''
    if not self.slug: self.slug = slugify(f"{self.name} {additionally}".strip())
    _super.save(*args, **kwargs)


class LicensingAuthority(models.Model):
    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, verbose_name="Name of authority")
    validator_url = models.URLField(verbose_name="Validator Url", blank=True, null=True)

    def save(self, *args, **kwargs):
        save_slug(self, super(), additionally=None, *args, **kwargs)

    class Meta:
        ordering = ["id"]
        verbose_name = "Licensing Authority"
        verbose_name_plural = "Licensing Authorities"

    def __str__(self):
        return self.name


class WithdrawalLimit(models.Model):
    casino = models.OneToOneField("Casino", on_delete=models.CASCADE, related_name='withdrawal_limit')
    daily = models.IntegerField(null=True, blank=True)
    weekly = models.IntegerField(null=True, blank=True)
    monthly = models.IntegerField(null=True, blank=True)

    unlimited = models.BooleanField()
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='')

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    # def clean(self):
    #     check_selected_source = self.selected_source if self.selected_source != 'undefined' else False
    #     values = (self.daily, self.weekly, self.monthly, check_selected_source)
    #     print(values)
    #     if not self.unlimited and not all(values):
    #         raise ValidationError('All fields must be filled when unlimited is False.')
    #     if not check_selected_source:
    #         raise ValidationError('Be sure to specify the data source (Selected source)')

    def __str__(self):
        str_unlimited = 'there are limits'
        if self.unlimited: str_unlimited = 'no limits'
        return f"Withdrawal Limits: {str_unlimited} | {self.casino.name}"


class SisterCasino(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class MinWagering(models.Model):
    min_value = models.IntegerField(null=True, blank=True)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='')
    unlimited = models.BooleanField(default=False)

    casino = models.OneToOneField(
        "Casino", on_delete=models.CASCADE, null=True, related_name='min_wagering', to_field='slug')

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    def clean(self):
        check_selected_source = self.selected_source if self.selected_source != 'undefined' else False
        print(f"Min Wagering: {check_selected_source=}")
        if not self.unlimited and not self.min_value:
            raise ValidationError('Values: MIN VALUE are required, or set to UNLIMITED.')
        elif self.unlimited and self.min_value:
            self.min_value = None
            self.symbol = None
            self.save()
        if not check_selected_source:
            raise ValidationError('Be sure to specify the data source (Selected source)')

# ------------------------------------------------------------------------------------------------------------------ #

class MinDep(models.Model):
    min_value = models.FloatField(null=True, blank=True)
    casino = models.ForeignKey(
        "Casino", on_delete=models.CASCADE, null=True, related_name='min_dep', to_field='slug')

    symbol = models.ForeignKey(
        "BaseCurrency", related_name='min_dip_symbol', on_delete=models.SET_NULL, null=True, blank=True)
    unlimited = models.BooleanField(default=False)

    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='',)

    class Meta:
        ordering = ["id"]
        verbose_name = "Min Deposit"
        verbose_name_plural = "Min Deposit"

    def __str__(self):
        return ''

    def clean(self):
        check_selected_source = self.selected_source if self.selected_source != 'undefined' else False
        print(f"Min Wagering: {check_selected_source=}")
        if not self.unlimited and not all((self.min_value, self.symbol)):
            raise ValidationError('Values: MIN VALUE, SYMBOL are required, or set to UNLIMITED.')
        elif self.unlimited and any((self.min_value, self.symbol)):
            self.min_value = None
            self.symbol = None
            self.save()
        if not check_selected_source:
            raise ValidationError('Be sure to specify the data source (Selected source)')

# ------------------------------------------------------------------------------------------------------------------ #

class Country(models.Model):
    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, verbose_name="Country Name")
    name2 = models.CharField(max_length=255, verbose_name="Country Name-2", null=True, blank=True)
    name3 = models.CharField(max_length=255, verbose_name="Country Name-3", null=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"{self.name} | {self.name2} | {self.name3}"

    def save(self, *args, **kwargs):
        save_slug(self, super(), additionally=None, *args, **kwargs)


class Language(models.Model):
    slug = models.SlugField(unique=True, db_index=True, max_length=255)
    name = models.CharField(max_length=255, verbose_name="Language")

    def __str__(self):
        return self.name


class GameType(models.Model):
    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, verbose_name="Game Type")
    objects: QuerySet = models.Manager()

    class Meta:
        ordering = [
            Case(
                When(name="Betting", then=Value(0)),
                When(name="Esports betting", then=Value(1)),
                default=Value(2),
                output_field=IntegerField(),
            ),
            "name"
        ]
        verbose_name = "Game Type"
        verbose_name_plural = "Game Type"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        save_slug(self, super(), additionally=None, *args, **kwargs)


class Provider(models.Model):
    name = models.CharField(max_length=255, verbose_name="Provider Name")

    def __str__(self):
        return self.name


class Game(models.Model):
    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, db_index=True, verbose_name="Game Name")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        save_slug(self, super(), additionally=None, *args, **kwargs)


class PaymentMethod(models.Model):
    name = models.CharField(max_length=255, verbose_name="Game Name")

    def __str__(self):
        return self.name


class BaseCurrency(models.Model):
    symbol = models.CharField(max_length=255, verbose_name="Symbol Currency", unique=True, null=True)
    name = models.CharField(max_length=255, verbose_name="Name Currency", null=True)
    name2 = models.CharField(max_length=255, verbose_name="Name2 Currency", null=True, blank=True)

    def __str__(self):
        additional_name = ''
        if self.name2: additional_name = f' | {self.name2}'
        return f"{self.symbol} | {self.name}{additional_name}"
    class Meta:
        ordering = ["id"]
        verbose_name = "Base Currency"
        verbose_name_plural = "Base Currencies"


class ClassicCurrency(BaseCurrency):
    class Meta:
        ordering = ["id"]
        verbose_name = "Classic Currency"
        verbose_name_plural = "Classic Currencies"


class CryptoCurrency(BaseCurrency):

    class Meta:
        ordering = ["id"]
        verbose_name = "Crypto Currency"
        verbose_name_plural = "Crypto Currencies"


class AccountData(models.Model):
    casino = models.OneToOneField(
        "Casino", on_delete=models.CASCADE, related_name='account_data', to_field='slug',)
    login = models.CharField(max_length=50, verbose_name="Login",)
    password = models.CharField(max_length=15, verbose_name="Password",)
    user_name = models.CharField(max_length=20, verbose_name="User Name", null=True, blank=True)

    def __str__(self):
        return self.login
    class Meta:
        ordering = ["login"]
        verbose_name = "Account Data"
        verbose_name_plural = "Account Data"
# ==================================================================================================================== #


class CasinoImage(models.Model):
    casino = models.ForeignKey("Casino", on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='casino_images/', verbose_name='Casino Image', null=True, blank=True)


class AffiliatesProgram(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Affiliate(models.Model):
    affiliate_program = models.ForeignKey(
        "AffiliatesProgram", on_delete=models.SET_NULL,
        null=True, blank=True, related_name='casino_affiliate_program', default=None
    )
    link_affiliate_program = models.URLField(verbose_name="affiliate Program URL", null=True, blank=True)
    link_affiliate = models.URLField(verbose_name="Affiliate Link", null=True, blank=True)

    class Meta:
        ordering = ["affiliate_program"]

    def __str__(self):
        return self.affiliate_program.name


class CasinoTheme(models.Model):
    name = models.CharField(max_length=255, verbose_name="Description",)
    def __str__(self):
        return self.name


class SocialBonus(models.Model):
    bonus = models.OneToOneField(
        "Casino", on_delete=models.CASCADE, null=True, related_name='social_bonuses', to_field='slug')
    choice = models.BooleanField(
        default=False, verbose_name="social bonuses choice", help_text=text_casino_other_social_bonuses)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE, default='', )

    class Meta:
        ordering = ["id"]
        verbose_name = "Social Bonus"
        verbose_name_plural = "Social Bonus"


class Casino(models.Model):
    CHOICES_LIVE_CHAT = [
        ("", ""),
        ("no_chat", 'No Chat'),
        ("didn't_answer_to_questions", "Didn't Answer to Questions"),
        ("high_competence", 'High Competence'),
        ("above_average", 'Above Average'),
        ("average", 'Average'),
        ("below_average", 'Below Average'),
        ("incompetent", 'Incompetent'),
    ]
    is_pars_data = models.BooleanField(default=False)
    affiliate = models.OneToOneField(
        "Affiliate", null=True, blank=True, on_delete=models.SET_NULL, related_name='casino')

    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, verbose_name="Casino Name", help_text=text_casino_name)
    casino_rank = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Casino Rank', null=True)

    theme = models.ForeignKey(
        "CasinoTheme", verbose_name="Casino Theme",
        on_delete=models.SET_NULL, related_name='casino', null=True, blank=True, help_text=text_casino_theme
    )

    vpn_usage = models.BooleanField(default=False, help_text=text_casino_vpn)
    sportsbook = models.BooleanField(default=False, help_text=text_casino_sportsbook)

    url = models.URLField(verbose_name="URL Website", help_text=text_url_casino)
    link_loyalty = models.URLField(verbose_name="URL Loyalty", null=True, blank=True)
    link_casino_guru = models.URLField(verbose_name="URL Casino-Guru", help_text=text_url_casinoguru)
    link_tc = models.URLField(verbose_name="URL General T&C", help_text=text_url_general_tc)
    link_bonus_tc = models.URLField(verbose_name="URL Bonus T&C", blank=True, help_text=text_url_bonus_tc)
    link_bonuses = models.URLField(
        verbose_name="URL Bonuses Main Page", null=True, blank=True, help_text=text_url_bonus_main_page)

    owner = models.CharField(
        max_length=255, verbose_name="Casino Owner", help_text=text_casino_owner, null=True, blank=True)
    established = models.PositiveIntegerField(
        verbose_name="Year of Establishment", help_text=text_casino_establish_year, null=True, blank=True)

    sisters_casinos = models.ManyToManyField("SisterCasino", related_name='casino')

    language_website = models.ManyToManyField("Language", related_name='casino_website',
                                              help_text=text_casino_website_languages)
    language_live_chat = models.ManyToManyField("Language", related_name='casino_live_chat',
                                                help_text=text_casino_livechat_languages, null=True, blank=True)
    blocked_countries = models.ManyToManyField("Country", related_name='casino',
                                               help_text=text_casino_blocked_countries)
    licenses = models.ManyToManyField("LicensingAuthority", related_name='casino',
                                      help_text=text_casino_license)

    game_types = models.ManyToManyField("GameType", related_name='casino')
    game_providers = models.ManyToManyField("Provider", related_name='casino')
    games = models.ManyToManyField("Game", related_name='casino')

    classic_currency = models.ManyToManyField("ClassicCurrency", related_name='casino', null=True, blank=True)
    crypto_currencies = models.ManyToManyField("CryptoCurrency", related_name='casino', null=True, blank=True)
    payment_methods = models.ManyToManyField("PaymentMethod", related_name='casino')

    wager_limit = models.BooleanField(default=False, help_text=text_casino_responsible_gambling_wager_limit)
    loss_limit = models.BooleanField(default=False, help_text=text_casino_responsible_gambling_loss_limit)
    session_limit = models.BooleanField(default=False, help_text=text_casino_responsible_gambling_session_limit)
    self_exclusion = models.BooleanField(default=False, help_text=text_casino_responsible_gambling_self_exclusion)
    cool_off = models.BooleanField(default=False, help_text=text_casino_responsible_gambling_cool_off)
    reality_check = models.BooleanField(default=False, help_text=text_casino_responsible_gambling_reality_check)
    self_assessment = models.BooleanField(default=False, help_text=text_casino_responsible_gambling_self_assessment)
    withdrawal_lock = models.BooleanField(default=False, help_text=text_casino_responsible_gambling_withdrawal_lock)
    deposit_limit = models.BooleanField(default=False, help_text=text_casino_responsible_gambling_deposit_limit)
    gamstop_self_exclusion = models.BooleanField(
        default=False, verbose_name='GAMSTOP self exclusion', help_text=text_gamstop_self_exclusion
    )

    tournaments = models.BooleanField(default=False, verbose_name="Tournaments", help_text=text_casino_tournaments)

    special_notes = models.TextField(blank=True)
    live_chat_competence = models.CharField(
        null=True, max_length=50, choices=CHOICES_LIVE_CHAT, default='',blank=True)
    bonus_hunt_with_active_bonus = models.BooleanField(default=False, help_text=text_casino_bonus_hunt)

    objects: QuerySet = models.Manager()

    class Meta:
        ordering = ["id"]
        verbose_name = "Casino"
        verbose_name_plural = "Casinos"

    def clean(self):
        if self.casino_rank and  self.casino_rank > 10:
            raise ValidationError('The value [Casino Rank] cannot be greater than 10')

    def save(self, *args, **kwargs):
        save_slug(self, super(), additionally=None, *args, **kwargs)

    def __str__(self):
        return self.name
