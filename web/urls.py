from django.conf.urls import url
from web import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('article', views.ArticleView)

urlpatterns = [
    # 首页
    url(r'^index/', views.index, name='index'),
    # 列表（日记）
    url(r'^list/', views.mylist, name='list'),
    # 关于我
    url(r'^about/', views.about, name='about'),
    # 相册
    url(r'^album/', views.album, name='album'),
    # 留言
    url(r'^gbook/', views.gbook, name='gbook'),
    # 内容页
    url(r'^info/(\d+)/', views.info, name='info'),
    # 图片内容页
    url(r'^infopic/', views.infopic, name='infopic'),
    # 按栏目查询
    url(r'^list_column/(\d+)/', views.list_column, name='list_column'),


]

urlpatterns += router.urls
