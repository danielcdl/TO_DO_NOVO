# Generated by Django 3.1.7 on 2021-05-21 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_novo_app', '0004_auto_20210521_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupos',
            name='sub_grupo',
        ),
        migrations.AddField(
            model_name='sub_grupos',
            name='grupo_sub',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grupo_sub', to='todo_novo_app.grupos'),
        ),
    ]