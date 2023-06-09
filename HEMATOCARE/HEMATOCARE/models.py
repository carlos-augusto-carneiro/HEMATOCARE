from django.db import models

class PontoDeColeta(models.Model):
    CNPJ = models.CharField(primary_key=True, max_length=14)
    Email = models.CharField(max_length=100)
    Nome = models.CharField(max_length=100)
    Segmento = models.CharField(max_length=100)
    Logradouro = models.CharField(max_length=100)
    Numero = models.CharField(max_length=10)
    Bairro = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=100)
    CEP = models.CharField(max_length=8)

class Doador(models.Model):
    CPF = models.CharField(primary_key=True, max_length=11)
    Nome = models.CharField(max_length=100)
    Idade = models.IntegerField()
    Email = models.CharField(max_length=100)
    Logradouro = models.CharField(max_length=100)
    Numero = models.CharField(max_length=10)
    Bairro = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=100)
    CEP = models.CharField(max_length=8)
    Tipo_sanguineo = models.CharField(max_length=5)
    Senha = models.CharField(max_length=255)

class TelefoneDoador(models.Model):
    CPF = models.ForeignKey(Doador, on_delete=models.CASCADE)
    Numero = models.CharField(max_length=20, primary_key=True)

class BolsaDeSangue(models.Model):
    Codigo_bolsa_sangue = models.AutoField(primary_key=True)
    CPF = models.ForeignKey(Doador, on_delete=models.CASCADE)
    Data = models.DateField()
    CNPJ = models.ForeignKey(PontoDeColeta, on_delete=models.CASCADE)

class Hospital(models.Model):
    CNPJ = models.CharField(primary_key=True, max_length=14)
    Email = models.CharField(max_length=100)
    Nome = models.CharField(max_length=100)
    Logradouro = models.CharField(max_length=100)
    Numero = models.CharField(max_length=10)
    Bairro = models.CharField(max_length=100)
    Cidade = models.CharField(max_length=100)
    CEP = models.CharField(max_length=8)

class TelefoneHospital(models.Model):
    CNPJ = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    Numero = models.CharField(max_length=20, primary_key=True)

class Recebe(models.Model):
    CNPJ = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    Codigo_bolsa_sangue = models.ForeignKey(BolsaDeSangue, on_delete=models.CASCADE)
    Data = models.DateField()
    Hora = models.TimeField()

class TelefonePontoDeColeta(models.Model):
    CNPJ_Ponto_de_coleta = models.ForeignKey(PontoDeColeta, on_delete=models.CASCADE)
    Numero = models.CharField(max_length=20, primary_key=True)

class Funcionario(models.Model):
    Codigo_fun = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    CRM = models.CharField(max_length=20)
    COREN = models.CharField(max_length=20)

class Atender(models.Model):
    Codigo_fun = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    CPF_doador = models.ForeignKey(Doador, on_delete=models.CASCADE)

