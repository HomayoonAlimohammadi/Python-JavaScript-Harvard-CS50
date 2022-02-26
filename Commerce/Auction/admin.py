from django.contrib import admin
from .models import User, Comment, Bid, Listing, Category

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Bid)
admin.site.register(Listing)
admin.site.register(Category)
