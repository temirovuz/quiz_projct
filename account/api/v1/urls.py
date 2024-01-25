from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CustomLoginView, CustomSignupView, UserModelViewSet

router = DefaultRouter()
router.register(r'users', UserModelViewSet)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
]

urlpatterns += router.urls