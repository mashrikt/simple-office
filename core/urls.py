from django.conf.urls import url, include
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    url(r'^', include('rest_auth.urls')),
    url(r'^api-token-refresh/', refresh_jwt_token),
]
