from django.conf.urls.static import static
from django.urls import path, include

from utilisateur import views
from OC_P9 import settings


urlpatterns = [
    path('', views.connection, name="connection"),
    path('register', views.create_user, name="register"),
    path('subscription', views.subscription, name="subscription"),
    path('accounts/', include('django.contrib.auth.urls')),   
    path('delete_subs/<int:id_subs>', views.delete_subs, name="delete_subs"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)