# Generated by Django 4.1.1 on 2022-09-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_detail_description_alter_todo_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AddField(
            model_name='todo',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='Дата удаления'),
        ),
        migrations.AddField(
            model_name='todo',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('Новая', 'New'), ('В работе', 'In Progress'), ('Завершена', 'Completed')], default='Новая', max_length=50, verbose_name='Статус'),
        ),
    ]
