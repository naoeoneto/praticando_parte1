# main.py
from operacoes_matematicas.soma import somar  # Novo
from operacoes_matematicas.subtracao import subtrair  # Novo
from operacoes_matematicas.multiplicacao import multiplicar

resultado_da_soma = somar(15, 7)
print(resultado_da_soma)
# 22

resultado_da_subtracao = subtrair(15, 7)
print(resultado_da_subtracao)
# 8

resultado_da_multiplicacao = multiplicar(4, 5)
print(resultado_da_multiplicacao)
# 20
