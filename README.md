## Configurando ambiente ##

#### Clonar repositório do projeto ####

```bash

git clone https://github.com/juniozguedes/django_music.git

```


#### Subindo imagem Docker:

  

```bash

sudo docker-compose up --build

```

  

#### Rodando Migrations

Para rodar as migrations abaixo abra um novo terminal ou encerre processo do docker/django no terminal atual em que foi montada a imagem Docker (CTRL+C) 

```bash
sudo docker-compose run web python manage.py makemigrations
sudo docker-compose run web python manage.py migrate

sudo docker-compose up -d --build

```
  <h4><i>A aplicação rodará em:</i> http://localhost:8000/</h4>


## Rotas
<h3> A api servirá um json a fim de alimentar o frontend em React sempre que for chamada.</h3>
<p>A idéia é servir um quiz a cada requisição para que o React sirva a aplicação final.</p>

### Quiz

* Rota para servir o quiz, pode ser executada no navegador ex.: <strong>http://localhost:8000/quiz/1</strong>

Método | URI | Params | Descrição | Ex.:
--- | --- | --- | --- | ---
*GET* | `http://localhost:8000/quiz/{{quiz_id}}` | **quiz_id** | Retorna quiz por id | `http://localhost:8000/quiz/1`


## Features

-  [Docker](https://www.docker.com/docker-community)

-  [PostgreSQL](https://www.postgresql.org/)

-  [Django](https://www.djangoproject.com/)

## Requerimentos
-  [Docker](https://www.docker.com/)

## Suporte
  
Desenvolvido por wellington.junior@oglobo.com.br - @Infoglobo)