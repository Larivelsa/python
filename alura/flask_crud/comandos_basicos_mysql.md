### Conectar no servidor usando um prompt (Windows ou Linux):
mysql -u root -p
onde -u indica que o parâmentro seguinte é o nome do usuário(root) e -p é de password que será digitado em seguida

### Mostra bases de dados no servidor MySQL:
SHOW DATABASES;

### Exibir usuário do server MySQL:
SELECT user FROM mysql.user;

### Exibir usuário server MySQL, caso haja duplicidade:
SELECT user,host FROM mysql.user;

### Exibir permissões do usuário logado em uso:
SHOW GRANTS FOR CURRENT_USER;

### Selecionar banco de dados:
USE nome-da-base-de-dados;

### Exibir tabelas do banco de dados:
Após selecionar a base de dados com o comando MySQL: USE <nome-da-base-de-dados>, use o comando:
SHOW tables;