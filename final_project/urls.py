"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path, include
import pairs.views as pairs 
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('', pairs.index),
    path('signup/', pairs.signup, name = "signup"),
    path(r'^captcha',include('captcha.urls')),
    path('login/',pairs.login, name ='login'),
    path('logout/',pairs.logout,name = 'logout'),
    path('profile/', pairs.profile),
    path("upload/", pairs.uploadFile, name = "upload"),
    path('profile/updated/',pairs.updated),
    path('pairing/',pairs.pairing),

    path('pairing/<str:pairname>/',pairs.pair_profile,name='pair_profile-url'),

    path('Learn_about_us/',pairs.learn),
    path('security/',pairs.security),
    path('marriage/',pairs.marriage),
    path('inrelationship/',pairs.inrelationship),    
    
]
urlpatterns += static(
    settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT
)