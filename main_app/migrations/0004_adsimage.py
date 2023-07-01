# Generated by Django 4.2.2 on 2023-06-28 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_ads_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ads')),
                ('ads', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main_app.ads')),
            ],
        ),
    ]