from django.contrib import admin
from django.utils.html import format_html
from django.db import models

from app_casinos.forms import NoClearableFileInput, FilterMinDepAdminForm, AccountDataForm
from app_casinos.models import Casino, AccountData, CasinoImage, Bonus, WithdrawalLimit, SisterCasino, MinWagering, \
    MinDep


class GameInline(admin.TabularInline):
    model = Casino.games.through  # games - поля ManyToMany в модели Casino
    extra = 1  # Количество дополнительных форм для ввода
    max_num = 0  # Запрет добавления новых записей
    can_delete = False  # Запрет удаления записей
    raw_id_fields = ['game']

class AccountDataInline(admin.TabularInline):
    # form = AccountDataForm
    model = AccountData
    can_delete = False
    fields = ('log', 'password', 'signature')

# ================================================================================================================== #

class CasinoImageInline(admin.TabularInline):
    model = CasinoImage
    extra = 1
    can_delete = False  # Запрещаем удаление записей
    formfield_overrides = {
        models.ImageField: {'widget': NoClearableFileInput},
    }
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
        else:
            return None


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


# ==================================================================================================================== #

class MinDepInline(admin.TabularInline):
    model = MinDep
    form = FilterMinDepAdminForm
    extra = 1
    can_delete = False
    fields = ('min_value', 'symbol', 'selected_source',)

