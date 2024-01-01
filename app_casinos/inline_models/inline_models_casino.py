from django.contrib import admin
from django.utils.html import format_html
from django.db import models

from app_casinos.forms import NoClearableFileInput, AccountDataForm
from app_casinos.all_models.bonus_model import Bonus
from app_casinos.all_models.models import (
    Casino, AccountData, CasinoImage, WithdrawalLimit,
    SisterCasino, MinWagering,MinDep,
)


class GameInline(admin.TabularInline):
    model = Casino.games.through  # games - поля ManyToMany в модели Casino
    extra = 1  # Количество дополнительных форм для ввода
    max_num = 0  # Запрет добавления новых записей
    can_delete = False  # Запрет удаления записей
    raw_id_fields = ['game']

class AccountDataInline(admin.TabularInline):
    form = AccountDataForm
    model = AccountData
    extra = 1
    max_num = 0
    can_delete = False
    fields = ('login', 'password', ) # 'signature'

# ================================================================================================================== #

class CasinoImageInline(admin.TabularInline):
    model = CasinoImage
    extra = 1
    can_delete = True  # Разрешаем удаление записей
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
    max_num = 1
    can_delete = False


# ==================================================================================================================== #

class MinDepInline(admin.TabularInline):
    model = MinDep
    extra = 1

    can_delete = False
    fields = ('min_value', 'symbol', 'selected_source',)
    autocomplete_fields = ('symbol',)

    def get_formset(self, request, obj=None, **kwargs):
        # print(f"{'&&' * 60}\n\nForm Set:\n"
        #       f"{obj=}\n"
        #       f"{obj.min_dep.__dict__=}\n"
        #       f"{obj.min_dep.all()=}\n")

        formset = super().get_formset(request, obj, **kwargs)
        # print(formset, type(formset))
        # print(formset.__dict__)
        try:
            obj_min_dip = obj.min_dep
            if len(obj_min_dip.all()) > 0: formset.extra = 0
        except Exception as err_extra: print(f"[file -> inline_models_admin.py] err_extra: {err_extra}")

        return formset
