from django.contrib import admin
from .models import Post


# I create a new Post model for the admin panel
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'datetime', 'hash', 'tx_id')


admin.site.register(Post, PostAdmin)
