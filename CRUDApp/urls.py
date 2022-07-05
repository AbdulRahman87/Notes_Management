from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="Home"),
    path('signup/',views.signUp, name="signUp"),
    path('handleSignUp/', views.handleSignUp, name="signUpHandler"),
    path('handleLogIn/', views.handleLogin, name="LogInHandler"),
    path('handleLogOut/', views.handleLogOut, name="LogOutHandler"),
    path('addNote/', views.addNote, name="addNote"),
    path('note/<int:note_id>', views.userNote, name="userNote"),
    path('deleteNote/<int:note_id>', views.deleteNote, name="deleteNote"),
    path('editNote/<int:note_id>', views.editNote, name="editNote"),
    path('searchNote/', views.searchNote, name="searchNote"),
]