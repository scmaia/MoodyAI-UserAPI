from django.contrib import admin
from django.urls import include, path, re_path
from moodyAIpy import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("api/", include("moodyAIpy.urls")),
    path("admin/", admin.site.urls),

    path('auth/', obtain_auth_token, name='api_token_auth'),
    path('auth/signup', views.register),

    re_path(r'^api/users/([0-9])$', views.one_user),
    re_path(r'^api/users/([0-9])/responses/$', views.responses_list),
    re_path(r'^api/responses/([0-9])$', views.one_response),
]

urlpatterns = format_suffix_patterns(urlpatterns)