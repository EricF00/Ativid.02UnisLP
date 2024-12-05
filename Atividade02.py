# -*- coding: latin1 -*-

#Programa que lê 3 valores a,b,c e verifica se eles formam ou não um triângulo. Supor que os valores lidos são inteiros e positivos. Caso os valores formem um triângulo, calcular e escrever a área deste triângulo. Se não formam triângulo escrever os valores lidos. (Se a &gt; b + c não formam triângulo algum, se a é o maior).
import math

A  = float(input("Digite o valor A em cm: "))
B  = float(input("Digite o valor B em cm: "))
C  = float(input("Digite o valor C em cm: "))

if A > (B + C):
    print(f"Os valores {int(A)}, {int(B)}, {int(C)} não formam um triângulo!")
else:
    p = (A + B + C) / 2
    area = round(math.sqrt(p*(p-A)*(p-B)*(p-C)),2)
    print(f"A área é aproximadamente de {area}cm²")
