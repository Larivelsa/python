### Tutorial de criação inicial de projeto Flask
Primeiro de tudo, o Flask é um microframework e não porque tem poucas utilidades, 
mas porque o programador tem maior controle do que vem por padrão, por exemplo.
Poucas dependências e melhor entendimento do que está sendo usado.

1. iniciamos importando a classe Flask no arquivo do projeto:
```from flask import Flask```. Aqui importamos apenas a classe Flask inicialmente porque é a partir do objeto obtido desta classe que a brincadeira começa.
Só com a classe Flask é possível criar rotas e botar para rodar o servidor.

2. agora é o momento de criarmos o objeto principal do projeto: ```app = Flask(__name__)```. O objeto é instanciado na variável app e a partir dela é possível criar rotas e usar o método run que sobe o servidor na porta, por padrão, 5000. É passado na classe o nome do módulo (no caso, será main, porque não é um módulo importado). Isso é importante porque é necessário informar ao Flask onde está a instância da classe criada (no caso, a variável é o objeto da classe Flask app). Resumindo, o objeto da classe precisa obter o pacote base a qual está vinculada.

3. criamos a rota: ```@app.route(<nome_da_rota>)```. Esse nome da rota é o caminho a partir do domínio (ou subdomínio). Por exemplo, se for digitado www.dominio.com.br/inicio e a rota estiver definida como /inicio em <nome_da_rota>. O símbolo @ indica que é um decorator. Um decorator é um padrão de projeto do Python (outras linguagens tb possuem este padrão de projeto). De acordo com o site Datacamp, o decorator serve para adicionar novas funcionalidades a um objeto já existente sem alterar sua estrutura. 


