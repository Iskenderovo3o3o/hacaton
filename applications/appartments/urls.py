from rest_framework.routers import DefaultRouter
from .views import AppartmentViewSet, CommentViewSet, FavoritesView

router = DefaultRouter()
router.register('post', AppartmentViewSet, 'posts')
router.register('comment', CommentViewSet, 'comments')
router.register(r'favorites_d', FavoritesView, basename='favorites_ff')


urlpatterns = router.urls
