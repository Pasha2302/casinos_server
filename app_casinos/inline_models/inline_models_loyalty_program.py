from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from app_casinos.models.loyalty_program import (
    PointAccumulation, Cashback, LevelUpBonus, LevelLoyalty, LoyaltyProgram,
    Withdrawals, SpecialPrize, Gifts, LoyaltyBonus
)


class LoyaltyBonusInline(admin.TabularInline):
    model = LoyaltyBonus


class GiftsInline(admin.StackedInline):
    model = Gifts


class SpecialPrizeInline(admin.TabularInline):
    model = SpecialPrize


class WithdrawalsInline(admin.TabularInline):
    model = Withdrawals


class LevelLoyaltyInline(admin.TabularInline):
    model = LevelLoyalty
    fields = ('level', 'edit_link')  # Добавляем поле 'edit_link'
    readonly_fields = ('edit_link',)  # Делаем поле только для чтения
    extra = 1

    def edit_link(self, obj):
        # Создаем ссылку, которая ведет на страницу редактирования конкретной записи
        if obj.pk:
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name),  args=[obj.pk] )
            return format_html('<a href="{}">Edit Level</a>', url)
        else:
            # Если бонус еще не существует, создаем ссылку на создание новой записи
            url = reverse('admin:%s_%s_add' % (obj._meta.app_label, obj._meta.model_name))
            return format_html('<a href="{}">Add Level</a>', url)

    edit_link.short_description = 'Editing and Adding'  # Задаем короткое описание для поля


class LevelUpBonusInline(admin.TabularInline):
    model = LevelUpBonus


class CashbackInline(admin.TabularInline):
    model = Cashback


class PointAccumulationInline(admin.TabularInline):
    model = PointAccumulation
    fields = ('point', 'value', 'next_lvl', 'level_value')


class LoyaltyProgramInline(admin.TabularInline):
    model = LoyaltyProgram
    fields = ('link', 'loyalty_understandable', 'vip_manager', 'edit_link')  # Добавляем поле 'edit_link'
    readonly_fields = ('edit_link',)  # Делаем поле только для чтения

    def edit_link(self, obj):
        # Создаем ссылку, которая ведет на страницу редактирования конкретной записи
        if obj.pk:
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name),  args=[obj.pk] )
            return format_html('<a href="{}">Edit Loyalty Program or add levels</a>', url)
        else:
            # Если бонус еще не существует, создаем ссылку на создание новой записи
            model_name = obj._meta.model_name
            url = reverse('admin:%s_%s_add' % (obj._meta.app_label, model_name))
            return format_html('<a href="{}">Add loyalty Program or add levels</a>', url)

    edit_link.short_description = 'Editing and Adding'  # Опционально, задаем короткое описание для поля
