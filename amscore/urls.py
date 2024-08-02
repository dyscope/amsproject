from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("<int:pk>/", views.AnimePage.as_view()),
    path("review/<int:pk>/", views.AddReviews.as_view(), name="add_reviews")
]
