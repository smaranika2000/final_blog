
from django.urls import path
from.import views

urlpatterns = [
    path('postapi/',views.post_api),
    path('postapi/<int:pk>',views.post_api),
]