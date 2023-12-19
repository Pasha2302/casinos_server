from django.contrib import admin
from app_casinos.models import (Casino, Bonus, WithdrawalLimit, SisterCasino,
                                MinWagering, MinDep, Country, Language, AccountData,
                                GameType, Provider, Game, ClassicCurrency, CryptoCurrency, LicensingAuthority)


class AccountDataInline(admin.TabularInline):
    model = AccountData
    extra = 1

class LicensesInline(admin.TabularInline):
    model = Casino.licenses.through
    extra = 1
    # verbose_name_plural = "Licensing Authorities"

class BonusesInline(admin.TabularInline):  # Используем StackedInline вместо TabularInline
    model = Bonus
    fields = ('name', 'link')
    extra = 1  # Задает начальное количество отображаемых форм
    search_fields = ('name',)

class WithdrawalLimitInline(admin.TabularInline):
    model = WithdrawalLimit
    extra = 1

class SisterCasinoInline(admin.TabularInline):
    model = SisterCasino
    extra = 1

class MinWageringInline(admin.TabularInline):
    model = MinWagering
    extra = 1

class MinDepInline(admin.TabularInline):
    model = MinDep
    extra = 1