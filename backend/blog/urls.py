from django.urls import path
from .views import (
    PostListCreateView,
    CommentListCreateView,
    health_check,
    readiness_check,
)

urlpatterns = [
    path("posts/", PostListCreateView.as_view(), name="posts"),
    path(
        "posts/<int:post_id>/comments/",
        CommentListCreateView.as_view(),
        name="comments",
    ),
    path("health/", health_check, name="health"),
    path("readiness/", readiness_check, name="readiness"),
]