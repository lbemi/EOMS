from django.contrib import admin
from .models import Host, Services, Service_Scripts
# Register your models here.


class Services_Info(admin.ModelAdmin):
    list_display = ('service_name','service_port','service_script')

class Host_Info(admin.ModelAdmin):
    list_display = ('host_name','host_ip')

class Scripts_Info(admin.ModelAdmin):
    list_display = ('script_id','script_name')

# def get_service_info():
#     data = Host.objects.all()
#     print(data)
# get_service_info()
admin.site.register(Services, Services_Info)
admin.site.register(Host, Host_Info)
admin.site.register(Service_Scripts, Scripts_Info)

