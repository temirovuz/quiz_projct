from django.urls import path

from rest_framework import routers

from .views import (
    hello_world,
    quiz_types,
    quiz_type_detail,
    QuestionViewSet,

)

router = routers.DefaultRouter()

router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', hello_world),
    path('types/', quiz_types),
    path('types/<int:pk>/', quiz_type_detail),
    # path('questions/', QuestionListAPIView.as_view(), name='question_list'),
    # path('questions/<int:pk>/', QuestionDetailAPIView.as_view(), name='question_deatil')
]

urlpatterns += router.urls
