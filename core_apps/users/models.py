# from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from django.core.validators import RegexValidator
# import uuid

# class User(AbstractUser):
    

#     pkid = models.BigAutoField(primary_key=True, editable=False)
#     id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     email = models.EmailField(_("Email Address"), unique=True, db_index=True)
#     mobile = models.CharField(_("Mobile Number"), max_length=15, unique=True)
#     username = models.CharField(
#         _("Username"),
#         max_length=60,
#         unique=True,
#         validators=[RegexValidator(
#             regex=r'^[\w.@+-]+$',
#             message=_("Enter a valid username."),
#         )],
#     )

#     role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.USER)
#     assigned_admin = models.ForeignKey(
#         'self',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='assigned_users'
#     )

#     # Override these to prevent reverse accessor clashes
#     groups = models.ManyToManyField(
#         Group,
#         related_name='customuser_set',
#         blank=True,
#         help_text=_('The groups this user belongs to.'),
#         verbose_name=_('groups'),
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         related_name='customuser_permissions',
#         blank=True,
#         help_text=_('Specific permissions for this user.'),
#         verbose_name=_('user permissions'),
#     )

#     REQUIRED_FIELDS = ['email', 'mobile']
#     USERNAME_FIELD = 'username'

#     def __str__(self):
#         return self.username

#     def is_superadmin(self):
#         return self.role == 'superadmin'

#     def is_admin(self):
#         return self.role == 'admin'

#     def is_user(self):
#         return self.role == 'user'

import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils.translation import gettext_lazy as _
from core_apps.users.managers import UserManager


class UsernameValidator(validators.RegexValidator):
    regex = r"^[\w.@+-]+\Z"
    message = _(
        "Your username is not valid. A username can only contain letters, numbers, a dot, "
        "@ symbol, + symbol and a hyphen."
    )
    flag = 0


class User(AbstractUser):
    class Roles(models.TextChoices):
        SUPERADMIN = "superadmin", "SuperAdmin"
        ADMIN = "admin", "Admin"
        USER = "user", "User"
        
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # UUID for uniqueness
    name = models.CharField(verbose_name=_("Full Name"), max_length=120)  # Single name field
    email = models.EmailField(verbose_name=_("Email Address"), unique=True, db_index=True)
    mobile = models.CharField(verbose_name=_("Mobile Number"), max_length=15, unique=True)  # Mobile number added
    username = models.CharField(
        verbose_name=_("Username"),
        max_length=60,
        unique=True,
        validators=[UsernameValidator()],
    )
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.USER)
    assigned_admin = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='assigned_users'
    )
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name", "mobile","email"]

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-date_joined"]

    def __str__(self):
        return self.email