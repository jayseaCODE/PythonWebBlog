from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.post_list, name='post_list'),
    # Django expects an integer value and will transfer it to the view as variable 'pk'
    url('post/<int:pk>/', views.post_detail, name='post_detail' ),
]