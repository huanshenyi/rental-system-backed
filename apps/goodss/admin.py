from django.contrib import admin
from .models import Category, Tag, Goods


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'is_nav', 'owner', 'created_time', )
    # 一ページ最大50個のデータを表示
    list_per_page = 50
    # 時間順に並び替え
    ordering = ('-created_time', )
    search_fields = ('name', )
    list_fields = ('name', 'status', 'is_nav', 'owner', )

    def save_model(self, request, obj, form, change):
        obj.owner = request.user.uid
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'owner', 'created_time', )
    # list_filter = ('id', 'name', 'status', 'owner', 'created_time', )
    fk_fields = ('user_group', )
    ordering = ('-created_time', )
    search_fields = ('name', )

    def save_model(self, request, obj, form, change):
        obj.owner = request.user.uid
        return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'image', 'owner', 'user_group', 'category', 'created_time', )
    fields = ('name', 'status', 'image', 'user_group', 'category', 'tag', )
    search_fields = ('name', )
    # fk_fields = ('owner', 'user_group', 'category', 'tag', )

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(GoodsAdmin, self).save_model(request, obj, form, change)
