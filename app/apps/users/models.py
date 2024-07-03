import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from config.settings import settings


class ClientManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError("Поле электронной почты должно быть заполнено")
        email = self.normalize_email(email)
        user = self.model(
            email=email, first_name=first_name, last_name=last_name, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, first_name, last_name, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперпользователь должен иметь is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Суперпользователь должен иметь is_superuser=True.")

        return self.create_user(email, first_name, last_name, password, **extra_fields)


class Client(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(default=False, max_length=12)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = ClientManager()

    def __str__(self):
        return self.first_name


class UserProxyManager(models.Manager):
    def get_or_create(self, request):
        if anon := not request.user.is_authenticated:
            session = request.session
            session_data = session.get(settings.USER_SESSION_ID)
            if session_data is None:
                session_data = {"uuid": str(uuid.uuid4())}
                session[settings.USER_SESSION_ID] = session_data
            session_uuid = session_data["uuid"]
            user, created = super().get_or_create(session=session_uuid)
        else:
            user, created = super().get_or_create(user=request.user)
        return user, created, anon


class UserProxy(models.Model):
    user = models.OneToOneField(Client, on_delete=models.CASCADE, null=True)
    session = models.CharField(max_length=40, null=True)
    objects = UserProxyManager()
