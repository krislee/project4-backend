# Generated by Django 3.1.1 on 2020-09-16 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_book_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.IntegerField(default=2),
        ),
    ]
