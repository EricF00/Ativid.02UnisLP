# -*- coding: latin1 -*-

#Função que receba uma frase como parâmetro e que retorne uma nova frase com cada palavra com as letras invertidas.
def invertText(text):
    invertedText = ""
    for palavra in text.split(" "):
        invertedText += palavra[::-1]+" "
    return invertedText

Text = input("Escreva uma frase que deseja inverter: ")
invertedText = invertText(Text)
print(invertedText)
