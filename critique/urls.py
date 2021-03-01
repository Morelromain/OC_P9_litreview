from django.conf.urls.static import static
from django.urls import path, include

from critique import views
from OC_P9 import settings

urlpatterns = [

    path('feed', views.feed, name="feed"),

    #path('accounts/', include('django.contrib.auth.urls')),  
 
    path('addreview', views.create_review, name="addreview"),
    path('addreview/<int:id_review>', views.create_review, name="addreview"),

    path('linkreview', views.link_review, name="linkreview"),    
    path('linkreview/<int:id_ticket>', views.link_review, name="linkreview"),

    path('viewreview/<int:id_review>', views.view_review, name="viewreview"),
    path('deletereview/<int:id_review>', views.delete_review, name="deletereview"),

    path('addtandr', views.create_t_and_r, name="addtandr"),
    
    path('addticket', views.create_ticket, name="addticket"),
    path('addticket/<int:id_ticket>', views.create_ticket, name="addticket"),
    path('viewticket/<int:id_ticket>', views.view_ticket, name="viewticket"),
    path('deleteticket/<int:id_ticket>', views.delete_ticket, name="deleteticket"),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)