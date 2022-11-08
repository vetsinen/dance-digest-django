from django.contrib import admin
from .models import Post, Coach

admin.site.register(Post)
@admin.register(Coach)
class CoachModelAdmin(admin.ModelAdmin):
    pass
    # exclude = ('maintainer',)
    #TODO: check if request.user is superadmin
    # def get_exclude(self, request, obj=None):
    #     if obj is not None and request.user.is_authenticated():  # In Django 1.10+ use request.user.is_authenticated
    #         if obj.creator == request.user:
    #             return ['status']
    #     else:
    #         return []

class CoachesEditorArea(admin.AdminSite):
    site_header = 'Coaches Editor Area'

coachesEditorArea = CoachesEditorArea(name='Coaches editor')

coachesEditorArea.register(Coach)

class CoachModelEditor(admin.ModelAdmin):
    exclude = ('maintainer',)

