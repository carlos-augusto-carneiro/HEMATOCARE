from django.shortcuts import render, get_object_or_404, redirect
from .models import PontoDeColeta, Doador, TelefoneDoador, BolsaDeSangue, Hospital, TelefoneHospital, Recebe, TelefonePontoDeColeta, Funcionario, Atender
from .forms import PontoDeColetaForm, DoadorForm, TelefoneDoadorForm, BolsaDeSangueForm, HospitalForm, TelefoneHospitalForm, RecebeForm, TelefonePontoDeColetaForm, FuncionarioForm, AtenderForm

# Funções de visualização para PontoDeColeta
def ponto_de_coleta_list(request):
    pontos_de_coleta = PontoDeColeta.objects.all()
    return render(request, 'crud/ponto_de_coleta_list.html', {'pontos_de_coleta': pontos_de_coleta})

def ponto_de_coleta_detail(request, cnpj):
    ponto_de_coleta = get_object_or_404(PontoDeColeta, CNPJ=cnpj)
    return render(request, 'crud/ponto_de_coleta_detail.html', {'ponto_de_coleta': ponto_de_coleta})

def ponto_de_coleta_create(request):
    if request.method == 'POST':
        form = PontoDeColetaForm(request.POST)
        if form.is_valid():
            ponto_de_coleta = form.save()
            return redirect('ponto_de_coleta_detail', cnpj=ponto_de_coleta.CNPJ)
    else:
        form = PontoDeColetaForm()
    return render(request, 'crud/ponto_de_coleta_form.html', {'form': form})

def ponto_de_coleta_update(request, cnpj):
    ponto_de_coleta = get_object_or_404(PontoDeColeta, CNPJ=cnpj)
    if request.method == 'POST':
        form = PontoDeColetaForm(request.POST, instance=ponto_de_coleta)
        if form.is_valid():
            ponto_de_coleta = form.save()
            return redirect('ponto_de_coleta_detail', cnpj=ponto_de_coleta.CNPJ)
    else:
        form = PontoDeColetaForm(instance=ponto_de_coleta)
    return render(request, 'crud/ponto_de_coleta_form.html', {'form': form})

def ponto_de_coleta_delete(request, cnpj):
    ponto_de_coleta = get_object_or_404(PontoDeColeta, CNPJ=cnpj)
    ponto_de_coleta.delete()
    return redirect('ponto_de_coleta_list')

# Funções de visualização para Doador
def doador_list(request):
    doadores = Doador.objects.all()
    return render(request, 'crud/doador_list.html', {'doadores': doadores})

def doador_detail(request, cpf):
    doador = get_object_or_404(Doador, CPF=cpf)
    return render(request, 'crud/doador_detail.html', {'doador': doador})

def doador_create(request):
    if request.method == 'POST':
        form = DoadorForm(request.POST)
        if form.is_valid():
            doador = form.save()
            return redirect('doador_detail', cpf=doador.CPF)
    else:
        form = DoadorForm()
    return render(request, 'crud/doador_form.html', {'form': form})

def doador_update(request, cpf):
    doador = get_object_or_404(Doador, CPF=cpf)
    if request.method == 'POST':
        form = DoadorForm(request.POST, instance=doador)
        if form.is_valid():
            doador = form.save()
            return redirect('doador_detail', cpf=doador.CPF)
    else:
        form = DoadorForm(instance=doador)
    return render(request, 'crud/doador_form.html', {'form': form})

def doador_delete(request, cpf):
    doador = get_object_or_404(Doador, CPF=cpf)
    doador.delete()
    return redirect('doador_list')

# Continue com as funções de visualização para as outras tabelas...

