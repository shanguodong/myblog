from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime


def home(request):
    articles = Article.objects.all()
    print(articles)
    return render(request, "home.html", {'articles': articles})


def overview(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title:%s, category:%s, datetime:%s, article:%s" % (post.title, post.category, post.date_time, post.article))
    return HttpResponse(str)
