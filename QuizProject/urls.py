from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema = get_schema_view(
    openapi.Info(
        title='Quiz app',
        default_version='v1'
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quizapp.urls')),
    # account
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),

    #api
    path('api/v1/', include("quizapp.api.v1.urls")),
    path('api/v1/account/', include("account.api.v1.urls")),

    # oauth2
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),

    #jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #schema
    path('swagger<format>/', schema.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema.with_ui('swagger'), name='schema-swagger-ui'),
    path('redoc/', schema.with_ui('redoc'), name='schema-redoc'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)