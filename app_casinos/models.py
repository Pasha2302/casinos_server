from django.db import models
from django.db.models import QuerySet
from django.utils.text import slugify
from app_casinos.description_model_fields import *


CHOICES_SOURCE = [
    ('terms_and_conditions', 'Terms & Conditions'),
    ('support', 'Support'),
    ('website', 'Website'),
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


class Bonus(models.Model):
    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, default=None)
    link = models.URLField()
    description = models.TextField()

    casino = models.ForeignKey(
        'Casino', on_delete=models.CASCADE, null=True, related_name='bonuses', to_field='slug')

    objects: QuerySet = models.Manager()

    def save(self, *args, **kwargs):
        save_slug(self, super(), additionally=None, *args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["id"]
        verbose_name_plural = "Bonuses"


class WithdrawalLimit(models.Model):
    casino = models.OneToOneField("Casino", on_delete=models.CASCADE, related_name='withdrawal_limit')
    daily = models.IntegerField(null=True, blank=True)
    weekly = models.IntegerField(null=True, blank=True)
    monthly = models.IntegerField(null=True, blank=True)

    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE)

    def save(self, *args, **kwargs):
        if not self.selected_source or self.selected_source not in dict(CHOICES_SOURCE):
            raise ValueError("Exactly one option must be selected.")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Withdrawal Limits: {self.selected_source}"


class SisterCasino(models.Model):
    name = models.CharField(max_length=255, blank=True)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE)
    casino = models.ForeignKey(
        "Casino", on_delete=models.CASCADE, null=True, related_name='sister_casinos', to_field='slug')

    def save(self, *args, **kwargs):
        if not self.selected_source or self.selected_source not in dict(CHOICES_SOURCE):
            raise ValueError("Exactly one option must be selected.")
        super().save(*args, **kwargs)

class MinWagering(models.Model):
    min_value = models.IntegerField(null=True, blank=True)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE)
    casino = models.OneToOneField(
        "Casino", on_delete=models.CASCADE, null=True, related_name='min_wagering', to_field='slug')

    def save(self, *args, **kwargs):
        if not self.selected_source or self.selected_source not in dict(CHOICES_SOURCE):
            raise ValueError("Exactly one option must be selected.")
        super().save(*args, **kwargs)


class MinDep(models.Model):
    currency_choices = [
        ('$', 'USD'),
        ('RUB', 'RUB'),
        ('BNB', 'BNB'),
    ]

    min_value = models.IntegerField(null=True, blank=True)
    casino = models.ForeignKey(
        "Casino", on_delete=models.CASCADE, null=True, related_name='min_dep', to_field='slug')

    symbol = models.CharField(max_length=3, choices=currency_choices)
    selected_source = models.CharField(max_length=20, choices=CHOICES_SOURCE)

    def save(self, *args, **kwargs):
        if not self.selected_source or self.selected_source not in dict(CHOICES_SOURCE):
            raise ValueError("Exactly one option must be selected.")
        super().save(*args, **kwargs)


class Country(models.Model):
    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, verbose_name="Country")
    class Meta:
        ordering = ["id"]
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        save_slug(self, super(), additionally=None, *args, **kwargs)


class Language(models.Model):
    slug = models.SlugField(unique=True, db_index=True, max_length=255)
    name = models.CharField(max_length=255, verbose_name="Language")

    def __str__(self):
        return self.name

class GameType(models.Model):
    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, verbose_name="Casino Name")
    objects: QuerySet = models.Manager()
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        save_slug(self, super(), additionally=None, *args, **kwargs)

class Provider(models.Model):
    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, verbose_name="Casino Name")
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        save_slug(self, super(), additionally=None, *args, **kwargs)

class Game(models.Model):
    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, verbose_name="Game Name")

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        save_slug(self, super(), additionally=None, *args, **kwargs)

class PaymentMethod(models.Model):
    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, verbose_name="Game Name")
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        save_slug(self, super(), additionally=None, *args, **kwargs)

class ClassicCurrency(models.Model):
    symbol = models.CharField(max_length=255, verbose_name="Symbol Currency", unique=True)
    name = models.CharField(max_length=255, verbose_name="Currency", blank=True, null=True)
    def __str__(self):
        return f"{self.symbol} | {self.name}"
    class Meta:
        ordering = ["id"]
        verbose_name = "Classic Currency"
        verbose_name_plural = "Classic Currencies"

