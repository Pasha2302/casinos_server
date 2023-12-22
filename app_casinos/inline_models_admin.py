from django.contrib import admin, messages
from django.utils.html import format_html

from app_casinos.models import (Casino, Bonus, WithdrawalLimit, SisterCasino,
                                MinWagering, MinDep, Country, Language, AccountData,
                                GameType, Provider, Game, ClassicCurrency, CryptoCurrency, LicensingAuthority,
                                CasinoImage)


class GameInline(admin.TabularInline):
    model = Casino.games.through  # games - поля ManyToMany в модели Casino
    extra = 1  # Количество дополнительных форм для ввода
    max_num = 0  # Запрет добавления новых записей
    can_delete = False  # Запрет удаления записей
    raw_id_fields = ['game']

class AccountDataInline(admin.TabularInline):
    model = AccountData
    extra = 1

class CasinoImageInline(admin.TabularInline):
    model = CasinoImage
    extra = 1
    can_delete = False  # Запрет удаления записей
    readonly_fields = ('display_image',)
    fieldsets = (
        (None, {
            'fields': ('display_image', 'image',)
        }),
    )

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 140px; max-width: 180px;" />', obj.image.url)
        else: return None

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
    max_num = 1  # Запрет добавления новых записей
    can_delete = False  # Запрет удаления записей

class SisterCasinoInline(admin.TabularInline):
    model = SisterCasino
    extra = 1
    readonly_fields = ('name', 'selected_source')
    max_num = 0  # Запрет добавления новых записей
    can_delete = False  # Запрет удаления записей

class MinWageringInline(admin.TabularInline):
    model = MinWagering
    extra = 1

class MinDepInline(admin.TabularInline):
    model = MinDep
    extra = 1
    filter_horizontal = ('symbol', )
    max_num = 1  # Запрет добавления новых записей
    can_delete = False  # Запрет удаления записей
