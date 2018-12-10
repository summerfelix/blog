from django.conf.urls import url, include
from backweb import views

from rest_framework.routers import SimpleRouter

# 生成路由对象
router = SimpleRouter()
router.register('column', views.ColumnView)

urlpatterns = [
    # 登录页面
    url(r'^login/', views.login, name='login'),
    # 主页
    url(r'^index/', views.index, name='index'),
    # 退出登录
    url(r'^logout/', views.logout, name='logout'),
    # 文章管理
    url(r'^article/', views.article, name='article'),
    # 添加文章
    url(r'^add_art/', views.add_art, name='add_article'),
    # 修改文章
    url(r'^update_art/(\d+)/', views.update_art, name='update_article'),
    # 删除文章
    url(r'^del_art/(\d+)/', views.del_art, name='del_art'),
    # 友情链接
    url(r'^flink/', views.flink, name='flink'),
    # 管理用户
    url(r'^manage_user/', views.manage_user, name='manage_user'),
    # 设置
    url(r'^setting/', views.setting, name='setting'),
    # 栏目
    url(r'^category/', views.category, name='category'),

]

# 生成资源对应的路由地址
urlpatterns += router.urls
