from django.contrib import admin
from .models import BlogPost, itemImage, Categorie
from .forms import *

# Register your models here. 
class imageInLine(admin.StackedInline):
    model = itemImage
    extra = 1

class blogAdmin(admin.ModelAdmin):
    inlines = [imageInLine]
    form = bodyAdminForm
   

admin.site.register(BlogPost, blogAdmin)
admin.site.register(Categorie)
admin.site.register(clientMessage)
admin.site.register(newsletter)
admin.site.register(blogComment)
