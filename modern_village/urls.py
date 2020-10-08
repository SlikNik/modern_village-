"""modern_village URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from authentication import views as authenticateviews
from notices import views as noticeviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', noticeviews.index_view, name='homepage'),
    path('notice/<int:id>/edit/', noticeviews.notice_edit, name='editnotice'),  
    path('notice/<int:id>/', noticeviews.notice_detail, name='noticedetails'),
    path('notices/', noticeviews.notice_sorted_view, name='noticesorted'),
    path('ownernotices/', noticeviews.owner_notice_view, name='ownernotices'),
    path('addnotice/', noticeviews.add_notice, name='addnotice'),
    path('login/', authenticateviews.login_view, name="loginview"),
    path('logout/', authenticateviews.logout_view, name="logoutview"),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
