from django.core.exceptions import ValidationError
from django.db import models

from app_casinos.models.casino import Casino


class CashbackPeriod(models.Model):
    name = models.CharField(verbose_name="Cashback Period", max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class CashbackType(models.Model):
    name = models.CharField(verbose_name="Cashback Type", max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Cashback(models.Model):
    level_loyalty = models.OneToOneField(
        "LevelLoyalty", null=True, on_delete=models.CASCADE, related_name='cashback')
    cashback_type = models.ForeignKey("CashbackType", on_delete=models.CASCADE, related_name='cashback')
    cashback_period = models.ForeignKey("CashbackPeriod", on_delete=models.CASCADE, related_name='cashback')
    percentage = models.FloatField(null=True, blank=True, verbose_name="Percentage %")
    wager = models.IntegerField(null=True, blank=True, verbose_name="Wager X")


class PointAccumulation(models.Model):
    level_loyalty = models.OneToOneField(
        "LevelLoyalty", null=True, on_delete=models.CASCADE, related_name='point_accumulation')
    point = models.IntegerField(null=True, blank=True, verbose_name="Point")
    value = models.IntegerField(null=True, blank=True, verbose_name="Value Point")
    next_lvl = models.IntegerField(null=True, blank=True, verbose_name="Next Level")
    level_value = models.IntegerField(null=True, blank=True, verbose_name="Level Value")


class LevelUpBonus(models.Model):
    level_loyalty = models.OneToOneField(
        "LevelLoyalty", null=True, on_delete=models.CASCADE, related_name='level_up_bonus')
    bonus = models.CharField(verbose_name="Bonus", max_length=255, null=True, blank=True)
    wager = models.IntegerField(verbose_name="Wager", null=True, blank=True)
    freespins = models.IntegerField(verbose_name="Freespins", null=True, blank=True)


class Withdrawals(models.Model):
    level_loyalty = models.OneToOneField(
        "LevelLoyalty", null=True, on_delete=models.CASCADE, related_name='withdrawals')
    faster_withdrawal = models.CharField(max_length=50, null=True, blank=True)
    withdrawal_limits = models.CharField(max_length=50, null=True, blank=True)


class SpecialPrize(models.Model):
    level_loyalty = models.OneToOneField(
        "LevelLoyalty", null=True, on_delete=models.CASCADE, related_name='special_prize')
    freespins = models.IntegerField(null=True, blank=True)
    free_bet = models.CharField(max_length=100, null=True, blank=True)
    other = models.CharField(max_length=100, null=True, blank=True)


class Gifts(models.Model):
    level_loyalty = models.OneToOneField(
        "LevelLoyalty", null=True, on_delete=models.CASCADE, related_name='gifts')
    holiday = models.CharField(max_length=100, null=True, blank=True)
    birthday = models.CharField(max_length=100, null=True, blank=True)
    offline = models.CharField(max_length=100, null=True, blank=True)
    personalized = models.CharField(max_length=100, null=True, blank=True)
    exclusive = models.CharField(max_length=100, null=True, blank=True)


class LoyaltyBonus(models.Model):
    level_loyalty = models.OneToOneField(
        "LevelLoyalty", null=True, on_delete=models.CASCADE, related_name='loyalty_Bonus')
    real_money = models.CharField(max_length=100, null=True, blank=True)
    customized = models.CharField(max_length=100, null=True, blank=True)
    weekly = models.CharField(max_length=100, null=True, blank=True)
    monthly = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ["id"]
        verbose_name = "Bonuses"
        verbose_name_plural = "Bonuses"


# ==================================================================================================================== #
class LevelLoyalty(models.Model):
    program = models.ForeignKey("LoyaltyProgram", on_delete=models.CASCADE, null=True, related_name='level_loyalty')
    level = models.CharField(verbose_name="Level", max_length=30, null=True, blank=True)
    vip_manager_access = models.BooleanField(default=False)
    special_notes = models.TextField(verbose_name="Special Notes", null=True, blank=True)

    def __str__(self):
        return self.program.__str__()

# ==================================================================================================================== #

class LoyaltyProgram(models.Model):
    CHOICES_VIP_MANAGER = [('undefined', 'Undefined'), ('yes', 'Yes'), ('no', 'No')]

    casino = models.OneToOneField(
        Casino, on_delete=models.CASCADE, related_name='loyalty_program', null=True, default=None)
    link = models.URLField(verbose_name="Loyalty Url", null=True, blank=True)
    loyalty_understandable = models.TextField(verbose_name="Is this loyalty easy to understand", null=True, blank=True)
    vip_manager = models.CharField(max_length=10, choices=CHOICES_VIP_MANAGER, default='')
    loyalty_rank = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Loyalty Rank', null=True)

    def __str__(self):
        return f"Loyalty Program {self.casino.name}"

    # def clean(self):
    #     if self.vip_manager == 'undefined':
    #         raise ValidationError('Be sure to specify the vip-manager (Yes/No)')
