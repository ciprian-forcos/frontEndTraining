"""
URL configuration for backendAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from notesApp import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schemaView = get_schema_view(
    openapi.Info(
        title= "Swagger API",
        default_version="v1",
        description="Swagger API description",
        terms_of_service="Open License",
        contact=openapi.Contact(
            email= "skipper_cpr@yahoo.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/notes", views.NOTE_VIEW_WITHOUT_PK.as_view(), name="Notes_Without_PK"),
    path("swagger/", schemaView.with_ui("swagger", cache_timeout=0), name="schema_swagger_ui"),
    
]


