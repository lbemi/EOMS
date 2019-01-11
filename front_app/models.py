from django.db import models

class Service_Scripts(models.Model):
    script_id = models.AutoField(verbose_name='脚本ID', primary_key=True)
    script_name = models.CharField(verbose_name='脚本名称', max_length=50)

    class Meta:
        verbose_name_plural = verbose_name = '脚本'

    def __str__(self):
        return self.script_name


class Services(models.Model):
    service_id = models.AutoField(verbose_name='服务I', primary_key=True)
    service_name = models.CharField(verbose_name='服务器名称', max_length=20)
    service_port = models.IntegerField(verbose_name='服务端口')
    service_script = models.ForeignKey(Service_Scripts, on_delete=models.DO_NOTHING, verbose_name='脚本')
    class Meta:
        verbose_name_plural = verbose_name = '服务'

    def __str__(self):
        return self.service_name

class Host(models.Model):
    host_id = models.AutoField(verbose_name='服务器ID', primary_key=True)
    host_name = models.CharField(verbose_name='服务器名称', max_length=20)
    host_ip = models.GenericIPAddressField(verbose_name='IP')
    host_services = models.ManyToManyField(Services , verbose_name='主机服务')

    class Meta:
        verbose_name_plural = verbose_name = '服务器'

    def __str__(self):
        return self.host_name