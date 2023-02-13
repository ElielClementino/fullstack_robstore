# RobStore - fullstack application

Full stack application created for selling web applications. Made using the [djavue template](https://github.com/huogerac/djavue)
![image](https://user-images.githubusercontent.com/103211332/218487829-ffd39aed-4152-42f6-8543-68046177a560.png)

 
## Backend technologies:
 - Python
 - Django
 - Docker
 - Postgres database
 - Flake8
 
## Frontend technologies:
 - Javascript
 - Vue 3
 - Vuetify 3
 - Nuxt
 - Eslint
 
## Extra features:
 - Dark and light mode
 
## Known bugs:
 - Login flow is breaking and need to hit login again
 
## Requirements:
- Node 14 installed (type `node -v` to see the version) and and get [vue-cli](https://cli.vuejs.org/) running
- Docker & Docker compose installed to upload everything very fast and not need to install/configure infinite libs/tools directly on your machine
 
## How to run:
 - Build with: ```docker compose build```
 - Run  with: ```docker compose up```
 - Ready, now just access ```localhost/```
  
## How to acess django admin:
 - With your container running, run in a terminal: ```docker exec -it "BACKEND_CONTAINER_ID" bash```
 - To find out your backend container ID, run in a terminal: ```docker ps```
 - Inside your container's bash, run: ```./manage.py createsuperuser```
 - Access the address ```localhost/8000``` and log in with the logins created previously
  
 ## Used ports:
 - Nginx: 80
 - Backend: 8000
 - Frontend: 3000
 - Postgres: 15432
 
PREVIEW WEBSITE: in progress
[PRESENTATION VIDEO](https://www.loom.com/share/d891410189994a679f8bfbb65bf5e820)
