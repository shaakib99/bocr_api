from django.db import models
from django.core.validators import RegexValidator
from bocr_api.common.datetime import DateTime


class Users(models.Model):
    id = models.AutoField(primary_key=True, unique=True, auto_created=True)
    name = models.CharField(validators=[RegexValidator("^[a-zA-Z]{2,20}$")],
                            max_length=20)
    email = models.EmailField(unique=True)
    password = models.TextField(validators=[
        RegexValidator(
            regex=
            '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',
            message=
            "Password should be alphanumeric with at least one capital letter, small letter, digit & special character."
        )
    ])
    phone_number = models.TextField(null=True)
    password_reset_token = models.TextField(null=True)
    password_reset_token_generated_at = models.FloatField(null=True)
    verification_token = models.TextField(null=True)
    verification_token_generated_at = models.FloatField(null=True)
    profile_pic = models.TextField(null=True)
    cover_pic = models.TextField(null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.FloatField(default=DateTime.now())
    updated_at = models.FloatField(default=DateTime.now())
