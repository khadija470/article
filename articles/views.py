from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, redirect, render
from articles.forms import ArticleForm
from articles.models import Article
# Create your views here.

def home(request):
    articles = Article.objects.all()
    return render(request,"index.html",{"articles":articles})

# def useradmin(request):
#     form = ArticleForm()
#     return render(request,"useradmin.html",{'form':form})

def useradmin(request):
    articles = Article.objects.all()
    if request.method == 'POST':
       form = ArticleForm(request.POST,request.FILES)
       if form.is_valid():
           article = form.save(commit=False)
           article.auteur = request.user
           article.save()
        #    messages.success(request,'Article ajoute avec succes!')
           return redirect('useradmin')
    else:
           form = ArticleForm()
    return render(request,"useradmin.html",{'form':form,'articles':articles})

def modifier_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('useradmin')
    else:
        form = ArticleForm(instance=article)
    
    return render(request, 'modifier_article.html', {'form': form, 'article': article})

def supprimer_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('useradmin')

    # auteur = request.user 
    # titre = request.POST['titre']
    # contenu = request.POST['contenu']
    # resume = request.POST['resume']
    # if titre and contenu and resume:
    #   article = Article.objects.create(auteur = auteur,titre = titre,resume = resume,contenu = contenu)
    #   article.save()
    #   return redirect('ajouter_article')
  
    # else:
    #     messages.error(request,'Tous les champs doivent etre remplis') 
