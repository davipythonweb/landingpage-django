from django.shortcuts import render
from .forms import CalculadoraFinanceiraForm, CalculadoraTrabalhistaForm
import os
from datetime import datetime
from django.conf import settings

def index(request):
    return render(request, 'calculadoras/index.html')

    
def salvar_resultado_txt(nome, conteudo):
    caminho = os.path.join(settings.BASE_DIR, 'resultados_calculos', f'{nome}_{datetime.now().strftime("%Y%m%d%H%M%S")}.txt')
    with open(caminho, 'w') as f:
        f.write(conteudo)

def calculadoras(request):
    resultado_financeira = None
    resultado_trabalhista = None

    if request.method == 'POST':
        if 'calcular_financeira' in request.POST:
            form_financeira = CalculadoraFinanceiraForm(request.POST)
            form_trabalhista = CalculadoraTrabalhistaForm()
            if form_financeira.is_valid():
                r = form_financeira.cleaned_data
                lucro = r['receitas'] - r['despesas']
                pl = r['ativo'] - r['passivo']
                cmv = r['estoque_inicial'] + r['compras'] - r['estoque_final']
                dre = f"""
                DRE:
                Receita: {r['receitas']}
                (-) Despesas: {r['despesas']}
                (=) Lucro: {lucro}
                CMV: {cmv}
                LAIR: {lucro - cmv}
                """
                resultado_financeira = f"Lucro: {lucro}\nPL: {pl}\nCMV: {cmv}\n{dre}"
                salvar_resultado_txt("calculadora_financeira", resultado_financeira)

        elif 'calcular_trabalhista' in request.POST:
            form_trabalhista = CalculadoraTrabalhistaForm(request.POST)
            form_financeira = CalculadoraFinanceiraForm()
            if form_trabalhista.is_valid():
                r = form_trabalhista.cleaned_data
                fgts = r['salario'] * r['meses_trabalhados'] * 0.08
                tipo = r['tipo_demissao']
                if tipo == 'justa':
                    total = 0
                elif tipo == 'sem_justa':
                    total = r['salario'] * r['meses_trabalhados'] + fgts + fgts * 0.4
                else:  # acordo
                    total = r['salario'] * r['meses_trabalhados'] + fgts + fgts * 0.2
                resultado_trabalhista = f"""
                Salário: {r['salario']}
                Meses Trabalhados: {r['meses_trabalhados']}
                FGTS: {fgts:.2f}
                Tipo de Demissão: {tipo}
                Total a receber: R$ {total:.2f}
                """
                salvar_resultado_txt("calculadora_trabalhista", resultado_trabalhista)

    else:
        form_financeira = CalculadoraFinanceiraForm()
        form_trabalhista = CalculadoraTrabalhistaForm()

    return render(request, 'calculadoras/calculadoras.html', {
        'form_financeira': form_financeira,
        'form_trabalhista': form_trabalhista,
        'resultado_financeira': resultado_financeira,
        'resultado_trabalhista': resultado_trabalhista
    })
