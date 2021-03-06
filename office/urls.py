"""office URL Configuration

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
from django.contrib import admin
from django.conf.urls import include, url
from graphene_django.views import GraphQLView
from rest_framework_swagger.views import get_swagger_view

from schema import schema

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('core.urls', namespace='core')),
    url(r'^api/organization/', include('organization.urls', namespace='organization')),
    url(r'^docs/', schema_view),
    url(r'^graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]

