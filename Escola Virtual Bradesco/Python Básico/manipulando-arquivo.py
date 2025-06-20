arquivo = open('arquivo.txt', 'w')
arquivo.write('Primeira linha do arquivo\n')
arquivo.write('Segunda linha do arquivo\n')
arquivo.close()

# Lendo o arquivo
arquivo = open('arquivo.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
# Fechando o arquivo
arquivo.close()
# Adicionando mais conteúdo ao arquivo 
arquivo = open('arquivo.txt', 'a')
arquivo.write('Terceira linha do arquivo\n')
# Fechando o arquivo novamente
arquivo.close()
# Lendo o arquivo novamente para verificar as alterações
arquivo = open('arquivo.txt', 'r')
conteudo = arquivo.read()
print(conteudo)
# Fechando o arquivo
arquivo.close()