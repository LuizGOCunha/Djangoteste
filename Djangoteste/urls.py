"""Djangoteste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

# Aqui a função include tem o trabalho de incluir um módulo URL inteiro no path especificado.
# No caso o que será feito é levar em consideração todos os outros paths que estão especificados neste módulo
# Poderíamos referenciar cada path em app.urls aqui mesmo, mas isso tornaria edição dos aplicativos mais dificil, e o
# layout do código mais confuso. Por isso é melhor dar um módulo urls para cada aplicativo e usar include.
urlpatterns = [
    path('app/', include('app.urls')),
    path('admin/', admin.site.urls),

]
