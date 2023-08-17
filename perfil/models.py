from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)  # colunas - definir tipo de informação (tipo de dados)
    essencial = models.BooleanField(default=False)  # booleano para definir se é obrigatório informar aquele dado
    valor_planejamento = models.FloatField(default=0)

    def __str__(self):
        return self.categoria

class Conta(models.Model):
    banco_choices = (  # criando uma tupla com as opções para o usuário escolher seu banco
        ('NU', 'Nubank'),
        ('CE', 'Caixa Econômica'),
    )
    tipo_choices = (
        ('pf', 'Pessoa Física'),
        ('pj', 'Pessoa Jurídica')
    )

    apelido = models.CharField(max_length=50)
    banco = models.CharField(max_length=2, choices=banco_choices)  # as opções pela sigla, para não deixar livre ao usuário escrever qualquer coisa
    tipo = models.CharField(max_length=2, choices=tipo_choices)
    valor = models.FloatField()
    icone = models.ImageField(upload_to='icones')  # indicando em qual pasta as imagens serão armazenadas, dentro da pasta já indicada no settings

    def __str__(self):
        return self.apelido
