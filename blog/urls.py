"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.staticfiles.urls import static

from blog.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 前台
    url(r'^web/', include('web.urls', namespace='web')),
    # 管理后台
    url(r'^backweb/', include('backweb.urls', namespace='backweb')),

    url(r'api/backweb/', include('backweb.urls')),

    url(r'api/web/', include('web.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
