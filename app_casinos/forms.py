from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django import forms

from app_casinos.models.casino import Country, Casino, Game
from django.forms.models import ModelMultipleChoiceField
from django.core.exceptions import ValidationError



class CustomFilteredSelectMultipleSlots(FilteredSelectMultiple):
    def __init__(self, verbose_name, is_stacked, attrs=None, choices=()):
        super().__init__(verbose_name, is_stacked, attrs, choices)

    # def get_context(self, name, value, attrs):
    #     context = super().get_context(name, value, attrs)
    #     context['queryset'] = Game.objects.none()  # Предотвращаем загрузку данных из модели Game


class CustomModelMultipleChoiceFieldSlot(ModelMultipleChoiceField):
    def __init__(self, queryset, **kwargs):
        super().__init__(queryset, **kwargs)

    def _check_values(self, value):
        key = self.to_field_name or "pk"
        try:
            value = frozenset(value)
        except TypeError:
            raise ValidationError(
                self.error_messages["invalid_list"],
                code="invalid_list",
            )
        for pk in value:
            try:
                self.queryset.filter(**{key: pk})
            except (ValueError, TypeError):
                raise ValidationError(
                    self.error_messages["invalid_pk_value"],
                    code="invalid_pk_value",
                    params={"pk": pk},
                )
        # qs = self.queryset.filter(**{"%s__in" % key: value})
        qs = Game.objects.filter(**{"%s__in" % key: value})
        pks = {str(getattr(o, key)) for o in qs}
        # print("\n\nPKS:", pks)
        for val in value:
            # print('\nval:', val)
            if str(val) not in pks:
                raise ValidationError(
                    self.error_messages["invalid_choice"],
                    code="invalid_choice",
                    params={"value": val},
                )
        return qs


