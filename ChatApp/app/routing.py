from django.urls import path
from . import consumers

websocket_urlpatterns=[
    path('ws/sws/<str:group_name>/', consumers.MySyncConsumer.as_asgi()),
]