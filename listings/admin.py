from django.contrib import admin

# Register your models here.
from listings.models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    # make sure to make the comma
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('id', 'title', 'description',
                     'address', 'city', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
