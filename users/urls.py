from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Ensure this is present
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

""""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', user_views.UserListCreate.as_view(), name='user-list-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
"""