from django.urls import include, path


urlpatterns = [
    path('banking/', include('banking.urls')),
]
