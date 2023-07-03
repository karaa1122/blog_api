from blog.views import *
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'blog', BlogView)
router.register(r'tags', Tagview)
router.register(r'comments', Commentview)
router.register(r'comments/<int:comment_id>', Commentview, basename = 'comments')
router.register(r'publicblog', PublicView)
router.register(r'likes', likeView)

urlpatterns = [
path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('register', RegisterView.as_view()),

] +router.urls