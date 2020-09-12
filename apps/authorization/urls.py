from django.conf.urls import url
from apps.authorization.views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login/$', LoginAPIView.as_view(), name="login")
]