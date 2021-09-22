## Tutorial de instalação do ambiente virtual e do Flask no Windows
1 - instalar ambiente virtual (venv) com o comando: 
> pip install virtualenv

2 - criar diretório do projeto e trocar para o criado

3 - criar o ambiente virtual estando no diretório do projeto, usar o comando: 
> python -m venv <nome_ambiente_virtual>

(a opção -m venv executa o pacote venv da biblioteca padrão como um script independente, passando o nome desejado como argumento)

! importante ! caso apresente erro "[...] não pode ser carregado porque a execução de scripts foi desabilitada neste sistema.", execute o comando Set-ExecutionPolicy -Scope CurrentUse no PowerShell e defina como parâmetro de ExecutionPolicy que será solicitado logo em seguida como Unrestricted

4 - ativar o ambiente virtual executando o seguinte comando, no caminho da criação do ambiente criado: 
> <nome_ambiente_virtual>\Script\activate

5 - instalar o Flask estando com o ambiente virtual Python ativo (será possível visualizar o nome do ambiente virtual Python antes do diretório atual no promp de comando): 
> pip install flask
(o comando acima instala o Flask e suas dependências e para verificar usar o comando pip freeze)

6 - verificar se o Flask está instalado corretamente: 
> python
>>> import flask

#### Alguns porquês
- Um ambiente virtual é uma cópia do interpretador Python no qual você pode instalar pacotes em particular, sem afetar o interpretador global Python instalado em seu sistema. 

Fonte: https://www.alura.com.br/artigos/flask-instalacao. Acessado em 22 de Setembro de 2021

#### Resumo da ópera
- é importante a criação do ambiente virtual para que possamos manipular de forma controlada as variáveis de ambiente
- para ficar organizado, cria-se a o ambiente virtual dentro do diretório do projeto
- usando a venv criada, ativa-se ela e partir disso é só instalar o Flask