class SlotsWageringContributionInlineForm(forms.ModelForm):
    slot = CustomModelMultipleChoiceFieldSlot(
        # queryset=BonusRestrictionGame.objects.all(),
        queryset=Game.objects.none(),
        # queryset=kwargs.get('instance'),
        # widget=FilteredSelectMultiple("Game", is_stacked=False),
        widget=CustomFilteredSelectMultipleSlots("Slots", is_stacked=False),
        # widget=forms.SelectMultiple(attrs={'size': '10'})
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Получаем экземпляр бонуса
        self.bonus_instance = kwargs.get('instance')
        # Если бонус уже существует, получаем выбранные игры и устанавливаем их как выбранные в поле
        if self.bonus_instance:
            selected_slot = self.bonus_instance.slot.all()
            # queryset_all_game = Game.objects.none()
            self.fields['slot'].initial = [slot.pk for slot in selected_slot]
            self.fields['slot'].queryset = selected_slot

    def clean_game(self):
        print(f"\n\nclean_slot".capitalize(), '!!!')
        game = self.cleaned_data['slot']
        print(f"\nSlot data: {game}")
        print(f"\nself.fields['slot'].queryset: {self.fields['slot'].queryset}")
        # if game != self.fields['game'].queryset:
        #     raise forms.ValidationError("Invalid choice. Please select a valid game.")
        return game



# =================================================================================================================== #
# =================================================================================================================== #


class CustomFilteredSelectMultiple(FilteredSelectMultiple):
    def __init__(self, verbose_name, is_stacked, attrs=None, choices=()):
        super().__init__(verbose_name, is_stacked, attrs, choices)

    # def get_context(self, name, value, attrs):
    #     context = super().get_context(name, value, attrs)
    #     context['queryset'] = Game.objects.none()  # Предотвращаем загрузку данных из модели Game
    #     return context


class CustomModelMultipleChoiceField(ModelMultipleChoiceField):
    def __init__(self, queryset, **kwargs):
        super().__init__(queryset, **kwargs)

    def _check_values(self, value):
        key = self.to_field_name or "pk"
        try:
            value = frozenset(value)
        except TypeError:
            raise ValidationError(
                self.error_messages["invalid_list"],
                code="invalid_list",
            )
        for pk in value:
            try:
                self.queryset.filter(**{key: pk})
            except (ValueError, TypeError):
                raise ValidationError(
                    self.error_messages["invalid_pk_value"],
                    code="invalid_pk_value",
                    params={"pk": pk},
                )
        # qs = self.queryset.filter(**{"%s__in" % key: value})
        qs = Game.objects.filter(**{"%s__in" % key: value})
        pks = {str(getattr(o, key)) for o in qs}
        # print("\n\nPKS:", pks)
        for val in value:
            # print('\nval:', val)
            if str(val) not in pks:
                raise ValidationError(
                    self.error_messages["invalid_choice"],
                    code="invalid_choice",
                    params={"value": val},
                )
        return qs

class BonusRestrictionGameInlineForm(forms.ModelForm):
    game = CustomModelMultipleChoiceField(
        # queryset=BonusRestrictionGame.objects.all(),
        queryset=Game.objects.none(),
        # queryset=kwargs.get('instance'),
        # widget=FilteredSelectMultiple("Game", is_stacked=False),
        widget=CustomFilteredSelectMultiple("Game", is_stacked=False),
        # widget=forms.SelectMultiple(attrs={'size': '10'})
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Получаем экземпляр бонуса
        self.bonus_instance = kwargs.get('instance')
        # Если бонус уже существует, получаем выбранные игры и устанавливаем их как выбранные в поле
        if self.bonus_instance:
            selected_games = self.bonus_instance.game.all()
            # queryset_all_game = Game.objects.none()
            self.fields['game'].initial = [game.pk for game in selected_games]
            self.fields['game'].queryset = selected_games

    def clean_game(self):
        print(f"\n\nclean_game".capitalize(), '!!!')
        game = self.cleaned_data['game']
        print(f"\nGame data: {game}")
        print(f"\nself.fields['game'].queryset: {self.fields['game'].queryset}")
        # if game != self.fields['game'].queryset:
        #     raise forms.ValidationError("Invalid choice. Please select a valid game.")
        return game


class BonusAdminForm(forms.ModelForm):
    """
    Если ModelForm будет использоваться только для администратора,
    самым простым решением будет опустить атрибут Meta.model,
    так как ModelAdmin предоставит правильную модель для использования.
    """


class CasinoForm(forms.ModelForm):
    class Meta:
        model = Casino
        # fields = ['title', 'authors', 'publisher']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control custom-form-control'})


class  PromotionPeriodForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if (start_date and not end_date) or (end_date and not start_date):
            raise forms.ValidationError("Both start date and end date are required if one is filled.")

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("End date cannot be earlier than start date.")

# ==================================================================================================================== #
class NoClearableFileInput(forms.ClearableFileInput):
    clear_checkbox_label = ''  # Устанавливаем пустую строку, чтобы не отображать чекбокс "Clear"


class RichTextEditorWidget(forms.Textarea):
    def render(self, name, value, attrs=None, renderer=None):
        print(f"\n\n[forms.Textarea <render>] params:{name=}\n{value=}\n{attrs=}\n{renderer=}\n{'--' * 60}")
        # Код для генерации HTML-разметки виджета
        # В данном примере, оборачиваем тег <textarea> блоком <div> со стилями:
        output_render = super().render(name, value, attrs, renderer)
        print(f"\n\nRender Text Area: {output_render}\nType output_render: {type(output_render)}\n")
        return mark_safe(
            f'<div style="border: 1px solid #ccc; padding: 5px; background-color: #eaeae6;">{output_render}</div>'
        )


# ==================================================================================================================== #
class CountryDataValidationForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        check_initial = getattr(self, 'initial', None)
        if not check_initial and cleaned_data.get('name'):
            slug = slugify(cleaned_data['name'])
            if Country.objects.filter(slug=slug).exists():
                raise forms.ValidationError({'name': "Record with this name already exists"})

        return cleaned_data

# ==================================================================================================================== #

class AccountDataForm(forms.ModelForm):
    count = 0
    print("\nClass Account Data Form <<===")

    def __init__(self, *args, **kwargs):
        super(AccountDataForm, self).__init__(*args, **kwargs)
        # print("\n\nINIT AccountDataForm !!!!")
        # print("\nFields Dict:", self.fields)
        # print('==' * 60)

        self.fields['password'].empty_value = "Enter your password"
        # print(f"{type(self.fields['password'])} | password:")
        # pprint(self.fields['password'].__dict__)
        # print('--' * 50)
        # print(f"{type(self.fields['login'])} | login:")
        # pprint(self.fields['login'].__dict__)


# {'max_length': 15, 'min_length': None, 'strip': True, 'empty_value': '',
# 'required': True, 'label': 'Password', 'initial': None, 'show_hidden_initial': False,
# 'help_text': '', 'disabled': False, 'label_suffix': None, 'localize': False,
# 'widget': <django.forms.widgets.PasswordInput object at 0x7f5253fe0be0>,
# 'error_messages': {'required': 'This field is required.'},
# 'validators': [<django.core.validators.MaxLengthValidator object at 0x7f5254332ef0>,
# <django.core.validators.ProhibitNullCharactersValidator object at 0x7f5254332ec0>],
# 'template_name': None}
