# Generated by Django 4.0 on 2022-02-05 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_comment_date_created_alter_comment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='rating',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
