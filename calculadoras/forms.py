from django import forms

class CalculadoraFinanceiraForm(forms.Form):
    receitas = forms.FloatField(label='Receitas')
    despesas = forms.FloatField(label='Despesas')
    ativo = forms.FloatField(label='Ativo')
    passivo = forms.FloatField(label='Passivo')
    estoque_inicial = forms.FloatField(label='Estoque Inicial')
    compras = forms.FloatField(label='Compras')
    estoque_final = forms.FloatField(label='Estoque Final')

class CalculadoraTrabalhistaForm(forms.Form):
    salario = forms.FloatField(label='Salário Mensal')
    meses_trabalhados = forms.IntegerField(label='Meses Trabalhados')
    tipo_demissao = forms.ChoiceField(
        choices=[
            ('justa', 'Justa Causa'),
            ('sem_justa', 'Sem Justa Causa'),
            ('acordo', 'Acordo entre as partes')
        ],
        label='Tipo de Demissão'
    )
