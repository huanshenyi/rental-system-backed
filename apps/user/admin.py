from django.contrib import admin
from .models import Group, User


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time', 'owner')
    fields = ('name', )

    def save_model(self, request, obj, form, change):
        obj.owner = request.user.uid
        return super(GroupAdmin, self).save_model(request, obj, form, change)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('uid', 'telephone', 'email', 'username', 'avatar', 'data_joined', 'is_active', 'user_group')
    fields = ('uid', 'telephone', 'email', 'username', 'avatar', 'data_joined', 'is_active', 'user_group')

