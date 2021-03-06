# Generated by Django 4.0 on 2022-02-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_delete_newuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('confirmpassword', models.CharField(max_length=200)),
                ('phone_no', models.IntegerField(max_length=20)),
            ],
        ),
    ]
