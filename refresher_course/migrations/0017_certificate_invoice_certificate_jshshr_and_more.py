# Generated by Django 4.0.6 on 2023-02-23 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refresher_course', '0016_course_is_visible_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='invoice',
            field=models.BigIntegerField(blank=True, max_length=20, null=True, verbose_name='Invoice'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='jshshr',
            field=models.BigIntegerField(blank=True, max_length=14, null=True, verbose_name='Jshshr'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='passport',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Pasport'),
        ),
    ]