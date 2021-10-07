### Tutorial de criação inicial de projeto Flask
Primeiro de tudo, o Flask é um microframework e não porque tem poucas utilidades, 
mas porque o programador tem maior controle do que vem por padrão, por exemplo.
Poucas dependências e melhor entendimento do que está sendo usado.

1. iniciamos importando a classe Flask no arquivo do projeto:
```from flask import Flask```. Aqui importamos apenas a classe Flask inicialmente porque é a partir do objeto obtido desta classe que a brincadeira começa.
Só com a classe Flask é possível criar rotas e botar para rodar o servidor.

2. agora é o momento de criarmos o objeto principal do projeto: ```app = Flask(__name__)```. O objeto é instanciado na variável app e a partir dela é possível criar rotas e usar o método run que sobe o servidor na porta, por padrão, 5000. É passado na classe o nome do módulo (no caso, será main, porque não é um módulo importado). Isso é importante porque é necessário informar ao Flask onde está a instância da classe criada (no caso, a variável é o objeto da classe Flask app). Resumindo, o objeto da classe precisa obter o pacote base a qual está vinculada.

3. criamos a rota: ```@app.route(<nome_da_rota>)```. Esse nome da rota é o caminho a partir do domínio (ou subdomínio). Por exemplo, se for digitado www.dominio.com.br/inicio e a rota estiver definida como /inicio em <nome_da_rota>, será acionado o que estiver indicado no parâmetro. O símbolo @ indica que é um decorator. Um decorator é um padrão de projeto do Python (outras linguagens tb possuem este padrão de projeto). De acordo com o site Datacamp, o decorator serve para adicionar novas funcionalidades a um objeto já existente sem alterar sua estrutura. O método route da classe Flask recebe como parâmetro um rule, que é a URL no formato de string. É possível passar como parâmetros mais opções. Vejamos mais adiante. Logo abaixo da função de rota decorada, declaramos a função respectiva da URL. Essa função fica no mesmo nível de identação da função decorada. Aqui na rota cabe tudo que irá na página, é a construção da página. Aqui que o Jinja é importante. 

4. depois de criar a rota, é botar o servidor para rodar usando o método run. Isso fará com que o servidor suba e assim podemos acessá-lo pelo browser. A porta padrão é 5000. É possível alterar usando os parâmetros, por exemplo: app.run(host='0.0.0.0', port=8080). E quem faz este serviço de gerenciar o servidor é o Werkzeug (emborpa tb o Python por si só consiga subir o servidor, mas seria trabalhoso definir toda configuração...). Até agora, foi o básico para fazer com que o Flask demonstre algo.

5. criar o diretório templates para lidar com as páginas.

