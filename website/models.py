from django.db import models
from django.db.models import Model



def options():
    return [('1', 'Juventus🏳️'), ('2', 'Real Madrid🏳️'), ('3', 'M. United🏳️')], \
           [('1', 'Jogador'), ('2', 'Treinador')], \
           [('1', '30000'), ('2', '40000'), ('3', '50000')], \
           [('1', 'Real Madrid'), ('2', 'Sporting'), ('3', 'M.United'), ('4', 'Juventus')], \
           [('1', 'Rui Costa'), ('2', 'S. Conceição'), ('3', 'Luís Figo')], \
           [('1', 'Sporting'), ('2', 'Benfica'), ('3', 'Porto')], \
           [('1', 'Mau'), ('2', 'Razoavel'), ('3', 'Bom'), ('4', 'Excelente')]


class Contacto(models.Model):
    id = models.CharField(primary_key=True, max_length=30, unique=True, null=False, blank=False, default='Obrigatorio')
    nome = models.CharField(max_length=30, blank=False, default='Obrigatorio')
    apelido = models.CharField(max_length=30, blank=False, default='Obrigatorio')
    telefone = models.IntegerField()
    email = models.CharField(max_length=30, blank=False, default='Obrigatorio')

    def __str__(self):
        return self.nome[:15]

class Quizz(models.Model):
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE, blank=False, default='Obrigatorio')
    nome = models.CharField(max_length=30, null=False)
    apelido = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=50, null=True)
    p1 = models.CharField(max_length=1, choices=options()[0], default='0')
    p2 = models.CharField(max_length=1, choices=options()[1], blank=True, default='0')
    p3 = models.CharField(max_length=22, null=True)
    p4 = models.CharField(max_length=1, choices=options()[2], default='0')
    p5 = models.CharField(max_length=1, choices=options()[3], blank=True, default='0')
    p6 = models.CharField(max_length=1, choices=options()[4], blank=True, default='0')
    p7 = models.IntegerField(default=0)
    p8 = models.TextField(max_length=10, null=True)
    p9 = models.CharField(max_length=1, choices=options()[5], default='0')
    p10 = models.IntegerField(default=0)


class Comentario(models.Model):
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE, blank=False, default='Obrigatorio')
    clareza = models.CharField(max_length=1, choices=options()[6], default='Unspecified')
    rigor = models.CharField(max_length=1, choices=options()[6], default='Unspecified')
    precisao = models.CharField(max_length=1, choices=options()[6], default='Unspecified')
    profundidade = models.CharField(max_length=1, choices=options()[6], default='Unspecified')
    amplitude = models.CharField(max_length=1, choices=options()[6], default='Unspecified')
    logica = models.CharField(max_length=1, choices=options()[6], default='Unspecified')
    significancia = models.CharField(max_length=1, choices=options()[6], default='Unspecified')
    originalidade = models.CharField(max_length=1, choices=options()[6], default='Unspecified')
    visual = models.CharField(max_length=1, choices=options()[6], default='Unspecified')
    geral = models.CharField(max_length=1, choices=options()[6], default='Unspecified')
    comment = models.CharField(max_length=100, blank=True, default='Comente aqui!')


class Jogador(models.Model):
    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE, blank=False, default='Obrigatorio')
    nome = models.CharField(max_length=15, blank=False, default='Obrigatorio')
    apelido = models.CharField(max_length=15, blank=False, default='Obrigatorio')
    clube = models.CharField(max_length=50, blank=False, default='Obrigatorio')

    def __str__(self):
        return self.nome[:15]


# Create your models here.
