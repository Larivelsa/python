### O que é o o Flask
- É um microfirmware (micro porque há apenas duas dependências instaladas) de Python para web
- As duas dependências são: Jinja (templates) e Werkzeug (ferramenta para server web)
- Jinja é um mecanismo de template em que usa-se marcadores parecidos com a sintaxe de Python e depois o template recebe dados para renderizar a página final. (fonte: https://jinja.palletsprojects.com/)

#### O que é WSGI - PEP 3333
WSGI é um acrônimo para Web Server Gateway Interface, trata-se de uma forma para servidores conversarem com frameworks, 
e vice-versa (fonte: http://devfuria.com.br/linux/instalando-apache-wsgi/). Os WSGI são apenas para Python (pelo menos até agora).
Outras linguagens de back-end usam outros gateway. Por exemplo, o PHP usa o FastCGI e o Perl usa o CGI para essa comunicação
com os servidores web.
O WSGI tem o objetivo de ser um interface simples e universal entre o web server API/frameworks web. 
Para que o WSGI funcione é necessário que os frameworks implementem isso. 

Numa aplicação web usando o WSGI tem-se os seguintes componentes:
- servidor WSGI
- servidor web (Apache, NGINX)
- web browser

1º o browser faz a requisição para o servidor web via HTTP

2º o servidor web passa essa requisição para o servidor WSGI

3º o servidor WSGI obtém a requisição e a envia para processamento na linguagem Python

4º o servidor WSGI devolve a resposta para o servidor web

5º finalmente, o servidor web envia a resposta ao cliente (browser)

Basicamente, a comunicação acontece deste modo:

##### cliente <---> web server <---> wsgi <---> python (é possível utilizar o wsgi sem frameworks)

ou

##### cliente <---> web server <---> wsgi <---> framework web python (flask, django, etc)


Servidores WSGI mais usados em Flask/Django:
- Green Unicorn qie é compatível com vários framework e é leve
- uWSGI
- mod_wsgi é um módulo do Apache que implementa o WSGI
- CherryPy

(fontes: https://medium.com/analytics-vidhya/what-is-wsgi-web-server-gateway-interface-ed2d290449e e https://www.python.org/dev/peps/pep-3333/)






