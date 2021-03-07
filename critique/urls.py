from django.conf.urls.static import static
from django.urls import path, include

from critique import views
from OC_P9 import settings


urlpatterns = [
    path('', views.feed, name="feed"),
    path('accounts/', include('django.contrib.auth.urls')), 
    
    path('feed', views.feed, name="feed"),
    path('addreview/<int:id_review>', views.create_review, name="addreview"),
    path('linkreview', views.link_review, name="linkreview"),    
    path('linkreview/<int:id_ticket>', views.link_review, name="linkreview"),
    path('deletereview/<int:id_review>', views.delete_review, name="deletereview"),
    path('addtandr', views.create_t_and_r, name="addtandr"),
    path('addticket', views.create_ticket, name="addticket"),
    path('addticket/<int:id_ticket>', views.create_ticket, name="addticket"),
    path('deleteticket/<int:id_ticket>', views.delete_ticket, name="deleteticket"),
    path('myposts', views.view_myposts, name="myposts"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
