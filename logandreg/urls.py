"""logandreg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from logreg import views

urlpatterns = [
    path('', views.home),
    path('register_user', views.register),
    path('success', views.success),
    path('login_user', views.login),
    path('logout', views.logout),
    path('add_message', views.add_mess),
    path('view/<int:user_id>', views.one_user),
    path('add_comm/<int:mess_id>', views.add_comm)
]
