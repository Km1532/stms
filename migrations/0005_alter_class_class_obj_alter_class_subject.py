# Generated by Django 4.2.8 on 2024-02-08 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_schedule_app', '0004_class_class_obj_class_day_class_subject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_obj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school_schedule_app.class'),
        ),
        migrations.AlterField(
            model_name='class',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_schedule_app.subject'),
        ),
    ]
