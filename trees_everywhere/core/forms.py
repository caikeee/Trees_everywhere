from django import forms
from .models import PlantedTree, Tree, Account

class PlantTreeForm(forms.ModelForm):
    # Dropdown para selecionar o tipo de árvore, estilizado com o CSS do Bootstrap
    tree = forms.ModelChoiceField(
        queryset=Tree.objects.all(),  # Queryset para popular o dropdown com as árvores disponíveis
        label='Árvore',  # Rótulo para o campo
        widget=forms.Select(attrs={'class': 'form-control'})  # Adiciona uma classe CSS para estilizar o campo
    )

    # Dropdown para selecionar a conta (opcional, dependendo da configuração do seu modelo)
    account = forms.ModelChoiceField(
        queryset=Account.objects.all(),  # Popula com as contas disponíveis
        label='Conta',  # Rótulo para o campo de conta
        widget=forms.Select(attrs={'class': 'form-control'}),  # Adiciona uma classe CSS para estilizar o campo
        required=False  # Torna o campo opcional, se necessário, altere para True para tornar obrigatório
    )

    # Classe Meta para definir o modelo e os campos usados no formulário
    class Meta:
        model = PlantedTree  # Modelo associado a este formulário
        fields = ['tree', 'age', 'location_lat', 'location_long', 'account']  # Campos exibidos no formulário





class AccountForm(forms.ModelForm):
    # O campo 'name' é obrigatório, e o campo 'active' pode ser opcional
    class Meta:
        model = Account  # Modelo associado ao formulário
        fields = ['name', 'active']  # Campos que aparecerão no formulário

    # Adicionando um campo customizado ou método se precisar de validações extras
    def clean_name(self):
        name = self.cleaned_data.get('name')
        # Validação adicional, por exemplo, verificar se o nome já existe
        if Account.objects.filter(name=name).exists():
            raise forms.ValidationError("Já existe uma conta com esse nome.")
        return name