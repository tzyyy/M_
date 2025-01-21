from django.contrib import admin
from django.urls import path
from accounts.views import SignUpView, SignInView, MeView

urlpatterns = [
    path("admin/", admin.site.urls),
]


urlpatterns += [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('me/', MeView.as_view(), name='me'),

]
