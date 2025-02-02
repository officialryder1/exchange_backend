from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from .views import CreateChatSessionView, SendMessageView, GetMessageView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




# schema_view = get_schema_view(
#     openapi.Info(
#         title="Your API",
#         default_version='v1',
#         description="API documentation",
#         terms_of_service="https://www.example.com/terms/",
#         contact=openapi.Contact(email="contact@example.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),  # Ensure this is a tuple or list
# )

# The API UrLS are now determined automatically by the router
urlpatterns = [

    #Chat for Customer Care
    path('chat/create/', CreateChatSessionView.as_view(), name='create_chat_session'),
    path('chat/<int:session_id>/send/', SendMessageView.as_view(), name='send_message'),
    path('chat/<int:session_id>/messages/', GetMessageView.as_view(), name='get_messages'),
]