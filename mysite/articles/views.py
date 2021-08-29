from django.shortcuts import render, redirect, HttpResponse, get_object_or_404,reverse
from .models import Article, Comment
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle
# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles.html', {'articles': articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    article = Article.objects.get(slug=slug)
    comments = article.comments.all()
    return render(request, 'articles/article_detail.html', {'article': article, "comments":comments })


def about_article(request):
    return render(request, 'about.html')

@login_required(login_url = "user:login")
def deleteArticle(request,slug):
    article = get_object_or_404(Article,slug=slug)
    article.delete()
    messages.success(request,"Article Successfully Deleted")
    return redirect("article:dashboard")

@login_required(login_url = "user:login")
def updateArticle(request, slug):
    article = get_object_or_404(Article, slug=slug)
    form = CreateArticle(request.POST or None,request.FILES or None,instance = article)
    if form.is_valid():
        article = form.save(commit=False)        
        article.author = request.user
        article.save()
        messages.success(request,"Makale başarıyla güncellendi")
        return redirect("article:list")

    return render(request,"update.html",{"form":form})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST or None, request.FILES or None)
        if form.is_valid():
            article = form.save(commit=False)
            article.slug = slugify(article.title)
            article.author = request.user
            article.save()
            messages.success(request,"Article created successfully")
            return redirect('articles:list')
    else:
        form = CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})

def addComment(request,slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author  = comment_author, comment_content = comment_content)
        newComment.article = article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"slug":slug}))