from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views import defaults as default_views

from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view

from organizations.backends import invitation_backend


API_PREFIX = "(?P<version>(v1|v2))"

urlpatterns = [
    path("", lambda request: redirect("api/v1/", permanent=False)),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("transportation_suppliers.users.urls", namespace="users"),
    ),
    path("accounts/", include("allauth.urls")),
    # Django Rest Framework URLs
    path(
        "api/openapi/",
        get_schema_view(
            title="Transport Suppliers API",
            description="Transport Suppliers API",
            # urlconf='transportation_suppliers.users.api.urls'
        ),
        name="openapi-schema",
    ),
    path(
        "api/schema/",
        TemplateView.as_view(
            template_name="swagger_ui.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        TemplateView.as_view(
            template_name="redoc.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="redoc",
    ),
    path("api/auth/", include("rest_framework.urls")),
    path("api/token/", views.obtain_auth_token),
    # Django organizations
    path("invitations/", include(invitation_backend().get_urls())),
    path("organization/", include("organizations.urls")),
    # Your stuff: custom urls includes go here
    re_path(
        f"^api/{API_PREFIX}/",
        include(("transportation_suppliers.users.api.urls", "api_users")),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls))
        ] + urlpatterns
