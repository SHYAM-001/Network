
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newPost",views.newPost, name = "newpost"),
    path("profile/<int:user_id>",views.profile, name = "profile"),
    path("unfollow",views.unfollow, name = "unfollow"),
    path("follow",views.follow, name = "follow"),
    path("following",views.following, name = "following"),
    path("edit/<int:post_id>",views.edit, name = "edit"),
    path("add_like/<int:post_id>",views.add_like, name = "add_like"),
    path("remove_like/<int:post_id>",views.remove_like, name = "remove_like"),
    path("profile_link/<int:user_id>",views.profile_link,name="profile_link"),
]
