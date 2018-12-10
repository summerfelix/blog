from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from backweb.models import Article, Column

from rest_framework import mixins, viewsets

from django.core.paginator import Paginator
from web.article_serializer import ArticleSerializer
from web.article_filter import ArticleFilter


def index(request):
    if request.method == 'GET':
        article = Article.objects.all()
        column = Column.objects.all()
        tags = set()
        for art in article:
            tags.add(art.tags)
        return render(request, 'web/index.html', {'article': article, 'tags': tags, 'column': column})


def mylist(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        article = Article.objects.all()
        paginator = Paginator(article, 5)
        page = paginator.page(page)

        column = Column.objects.all()

        tags = set()
        for art in article:
            tags.add(art.tags)

        return render(request, 'web/list.html', {'article': article, 'page': page, 'tags': tags, 'column': column})


def about(request):
    if request.method == 'GET':

        return render(request, 'web/about.html')


def album(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        article = Article.objects.all()
        paginator = Paginator(article, 4)
        page = paginator.page(page)
        return render(request, 'web/share.html', {'page': page})


def gbook(request):
    if request.method == 'GET':

        return render(request, 'web/gbook.html')


def info(request, id):
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        articles = Article.objects.all()

        column = Column.objects.all()

        tags = set()
        for art in articles:
            tags.add(art.tags)

        return render(request, 'web/info.html', {'art': article, 'article': articles, 'tags': tags, 'column': column})


def infopic(request):
    if request.method == 'GET':

        return render(request, 'web/infopic.html')


def list_column(request, id):
    if request.method == 'GET':

        article = Article.objects.all()
        column = Column.objects.all()

        col = Column.objects.filter(pk=id).first()

        tags = set()
        for art in article:
            tags.add(art.tags)

        return render(request, 'web/list_column.html', {'col': col, 'article': article, 'tags': tags, 'column': column})


class ArticleView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Article.objects.all()

    serializer_class = ArticleSerializer

    filter_class = ArticleFilter





