from django.contrib import admin
from .models import Userprofile
from django.utils.safestring import mark_safe

class UserprofileAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number', 'get_image', 'image', 'is_employer')
    fields = ['is_employer', 'phone_number', 'image']   
    list_filter = ['is_employer']
    list_editable = ['phone_number','is_employer']


    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="(obj.image.url)" width="75">')
        else:
            return 'No photo'

    get_image.short_description = 'Photo'

admin.site.register(Userprofile, UserprofileAdmin)