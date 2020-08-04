from rest_framework.routers import SimpleRouter
from api.books.views import BookViewSet
from api.post.views import PostViewSet
from api.happiness.views import HappyRecordViewSet
from api.todo.views import TodoViewSet
from api.user.views import UserViewSet

# urlpatterns = [
#     path("books", BookListAPIView.as_view()),
#     path("books/<int:pk>", BookAPIView.as_view()),
#     path("todos", TodoListAPIView.as_view()),
#     path("todos/<int:pk>", TodoAPIView.as_view()),
#     path("posts", PostListAPI.as_view()),
#     path("posts/<int:pk>", PostAPI.as_view()),
#     path("users/", UserList.as_view()),  # new
#     path("users/<int:pk>/", UserDetail.as_view()),  # new
# ]

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("posts", PostViewSet, basename="posts")
router.register("todos", TodoViewSet, basename="todos")
router.register("books", BookViewSet, basename="books")
router.register("happy_records", HappyRecordViewSet, basename="happy_level")
urlpatterns = router.urls
