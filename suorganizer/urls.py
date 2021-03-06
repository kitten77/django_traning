"""suorganizer URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from organizer import urls as organizer_urls
from blog import urls as blog_urls
from blog.views import PostList
from .views import redirect_root
from user import urls as user_urls
#from organizer.views import homepage, tag_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    ##deprecated in django 2.0 now app_name is set inside app.urls.py
    #url(r'^user/', include(user_urls, app_name='user', namespace='dj-auth')),
    url(r'^user/', include(user_urls)),
    url(r'^$', redirect_root),
    url(r'^blog/', include(blog_urls)),
    url(r'^organizer/', include(organizer_urls)),
]
