from django.urls import path
from.import views

urlpatterns = [
    path('event',views.create_event,name='event'),
    path('bookapt',views.bookApt,name="bookapt"),
    path('bookapt1',views.bookapt1,name="bookapt1"),
]