# Generated by Django 4.2.1 on 2023-05-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "user_id",
                    models.CharField(max_length=18, unique=True, verbose_name="아이디"),
                ),
                (
                    "nick_name",
                    models.CharField(max_length=10, null=True, verbose_name="닉네임"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=128, null=True, unique=True, verbose_name="이메일"
                    ),
                ),
                ("phone_num", models.IntegerField(null=True, verbose_name="전화번호")),
                ("is_active", models.BooleanField(default=True)),
                ("is_admin", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]