from django.shortcuts import render, redirect
from django.http import HttpResponse
from article.models import Article
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    return render(request, "home.html", {'article_list': article_list})


def overview(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title:%s, category:%s, datetime:%s, article:%s" % (post.title, post.category, post.date_time, post.article))
    return HttpResponse(str)


def detail(request, article_id):
    try:
        article_p = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        raise Http404
    return render(request, "post.html", {"article_p": article_p})


def allarticle(request):
    try:
        articles = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, "archives.html", {'articles': articles})


def aboutme(request):
    return render(request, "aboutme.html")


def search_tig(request, cate):
    try:
        articles = Article.objects.filter(category=str(cate))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {"articles": articles, "cate": str(cate)})


def search(request):
    if 'search_name' in request.GET:
        s = request.GET.get('search_name')
        if not s:
            render(request, 'home.html')
        else:
            search_list = Article.objects.filter(title__contains=str(s))
            if search_list.__len__() == 0:
                return render(request, 'search.html', {"search_list": search_list, "search_title": str(s), "error": True})
            else:
                return render(request, 'search.html', {"search_list": search_list, "search_title": str(s), "error": False})

    return redirect('/')


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.article