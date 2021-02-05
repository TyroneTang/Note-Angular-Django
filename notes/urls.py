from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/notes/<int:id>", views.notes, name="notes"),
    path("api/editnotes/<int:id>", views.edit_notes, name="edit_notes"),
    path("api/deletenotes/<int:id>", views.delete_notes,name="delete_notes"),
    
    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    # path('auth/signup/', views.new_user, name="new_user"),
    path('auth/refresh-token/', refresh_jwt_token),
]