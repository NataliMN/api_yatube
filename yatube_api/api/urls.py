from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_for_api_v1 = DefaultRouter()
router_for_api_v1.register('posts', PostViewSet)
router_for_api_v1.register('groups', GroupViewSet)
router_for_api_v1.register(r'^posts/(?P<post_id>\d+)/comments',
                           CommentViewSet, basename='comments')


urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(router_for_api_v1.urls)),
]
