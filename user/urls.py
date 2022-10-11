from django.urls import path
from .views import delete_user, edit_user, register_user, user_list, user_profile

app_name="user"

urlpatterns=[
    path('register_user/',register_user,name='register_user'),
    path('user_list/',user_list,name='user_list'),
    path('edit_user/<int:id>',edit_user,name='edit_user'),
    path('user_profile/<int:id>',user_profile,name='user_profile'),
    path('delete_user/<int:id>',delete_user,name='delete_user'),
    
]