

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework_jwt.views import obtain_jwt_token
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('global_idea_of_travel_notebook.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token-auth/', obtain_jwt_token),
    path('core/', include('core.urls')),
    path('', views.EntryList.as_view(), name='entry_list'),
    path('<int:pk>', views.EntryDetail.as_view(), name='entry_detail'),
]
