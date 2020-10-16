from django.contrib import admin
from .models import Profile


# I create a new Profile model for the admin panel
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_ip_used', 'is_ip_changed', 'post_counter')

    # I add a new field to show the number of posts written by each user
    @staticmethod
    def post_counter(self):
        return self.user.post_set.all().count()


admin.site.register(Profile, ProfileAdmin)
