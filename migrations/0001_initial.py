# Generated by Django 3.2.12 on 2022-02-14 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apteks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharm_name', models.CharField(max_length=255)),
                ('pharm_city', models.CharField(max_length=255)),
                ('pharm_working_schedule', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('pharm_telephone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BePartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharm_name', models.CharField(max_length=255, verbose_name='Название вашей аптеки')),
                ('pharm_email', models.CharField(max_length=255, verbose_name='Почта вашей аптеки')),
                ('pharm_phone', models.CharField(max_length=255)),
                ('document', models.FileField(blank=True, upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(max_length=255, verbose_name='Your name')),
                ('person_email', models.CharField(max_length=255, verbose_name='Enter your email:')),
                ('person_tel', models.CharField(max_length=255, verbose_name='Enter your telephone number')),
                ('person_city', models.CharField(max_length=255, verbose_name='Enter your city')),
                ('person_Address', models.CharField(max_length=255, verbose_name='Enter your home address')),
                ('person_wish', models.TextField(verbose_name='Пожелания для доставки')),
                ('drug_name', models.CharField(max_length=255, verbose_name='Needed chemicals')),
            ],
        ),
        migrations.CreateModel(
            name='illness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('illness_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacy', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recomendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('user_email', models.CharField(max_length=255)),
                ('user_phone', models.CharField(max_length=255)),
                ('recommendations', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('name', models.CharField(max_length=255)),
                ('cost', models.CharField(max_length=200)),
                ('pharmacy', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('number', models.CharField(max_length=255)),
                ('ii_name', models.CharField(max_length=255)),
                ('illness', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='spharm.illness')),
            ],
        ),
    ]
