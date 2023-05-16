# Generated by Django 4.2 on 2023-05-16 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_investor_assertivo_investor_conservador_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investor',
            name='assertivo',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='conservador',
        ),
        migrations.RemoveField(
            model_name='investor',
            name='moderador',
        ),
        migrations.AlterField(
            model_name='investor',
            name='perfil',
            field=models.CharField(choices=[('c', 'Conservador'), ('m', 'Moderador'), ('a', 'assertivo')], default='', max_length=20),
        ),
    ]
