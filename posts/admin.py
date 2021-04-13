from django.contrib import admin
from .models import PostInfo, PostImage, Category, SubCategory

class PostImageAdmin(admin.StackedInline):
    model = PostImage
    

@admin.register(PostInfo)
class PostInfoAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    list_display = ['id', 'title', 'subCategory', 'show', 'updated', 'created']
    
    list_editable = ['show']
    exclude = ['slug']
    class Meta:
       model = PostInfo



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    prepopulated_fields = {'slug': ('name',)}
