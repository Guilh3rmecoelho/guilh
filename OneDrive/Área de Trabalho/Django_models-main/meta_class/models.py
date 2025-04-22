from django.db import models
from django.contrib.auth.models import User



from django.db import models

# Importando a classe Categoria antes de usá-la
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)  # Referência tardia

    def __str__(self):
        return self.nome




class Cliente(models.Model):
    # Definição da lista de estados antes do campo
    ESTADOS_BRASILEIROS = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    # Relacionamento com o modelo User (autenticação do Django)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Campos de endereço e cidade
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    
    # Campo de estado com as opções definidas acima
    estado = models.CharField(max_length=2, choices=ESTADOS_BRASILEIROS)
    
    # Campo de CEP
    cep = models.CharField(max_length=9)

    def __str__(self):
        return self.user.get_full_name()
    
    

