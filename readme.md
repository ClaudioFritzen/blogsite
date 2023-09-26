## https://bulma.io/documentation/overview/start/


crie o ambiente virtual

    instale o django

crie um projeto django  
        django-admin startproject nome .

configure as variaveis de ambientação

º Crie um app django
    py manage.py startapp nome
    crie uma pasta chamada templates 
    e dentro uma chamada o nome do app

º coloque o app em install apps no settings.py 

##########
# Criando as models
 class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

## py manage.py makemigrations
## py manage.py migrate

# Cadrastre na are Administrativa


#### manuntencão das minhas ideias 

Para criarmos um post, devemos passar as seguintes informações 

titilo

# slug
    # no slug quero criar uma função que pega o titulo, e remove espaçoes em brancos e substituiu por underscore! ou hifen

intro
body


## Para criamos um novo post
 devemos criar um formulario para o utilizador 
 preenche-lo





 ## deploy com o railways

 # links de referencias
https://fly.io/
https://fly.io/docs/django/getting-started/existing/


## para se conectar ao banco utilizamos apenas 
pip install dj-database-url

pip install psycopg2-binary

pip install psycopg2


faremos a importação no settings

import dj_database_url


paremos o conector

DATABASE_URL = os.getenv('DATABASE_URL')

DATABASE_URL = os.getenv('DATABASE_URL')
DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL)

}
