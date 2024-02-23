from todo.views import PessoaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PessoaViewSet)
urlpatterns = router.urls

