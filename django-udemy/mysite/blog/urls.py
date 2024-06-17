from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove', PostDeleteView.as_view(), name='post_remove'),
]