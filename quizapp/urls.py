from django.urls import path, include

from  .views import question, qiuz, result_list

urlpatterns = [
    path('', qiuz, name='qiuz'),
    path('quiz/<int:pk>/', question, name='quistion'),
    path('results/', result_list, name='results'),

]