# Generated by Django 5.0.6 on 2024-05-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(blank=True, max_length=60)),
                ('company', models.CharField(blank=True, max_length=60)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('web', models.URLField(blank=True)),
                ('description', models.TextField()),
                ('sitestatus', models.CharField(choices=[('NEW', 'New Site'), ('EX', 'Existing Site')], max_length=20)),
                ('priority', models.CharField(choices=[('U', 'Urgent - 1 week or less'), ('N', 'Normal - 2 to 4 weeks'), ('L', 'Low - Still Researching')], max_length=40)),
                ('jobfile', models.FileField(blank=True, upload_to='uploads/')),
                ('submitted', models.DateField(auto_now_add=True)),
                ('quotedate', models.DateField(blank=True, null=True)),
                ('quoteprice', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7)),
            ],
        ),
    ]
