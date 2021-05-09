PALAVRAS_PROIBIDAS = ('futebol','religião','política')

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]


for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print (palavra)
            print(f'Texto possui pelo menos uma palavra proibida: {palavra}')
            found = True
            break
    else:
        print(f'Texto autorizado: {texto}')
            


            