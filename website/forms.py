from django.forms import ModelForm
from django import forms
from .models import Contacto, Quizz, Comentario, Jogador


class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'id': forms.TextInput(),
            'nome': forms.TextInput(),
            'apelido': forms.TextInput(),
            'telefone': forms.TextInput(),
            'email': forms.EmailInput(attrs={'class': 'form-block', 'placeholder': 'abc@def.com'}),
            'data_de_nascimento': forms.DateInput(),
        }
        labels = {
            'id': 'Introduza o seu Username (Obrigatório para adicionar jogadores!):',
            'nome': 'Introduza o seu nome:',
            'apelido': 'Introduza o seu apelido:',
            'telefone': 'Introduza o seu telefone:',
            'email': 'Introduza o seu email:',
        }


class QuizzForm(ModelForm):
    class Meta:
        model = Quizz
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'contacto': forms.TextInput(),
            'nome': forms.TextInput(attrs={'placeholder': 'nome'}),
            'apelido': forms.TextInput(attrs={'placeholder': 'apelido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'abc@def.com'}),
            'p1': forms.RadioSelect(),
            'p2': forms.Select(),
            'p3': forms.TextInput(),
            'p4': forms.RadioSelect(),
            'p5': forms.Select(),
            'p6': forms.Select(),
            'p7': forms.NumberInput(attrs={'class': 'form-block', 'min': '0', 'max': '20'}),
            'p8': forms.TextInput(),
            'p9': forms.RadioSelect(),
            'p10': forms.NumberInput(),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'contacto': 'Introduza o seu Username (Obrigatório para adicionar quizz!):',
            'p1': 'Qual o clube com mais Champions League❓',
            'p2': 'Qual a actual função de Zinédine Zidane❓',
            'p3': '🗺Qual o actual clube de Lionel Messi❓',
            'p4': '👨‍👩‍👦‍👦Qual a capacidade do Estádio José Alvalade XXI(arredondado)❓',
            'p5': '⚽ Qual destes clubes é o mais antigo❓',
            'p6': 'ℹ️Qual destes jogadores ganhou a bola de ouro❓',
            'p7': '🔢Quantos troféus Champions League tem o Real Madrid(entre 0 e 20)❓',
            'p8': '🌍Qual o país natal de Cristiano Ronaldo❓',
            'p9': '❓Qual destes clubes é o "preferido" de CR7❓',
            'p10': 'Quantas bolas de ouro tem CR7❓',
        }


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'contacto': forms.TextInput(),
            'clareza': forms.RadioSelect(),
            'rigor': forms.RadioSelect(),
            'precisao': forms.RadioSelect(),
            'profundidade': forms.RadioSelect(),
            'amplitude': forms.RadioSelect(),
            'logica': forms.RadioSelect(),
            'significancia': forms.RadioSelect(),
            'originalidade': forms.RadioSelect(),
            'visual': forms.RadioSelect(),
            'geral': forms.RadioSelect(),
            'comment': forms.TextInput(),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'contacto': 'Introduza o seu Username (Obrigatório para adicionar comentario!):',
            'clareza': 'Como avalia o nível de clareza do website❓',
            'rigor': 'Como avalia o nível de rigor do website❓',
            'precisao': 'Como avalia o nível de precisão do website❓',
            'profundidade': 'Como avalia o nível de profundidade do website❓',
            'amplitude': 'Como avalia o nível de amplitude do website❓',
            'logica': 'Como avalia o nível de lógica do website❓',
            'significancia': 'Como avalia o nível de significância do website❓',
            'originalidade': 'Como avalia o nível de originalidade do website❓',
            'visual': 'Como avalia o nível visual do website❓',
            'geral': 'De uma forma geral, como avalia o website❓',
            'comment': 'Faça o seu comentário ao website:',
        }


class JogadorForm(ModelForm):
    class Meta:
        model = Jogador
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'contacto': forms.TextInput(),
            'nome': forms.TextInput(),
            'apelido': forms.TextInput(),
            'clube': forms.TextInput(),
        }
        labels = {
            'contacto': 'Introduza username previamente registrado em contactos:',
            'nome': 'Introduza o nome do Jogador:',
            'apelido': 'Introduza o apelido do Jogador:',
            'clube': 'Introduza o clube atual do Jogador:',
        }



