from django_select2.forms import Select2Widget
from django import forms

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
    class Meta:
        model = AccountData
        fields = ('log', 'password')
        widgets = {
            'password': forms.PasswordInput(),  # Добавляем виджет для скрытия пароля
        }

    def __init__(self, *args, **kwargs):
        print("\n\nINIT AccountDataForm !!!!")
        super(AccountDataForm, self).__init__(*args, **kwargs)
        # print(self.fields.items())
        for field_name, field in self.fields.items():
            field.required = True  # Устанавливаем поля как обязательные
