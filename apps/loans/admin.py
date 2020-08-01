from django.contrib import admin
from .models import Period


@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display = (
        "id", "owner", "goods", "goods_num", "status", "comment", "plans_return_time", "returned_time", "created_time",)
    list_per_page = 50
    ordering = ("-created_time",)
    list_editable = ("goods", "goods_num", "status", "comment", "plans_return_time", )
    fields = ("goods", "goods_num", "status", "comment", "plans_return_time", )
    fk_fields = ('owner', 'goods', )

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user.uid
    #     return super(PeriodAdmin, self).save_model(request, obj, form, change)
