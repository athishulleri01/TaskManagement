from django.contrib import admin
from django.urls import path, include
from django.conf import settings


from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Task management API",
        default_version="v1",
        description="An Task Management API for Management",
        contact=openapi.Contact(email="api.imperfect@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path(settings.ADMIN_URL, admin.site.urls), 
    path("api/v1/auth/", include("djoser.urls")),
    path("api/v1/auth/", include("core_apps.users.urls")),
    path("api/v1/admin/", include("core_apps.dashboard.urls")),
    path("api/v1/", include("core_apps.tasks.urls")),

]

admin.site.site_header = "Task Management Admin"
admin.site.site_title = "Task Management Admin Portal"
admin.site.index_title = "Welcome to Task Management Admin Portal"
