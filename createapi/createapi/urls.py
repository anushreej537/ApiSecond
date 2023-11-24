from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stucreate/', views.student_create),
    path('getdata/',views.getdata),
    path('senddata/',views.senddata)
]
