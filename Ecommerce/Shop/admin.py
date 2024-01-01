from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.category)
admin.site.register(models.user_model)
admin.site.register(models.discount)
admin.site.register(models.seller)
admin.site.register(models.order)
admin.site.register(models.payment)

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
        list_display = ['id','name','massage']
        
@admin.register(models.CommentReply)
class CommentAdmin(admin.ModelAdmin):
        list_display = ['id','name','massage']
        
@admin.register(models.product)
class ProductAdmin(admin.ModelAdmin):
    fields=(('title','discounted_prices','price','discount','slug','tags')
        ,('image','additional_image_1')
        ,('quantity','width','height','length','Weight')
        ,('category','status','color','Advertising','size','material','season','sexuality')
            )
    list_display = ['id','__str__','slug','category','price','status']
    ordering = ('id',)
    search_fields =('id','name','price',)




