import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter ,URLRouter
from channels.auth import AuthMiddlewareStack
import client_manager.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = ProtocolTypeRouter(
    {
        "http" : get_asgi_application() , 
        "websocket" : AuthMiddlewareStack(
            URLRouter(
                client_manager.routing.websocket_urlpatterns
            )    
        )
    }
)