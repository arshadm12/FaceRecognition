# Generated by Django 2.2.5 on 2020-04-26 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0015_auto_20200425_0851'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='marksclass',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='marksclass',
            name='assign',
        ),
        migrations.DeleteModel(
            name='Marks',
        ),
        migrations.DeleteModel(
            name='MarksClass',
        ),
    ]
