"""authproject URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from firstapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.home_view),
    url(r'^help/', views.help_view),
    url(r'^contact/', views.contact_view),
    url(r'^mysql/', views.mysql_view),
    url(r'^django/', views.django_view),
    url(r'^contact1/', views.contact1_view),
    url(r'^logout/', views.logout_view),
    url(r'^loading/', views.loading_view),
    url(r'^signup/', views.signup_view),
    url(r'^file/', views.simple_upload),
    url(r'^upload/', views.model_form_upload),
    url(r'^display/', views.display_info),
    url(r'^data/', views.data_info),
    url(r'^dataa/',views.dataa_info),
    url(r'^catch/',views.Catch_info),
    url(r'^files/',views.Files_info),
    url(r'^file1/',views.simple1_upload),
    url(r'^mdmd/',views.Admin_info),
    url(r'^queries/',views.Queries_info),
    url(r'^donate/',views.Donate_info),
    url(r'^accounts/', include("django.contrib.auth.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)