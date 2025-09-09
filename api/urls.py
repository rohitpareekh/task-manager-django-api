from django.urls import path
from .views import RegisterView, TaskListCreateView, TaskDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# router = DefaultRouter()
# router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("login/", TokenObtainPairView.as_view(), name="login"),   # JWT login
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("tasks/", TaskListCreateView.as_view(), name="task_list_create"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
]

# urlpatterns += router.urls