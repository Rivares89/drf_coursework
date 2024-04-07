from django.urls import path
from users.apps import UsersConfig
from users.views import (UserCreateAPIView,
                         UserUpdateAPIView, UserRetrieveAPIView)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserCreateAPIView.as_view(),
         name='login_user'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(),
         name='update_user'),
    path('detail/<int:pk>/', UserRetrieveAPIView.as_view(),
         name='detail_user'),

    path('token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
