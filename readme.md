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


