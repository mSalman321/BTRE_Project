from django.urls import path
from . import views

# /listings/
urlpatterns = [

    path('',views.index,name="listings"),
    # accessing the paramter within the view method
    path('<int:listing_id>',views.listing, name="listing"),
    path('search', views.search, name="search")

]

