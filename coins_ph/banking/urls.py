from django.urls import path
from banking import views


urlpatterns = [
    path('', views.index, name='index'),
    path('payments/', views.payment_list),
]