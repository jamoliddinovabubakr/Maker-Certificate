# Generated by Django 4.0.6 on 2023-01-30 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refresher_course', '0003_alter_certificate_month_alter_certificate_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecomplete',
            name='month',
            field=models.CharField(choices=[('yanvar', 'Yanvar'), ('fevral', 'Fevral'), ('mart', 'Mart'), ('aprel', 'Aprel'), ('may', 'May'), ('iyun', 'Iyun'), ('iyul', 'Iyul'), ('avgust', 'Avgust'), ('sentabr', 'Sentabr'), ('oktabr', 'Oktabr'), ('noyabr', 'Noyabr'), ('dekabr', 'Dekabr')], default='yanvar', max_length=50, verbose_name='Oy'),
        ),
        migrations.AlterField(
            model_name='coursecomplete',
            name='year',
            field=models.CharField(choices=[('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027')], default='2022', max_length=4, verbose_name='Yil'),
        ),
    ]
