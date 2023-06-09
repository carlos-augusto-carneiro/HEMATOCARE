from django import forms
from .models import PontoDeColeta, Doador, TelefoneDoador, BolsaDeSangue, Hospital, TelefoneHospital, Recebe, TelefonePontoDeColeta, Funcionario, Atender

# Formulários para PontoDeColeta
class PontoDeColetaForm(forms.ModelForm):
    class Meta:
        model = PontoDeColeta
        fields = '__all__'

class DoadorForm(forms.ModelForm):
    class Meta:
        model = Doador
        fields = '__all__'

class TelefoneDoadorForm(forms.ModelForm):
    class Meta:
        model = TelefoneDoador
        fields = '__all__'

class BolsaDeSangueForm(forms.ModelForm):
    class Meta:
        model = BolsaDeSangue
        fields = '__all__'

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

class TelefoneHospitalForm(forms.ModelForm):
    class Meta:
        model = TelefoneHospital
        fields = '__all__'

class RecebeForm(forms.ModelForm):
    class Meta:
        model = Recebe
        fields = '__all__'

class TelefonePontoDeColetaForm(forms.ModelForm):
    class Meta:
        model = TelefonePontoDeColeta
        fields = '__all__'

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

class AtenderForm(forms.ModelForm):
    class Meta:
        model = Atender
        fields = '__all__'

# Continue com os formulários para as outras tabelas...

