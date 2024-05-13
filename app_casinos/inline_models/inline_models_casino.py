from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.db import models

from app_casinos.forms import NoClearableFileInput, AccountDataForm
from app_casinos.models.bonus import Bonus
from app_casinos.models.casino import (
    Casino, AccountData, CasinoImage, WithdrawalLimit,
    MinWagering, MinDep, SocialBonus,
)


class SocialBonusInline(admin.TabularInline):
    model = SocialBonus
    # extra = 1
    # can_delete = False


class GameInline(admin.TabularInline):
    model = Casino.games.through  # games - поля ManyToMany в модели Casino
    extra = 1  # Количество дополнительных форм для ввода
    max_num = 0  # Запрет добавления новых записей
    # can_delete = False  # Запрет удаления записей
    raw_id_fields = ['game']

class AccountDataInline(admin.TabularInline):
    form = AccountDataForm
    model = AccountData
    extra = 1
    max_num = 0
    # can_delete = False
    fields = ('login', 'password', 'user_name',)

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


class BonusInline(admin.TabularInline):
    model = Bonus
    fields = ('name', 'link', 'edit_link')  # Добавляем поле 'edit_link'
    readonly_fields = ('edit_link',)  # Делаем поле только для чтения

    extra = 1

    def edit_link(self, obj):
        # Создаем ссылку, которая ведет на страницу редактирования конкретной записи
        if obj.pk:
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name),  args=[obj.pk] )
            return format_html('<a href="{}">Edit Bonus</a>', url)
        else:
            # Если бонус еще не существует, создаем ссылку на создание нового бонуса
            model_name = obj._meta.model_name
            url = reverse('admin:%s_%s_add' % (obj._meta.app_label, model_name))
            return format_html('<a href="{}">Add Bonus</a>', url)

    edit_link.short_description = 'Editing and Adding'  # Опционально, задаем короткое описание для поля


class WithdrawalLimitInline(admin.TabularInline):
    model = WithdrawalLimit
    extra = 1
    # can_delete = False


# class SisterCasinoInline(admin.TabularInline):
#     model = SisterCasino
#     extra = 1
#     readonly_fields = ('name', 'selected_source')
#     max_num = 0  # Запрет добавления новых записей
#     can_delete = False  # Запрет удаления записей


class MinWageringInline(admin.TabularInline):
    model = MinWagering
    extra = 1
    max_num = 1
    # can_delete = False
    fields = ('min_value', 'unlimited', 'selected_source',)


# ==================================================================================================================== #

class MinDepInline(admin.TabularInline):
    model = MinDep
    extra = 1

    # can_delete = False
    fields = ('min_value', 'symbol', 'unlimited', 'selected_source',)
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
