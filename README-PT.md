Aplicação full stack criada para vender aplicações web. Feito usando o [template djavue](https://github.com/huogerac/djavue)
![imagem](https://user-images.githubusercontent.com/103211332/218487829-ffd39aed-4152-42f6-8543-68046177a560.png)

 
## Tecnologias de back-end:
 - Python
 - Django
 - Docker
 - Postgres
 - Flake8
 
## Tecnologias front-end:
 - Javascript
 - Visão 3
 - Vuetify 3
 - Nuxt
 - Eslint
 
## Recursos extras:
 - Modo escuro e claro
 
## Erros conhecidos:
 - O fluxo de login está sendo interrompido e é necessário logar novamente
 
## Requisitos:
- Node 14 instalado (digite `node -v` para ver a versão) e execute [vue-cli](https://cli.vuejs.org/)
- Docker & Docker compose instalado para carregar tudo muito rápido e não precisar instalar/configurar bibliotecas/ferramentas infinitas diretamente na sua máquina
 
## Como executar:
 - Construa com: ```docker compose build```
 - Execute com: ```docker compose```
 - Pronto, agora é só acessar ```localhost/```
  
## Como acessar o administrador do Django:
 - Com seu container em execução, execute em um terminal: ```docker exec -it "BACKEND_CONTAINER_ID" bash```
 - Para descobrir o ID do container de back-end, execute em um terminal: ```docker ps```
 - Dentro do bash do seu container, execute: ```./manage.py createsuperuser```
 - Acesse o endereço ```localhost/8000``` e faça login com os dados criados anteriormente
  
 ## Portas usadas:
 - Nginx: 80
 - Backend: 8000
 - Front-end: 3000
 - Postgres: 15432
 
 PREVIEW: em andamento