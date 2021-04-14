"""djangoProject URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from professors import views
from django.contrib.auth.views import LoginView, LogoutView

from professors.views import ReferenceFormSetView

urlpatterns = [
    path(r'group/<int:groupid>/', ReferenceFormSetView.as_view(), name='tests'),
    path(r'groups/<int:typeid>/', views.GroupsListView.as_view(), name='groups'),
    re_path(r'^groups/', views.ProfessorTypesListView.as_view(), name='groups_type'),
    path('home/', views.index, name='home'),
    path('', views.index),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    url(r'^professors/$', views.ProfessorsListView.as_view(), name='professors'),
    path('login/', LoginView.as_view(), name='login'),
    # url(r'^tests/$', ReferenceFormSetView.as_view(), name='tests'),
    path('formula/', views.formula, name='formula'),
    url(r'^administration/', views.AllGroupsListView.as_view(), name='administration'),
]
