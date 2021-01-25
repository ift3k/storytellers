from django.urls import path
from . import views

app_name = 'storytellers'

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:Post>/',
         views.post_detail,
         name='post_detail'),
]
