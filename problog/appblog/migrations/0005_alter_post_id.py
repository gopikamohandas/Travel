# Generated by Django 5.1.2 on 2024-10-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appblog', '0004_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]