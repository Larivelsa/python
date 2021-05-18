'''
Henrique, mesmo dando os primeiros passos com a linguagem Python, 
decidiu criar um sistema de identificação de usuários. 
É claro que em uma aplicação real é necessário acessar o banco de 
dados, entre outras coisas, mas usando o que ele já aprendeu, 
ele conseguiu algo parecido. Esse é o código do aluno.
A ideia de Henrique é simples, porém não muito eficiente. 
Ele quer aceitar apenas os usuários Flávio, Douglas e Nico. 
No entanto, seu código não funciona!
'''

usuario = input("Informe o usuário do sistema: ")

autenticado = usuario == "Flávio" or usuario == "Douglas" or usuario == "Nico"

if(autenticado):
    print(f"Seja bem-vindo {usuario}!")
else:
    print("Usuário não identificado!")
