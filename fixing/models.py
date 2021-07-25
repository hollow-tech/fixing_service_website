from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

TYPE_CHOICES = (
    ('ремонт', 'ремонт'),
    ('обслуживание', 'обслуживание'),
    ('консультация', 'консультация')
)

STATUS_CHOICES = (
    ('в работе', 'в работе'),
    ('закрыта', 'закрыта')
)


class Worker(models.Model):
    name = models.CharField("Сотрудник", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Order(models.Model):
    name = models.CharField("Имя", max_length=50, blank=True, null=True)
    phone_number = PhoneNumberField("Телефон", blank=True, null=True)
    workers = models.ForeignKey(Worker, on_delete=models.CASCADE, blank=True, null=True)
    order_time = models.DateTimeField("Время подачи заявки", auto_now_add=True)
    type = models.CharField("Тип заявки", max_length=300, choices=TYPE_CHOICES, blank=True, null=True)
    status = models.CharField("Статус заявки", max_length=300, choices=STATUS_CHOICES, blank=True, null=True,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


class Consultation(models.Model):
    name = models.CharField("Имя", max_length=50, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    workers = models.ForeignKey(Worker, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Консультация"
        verbose_name_plural = "Консультации"



