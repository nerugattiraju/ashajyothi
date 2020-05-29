from django.contrib import admin
from .models import Content1,Document,Simple,Data,Catch,Files

# Register your models here.
class Content1Admin(admin.ModelAdmin):
    fields = ['Name','Email','Massage']
admin.site.register(Content1,Content1Admin)
class DocumentAdmin(admin.ModelAdmin):
    fields=["description","document"]
admin.site.register(Document,DocumentAdmin)
class SimpleAdmin(admin.ModelAdmin):
    fields=["myfile"]
admin.site.register(Simple,SimpleAdmin)
class DataAdmin(admin.ModelAdmin):
    fields=["data"]
admin.site.register(Data,DataAdmin)
class CatchAdmin(admin.ModelAdmin):
    fields=["image"]
admin.site.register(Catch,CatchAdmin)
class FilesAdmin(admin.ModelAdmin):
    fields=["image"]
admin.site.register(Files,FilesAdmin)

