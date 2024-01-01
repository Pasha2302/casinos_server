from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django import forms

from app_casinos.all_models.models import Country


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

class BonusAdminForm(forms.ModelForm):
    """
    Если ModelForm будет использоваться только для администратора,
    самым простым решением будет опустить атрибут Meta.model,
    так как ModelAdmin предоставит правильную модель для использования.
    """
    pass


# ==================================================================================================================== #

class ModelDataValidationForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        check_initial = getattr(self, 'initial', None)
        print(f"\n\n{self=} / {type(self)=}\n{self.__dict__=}")
        print('==' * 60)
        print(f"{cleaned_data=}\n{type(cleaned_data)=}")
        print(f"\n{check_initial=}\n{type(check_initial)=}")

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
