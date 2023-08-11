from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from departments.api.router import router_department
from visit.api.router import router_visit

urlpatterns = [
    path('admin/', admin.site.urls),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
     path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
     path('api/', include('users.api.router')),
     path('api/',include(router_department.urls)),
     path('api/',include(router_visit.urls)),
]
