from django.contrib import admin
from .models import * 

admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(Buyers)
admin.site.register(Admin)