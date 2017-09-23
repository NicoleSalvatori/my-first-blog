from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    #estrazione dati (query) dai post
    #lte di plublish zone sta per less than equal
    #metto - davanti a publish date per invertire l'ordine ed ordinarli dal più recente al meno
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
