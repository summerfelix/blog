from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from backweb.column_serializer import ColumnSerializer
from backweb.form import AddArtForm
from backweb.models import Admin, Article, Column

from django.core.paginator import Paginator

from rest_framework import mixins, viewsets


def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpwd')

        admin = Admin.objects.filter(username=username, password=password).first()

        if not admin:
            return render(request, 'backweb/login.html')

        request.session['admin_id'] = admin.id

        return HttpResponseRedirect(reverse('backweb:index'))


def index(request):
    if request.method == 'GET':
        admin = request.admin.first()
        return render(request, 'backweb/index.html', {'admin': admin})


def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('backweb:login'))


def article(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        articles = Article.objects.all()
        paginator = Paginator(articles, 4)
        page = paginator.page(page)

        admin = request.admin.first()
        return render(request, 'backweb/article.html', {'page': page, 'admin': admin})


def add_art(request):
    if request.method == 'GET':
        admin = request.admin.first()

        return render(request, 'backweb/add-article.html', {'admin': admin})

    if request.method == 'POST':
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # desc = request.POST.get('describe')
        # tags = request.POST.get('tags')

        form = AddArtForm(request.POST, request.FILES)
        col = Column.objects.all()

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            desc = form.cleaned_data['desc']
            tags = form.cleaned_data['tags']
            icon = form.cleaned_data['titlepic']
            column = form.cleaned_data['column']

            Article.objects.create(title=title, desc=desc, content=content, tags=tags, icon=icon, column_id=column)

            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            return render(request, 'backweb/add-article.html', {'form': form})


def update_art(request, id):
    if request.method == 'GET':
        admin = request.admin.first()

        article = Article.objects.filter(pk=id).first()
        return render(request, 'backweb/add-article.html', {'article': article, 'admin': admin})
    if request.method == 'POST':
        form = AddArtForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            desc = form.cleaned_data['desc']
            tags = form.cleaned_data['tags']
            icon = form.cleaned_data['titlepic']
            column = form.cleaned_data['column']

            article = Article.objects.filter(pk=id).first()

            article.title = title
            article.content = content
            article.tags = tags
            article.desc = desc
            article.column_id = column
            if icon:
                article.icon = icon
            article.save()

            return HttpResponseRedirect(reverse('backweb:article'))
        else:
            article = Article.objects.filter(pk=id).first()
            return render(request, 'backweb/add-article.html', {'form': form, 'article': article, 'admin': admin})


def del_art(request, id):
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()

        return HttpResponseRedirect(reverse('backweb:article'))


def flink(request):
    if request.method == 'GET':
        admin = request.admin.first()

        return render(request, 'backweb/flink.html', {'admin': admin})


def manage_user(request):
    if request.method == 'GET':
        admin = request.admin.first()
        user = Admin.objects.all()
        return render(request, 'backweb/manage-user.html', {'admin': admin, 'user': user})


def setting(request):
    if request.method == 'GET':
        admin = request.admin.first()

        return render(request, 'backweb/setting.html', {'admin': admin})


class ColumnView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin,
             mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    # 查询返回的数据
    queryset = Column.objects.all()
    # 序列化返回的数据
    serializer_class = ColumnSerializer


# 栏目
def category(request):
    if request.method == 'GET':
        return render(request, 'backweb/category.html')

