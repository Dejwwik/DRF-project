# Generated by Django 5.1.6 on 2025-02-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=120)),
                ('content', models.TextField(blank=True, max_length=500, null=True)),
                ('price', models.DecimalField(decimal_places=5, max_digits=15)),
            ],
        ),
    ]
