from django.contrib import admin
from django.urls import path, include
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('todos.urls')),
    path('api-auth/', include('rest_auth.urls')),
    path('api/v1/', include('categories.urls')),
    path('api-auth/registration/', include('rest_auth.registration.urls'))
]
