from django.db import models

from core.utils.models import BaseModel


class Client(BaseModel):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True, blank=True)
    phone_number = models.CharField(max_length=20, unique=True, blank=True)
    note = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'clients'

    def __str__(self):
        return f'{self.__class__.__name__}: {self.pk}, {self.full_name}'

    @property
    def label(self):
        return f'{self.full_name} ({self.phone_number})'

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return '-'


class TelegramClient(BaseModel):
    client = models.OneToOneField(Client, on_delete=models.PROTECT, related_name='telegram_data')
    tg_id = models.PositiveBigIntegerField(unique=True)
    username = models.CharField(max_length=100, blank=True)
    language_code = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = 'telegram_clients'

    def __str__(self):
        return f'{self.__class__.__name__}: {self.pk}, {self.username}'
