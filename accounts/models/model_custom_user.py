from django.contrib.auth.models import AbstractUser
from accounts.managers import CustomUserManager
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    objects = CustomUserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        """ return  full name user """
        return f"{self.first_name} {self.last_name}"
