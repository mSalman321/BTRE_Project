from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','photo_main','address','list_date'  ,'realtor', 'is_published')
    # to make links clickable

    list_display_links = ('id', 'title',)

    list_filter = ('realtor','price','is_published', )

    list_editable = ('is_published',)

    search_fields = ('title', 'description', 'address' , 'city', 'zipcode')

    list_per_page = 25;





admin.site.register(Listing,ListingAdmin)