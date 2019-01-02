from django.contrib import admin
from .models import Post, Serials, Topserials

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','serie','episode')
    pass

admin.site.register(Post, PostAdmin)

class SerialsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    pass

admin.site.register(Topserials)

admin.site.register(Serials, SerialsAdmin)

