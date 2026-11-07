from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('dining/', views.dining, name='dining'),
    path('contact/', views.contact, name='contact'),
    path('offers/', views.offers, name='offers'),
    path('rooms/', views.rooms, name='rooms'),
    path('rooms/premium-king/', views.room_detail, {'template_name': 'room-details.html'}, name='room_details'),
    path('rooms/standard/', views.room_detail, {'template_name': 'room-details2.html'}, name='room_details2'),
    path('rooms/garden-suite/', views.room_detail, {'template_name': 'room-details3.html'}, name='room_details3'),
    path('rooms/family/', views.room_detail, {'template_name': 'room-details4.html'}, name='room_details4'),
    path('offers/offer-1/', views.offer_detail, {'template_name': 'offer1.html'}, name='offer_detail1'),
    path('offers/offer-2/', views.offer_detail, {'template_name': 'offer2.html'}, name='offer_detail2'),
    path('offers/offer-3/', views.offer_detail, {'template_name': 'offer3.html'}, name='offer_detail3'),
    path('offers/offer-4/', views.offer_detail, {'template_name': 'offer4.html'}, name='offer_detail4'),
]