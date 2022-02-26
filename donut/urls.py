from django.urls import path
# import views
from .views import HomePageView, AboutView, InfoView

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutView.as_view(), name= 'about'),
    path('info', InfoView.as_view(), name= 'info'),
]