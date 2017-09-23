from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model): #dfinisco da dove deriva il modello. in questo caso django di base
    author = models.ForeignKey('auth.User') #un post ha una proprietà legata all'utente
    title = models.CharField(max_length=200)
    text = models.TextField() #se so che un certo testo è limitato a una ceta lunghezza uso il chart
    created_date = models.DateTimeField(
            default=timezone.now) # di defaut mi mette la data attuale
    published_date = models.DateTimeField( #il published date, gli è consentito di essee vuoto
            blank=True, null=True) #la stessa cosa, ma blanck per l'admin(che puoi mettere vuoto) e null è per il bit
            #vuoto che può essere lasciato

#ora aggiungiamo cose alla classe
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #già definita in models.model ma la personalizzo
        return self.title #quando ti chiedo l'str dammi il titolo del post