class CryptoCurrency(models.Model):
    symbol = models.CharField(max_length=255, verbose_name="Symbol Currency", unique=True)
    name = models.CharField(max_length=255, verbose_name="Name Currency", blank=True, null=True)
    def __str__(self):
        return f"{self.symbol} | {self.name}"
    class Meta:
        ordering = ["id"]
        verbose_name = "Crypto Currency"
        verbose_name_plural = "Crypto Currencies"

class AccountData(models.Model):
    casino = models.OneToOneField(
        "Casino", on_delete=models.CASCADE, null=True, related_name='account_data', to_field='slug')
    log = models.CharField(max_length=50, verbose_name="Login")
    password = models.CharField(max_length=15, verbose_name="Password", blank=True, null=True)
    def __str__(self):
        return self.log
    class Meta:
        ordering = ["id"]
        verbose_name = "Account Data"
        verbose_name_plural = "Account Data"

# ==================================================================================================================== #
class Casino(models.Model):
    CHOICES_LIVE_CHAT = [
        (1, 'High Competence'),
        (2, 'Above Average'),
        (3, 'Average'),
        (4, 'Below Average'),
        (5, 'Incompetent'),
    ]

    slug = models.SlugField(unique=True, db_index=True, blank=True, max_length=255)
    name = models.CharField(max_length=255, verbose_name="Casino Name", help_text=text_casino_name)

    using_vpn = models.BooleanField(default=False, help_text=text_casino_vpn)
    sportsbook = models.BooleanField(default=False, help_text=text_casino_sportsbook)

    url = models.URLField(verbose_name="URL Website", help_text=text_url_casino)
    link_casino_guru = models.URLField(verbose_name="URL Casino-Guru", help_text=text_url_casinoguru)
    link_tc = models.URLField(verbose_name="URL General T&C", help_text=text_url_general_tc)
    link_bonus_tc = models.URLField(verbose_name="URL Bonus T&C", blank=True, help_text=text_url_bonus_tc)
    link_bonuses = models.URLField(
        verbose_name="URL Bonuses Main Page", null=True, blank=True, help_text=text_url_bonus_main_page)

    owner = models.CharField(
        max_length=255, verbose_name="Casino Owner", help_text=text_casino_owner, null=True, blank=True)
    established = models.PositiveIntegerField(
        verbose_name="Year of Establishment", help_text=text_casino_establish_year, null=True, blank=True)

    language_website = models.ManyToManyField("Language", related_name='casino_website', help_text=text_casino_website_languages)
    language_live_chat = models.ManyToManyField("Language", related_name='casino_live_chat', help_text=text_casino_livechat_languages)

    blocked_countries = models.ManyToManyField("Country", related_name='casinos_blocked', help_text=text_casino_blocked_countries)
    licenses = models.ManyToManyField(
        "LicensingAuthority", related_name='casino_licenses', help_text=text_casino_license)

    game_types = models.ManyToManyField("GameType", related_name='casino_game_types')
    game_providers = models.ManyToManyField("Provider", related_name='casino_providers')
    games = models.ManyToManyField("Game", related_name='casino_games')

    classic_currency = models.ManyToManyField("ClassicCurrency", related_name='casino_classic_currency')
    crypto_currencies = models.ManyToManyField("CryptoCurrency", related_name='casino_crypto_currencies')
    payment_methods = models.ManyToManyField("PaymentMethod", related_name='casino_payment_method')

    wager_limit = models.BooleanField(default=False)
    loss_limit = models.BooleanField(default=False)
    session_limit = models.BooleanField(default=False)
    self_exclusion = models.BooleanField(default=False)
    cool_off = models.BooleanField(default=False)
    reality_check = models.BooleanField(default=False)
    self_assessment = models.BooleanField(default=False)
    withdrawal_lock = models.BooleanField(default=False)
    tournaments = models.BooleanField(default=False, verbose_name="Tournaments")

    special_notes = models.TextField(blank=True)
    live_chat_competence = models.IntegerField(choices=CHOICES_LIVE_CHAT, default='High Competence')
    bonus_hunt_active_bonus = models.BooleanField(default=False, help_text=text_casino_bonus_hunt)

    objects: QuerySet = models.Manager()

    def save(self, *args, **kwargs):
        save_slug(self, super(), additionally=None, *args, **kwargs)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["id"]
        verbose_name = "Casino"
        verbose_name_plural = "Casinos"




