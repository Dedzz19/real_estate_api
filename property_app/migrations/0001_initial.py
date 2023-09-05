# Generated by Django 4.2.4 on 2023-09-05 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('description', models.TextField()),
                ('property_type', models.CharField(choices=[('Land', 'Land'), ('House', 'House'), ('Flat/Apartment', 'Flat/Apartment'), ('Commercial Property', 'Commercial Property')], max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('state', models.CharField(choices=[('Lagos', 'Lagos'), ('Abuja', 'Abuja'), ('Ogun', 'Ogun'), ('Edo', 'Edo')], default='Lagos', max_length=100)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property', to='user_app.agent')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='property_images/')),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='property_app.property')),
            ],
        ),
    ]
