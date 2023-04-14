
from django.urls import path
from website.views import index_view,about_view,contact_view

urlpatterns = [
    
    #path("url addres ", "view")
    path('',index_view ),
    path('about',about_view),
    path('contact',contact_view)
    
]