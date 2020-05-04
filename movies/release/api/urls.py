from django.urls import path, include

from rest_framework.routers import DefaultRouter

from release.api import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet)


# api_name = 'release'
urlpatterns =[
    path('', include(router.urls)),
]