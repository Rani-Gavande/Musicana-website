"""
URL configuration for Musicanaweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Musicanaweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('header/',views.header),
    path('login/',views.mylogin),
    path('sign/',views.mysignup),
    path('logout/',views.logout),
    path('mymain/',views.mymain),
    path('',views.homepage),
    path('profile/',views.profile),
    path('profile/EditProfile/',views.EditProfile),
    path('error/',views.error),
    path('errorlogin/',views.errorlogin),
    path('TrendingDetails/',views.TrendingDetail),
    path('ArtistDetails/<int:artist_id>/',views.artist_Details),
    path('AlbumDetails/<int:album_id>/',views.album_Details),
    path('AboutUs/',views.AboutUs),
    path('Premium/',views.Premium),
    path('Help/',views.Help)

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)