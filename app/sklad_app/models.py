from django.db import models

class sklad_item(models.Model):
    on_base = 'OB'
    given = 'GV'
    registrator = 'RG'
    camera = 'CAM'
    injector = 'INJ'
    type_choices = (
        (registrator, 'Регистратор'),
        (camera, 'Камера'),
        (injector, 'Инжектор'),
        (injector, 'Коммутатор'),
    )
    status_choices = (
        (on_base, 'На складе'),
        (given, 'Выдан'),
    )
    id                = models.AutoField(primary_key=True)
    type              = models.CharField("Тип устройства", max_length=3, choices=type_choices)
    name              = models.CharField("Наименование", max_length=255, blank=True)
    serial_number     = models.CharField("Серийный номер", max_length=100, blank=True)
    mac               = models.CharField("MAC", max_length=17, blank=True)
    many              = models.BooleanField('Множественная добавка')
    how_many          = models.IntegerField("Количество", default=1)
    create_time       = models.DateField('Дата создания', auto_now_add=True)
    status            = models.CharField('Статус', max_length=2, choices=status_choices)
    given_time        = models.DateField('Дата выдачи', auto_now_add=False)
    receiver          = models.CharField('Кому выдан',max_length=50, blank=True,null=True)



    def __str__(self):
        return '{} {}'.format(self.name,self.mac)

    class Meta:
        verbose_name        = 'итем склада'
        verbose_name_plural = 'итемы склада'
