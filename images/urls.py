from django.urls import path
from rest_framework.routers import SimpleRouter

from images import views

# urlpatterns = [
#     path('<int:pk>/', views.PostDetail.as_view(), ),
#     path('', views.PostList.as_view(), ),
#     path('users/', views.UserList.as_view()),
#     path('users/<int:pk>/', views.UserDetail.as_view())
# ]

router = SimpleRouter()
router.register('images', views.ImagesViewSet, basename='images')

urlpatterns = router.urls
