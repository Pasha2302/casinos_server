from django_select2.forms import Select2Widget
from django import forms
from pprint import pprint

from app_casinos.models import Casino, AffiliatesProgram, MinDep, BaseCurrency, AccountData


class NoClearableFileInput(forms.ClearableFileInput):
    clear_checkbox_label = ''  # Устанавливаем пустую строку, чтобы не отображать чекбокс "Clear"


class FilterAffiliateProgramAdminForm(forms.ModelForm):
    class Meta:
        model = Casino
        fields = ['affiliate_program']

    affiliate_program = forms.ModelChoiceField(
        queryset=AffiliatesProgram.objects.all(),
        widget=Select2Widget(),
        required=False,
    )

class FilterMinDepAdminForm(forms.ModelForm):
    class Meta:
        model = MinDep
        fields = ['symbol']

    symbol = forms.ModelChoiceField(
        queryset=BaseCurrency.objects.all(),
        widget=Select2Widget(),
        # required=False,
    )

# ==================================================================================================================== #
class AccountDataForm(forms.ModelForm):
    count = 0
    print("\nClass Account Data Form <<===")
    class Meta:
        model = AccountData
        fields = ('login', 'password')
        # widgets = {
        #     'password': forms.PasswordInput(),  # Добавляем виджет для скрытия пароля
        # }

    def __init__(self, *args, **kwargs):
        print("\n\nINIT AccountDataForm !!!!")
        super(AccountDataForm, self).__init__(*args, **kwargs)
        print("\nFields Dict:", self.fields)
        print('==' * 60)

        self.fields['password'].empty_value = "Enter your password"
        print(f"{type(self.fields['password'])} | password:")
        pprint(self.fields['password'].__dict__)
        print('--' * 50)
        print(f"{type(self.fields['login'])} | login:")
        pprint(self.fields['login'].__dict__)


# {'max_length': 15, 'min_length': None, 'strip': True, 'empty_value': '',
# 'required': True, 'label': 'Password', 'initial': None, 'show_hidden_initial': False,
# 'help_text': '', 'disabled': False, 'label_suffix': None, 'localize': False,
# 'widget': <django.forms.widgets.PasswordInput object at 0x7f5253fe0be0>,
# 'error_messages': {'required': 'This field is required.'},
# 'validators': [<django.core.validators.MaxLengthValidator object at 0x7f5254332ef0>,
# <django.core.validators.ProhibitNullCharactersValidator object at 0x7f5254332ec0>],
# 'template_name': None}
