# Generated by Django 4.0.1 on 2022-06-21 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Kurs nomi')),
                ('slug', models.SlugField()),
                ('img', models.ImageField(upload_to='courses/')),
                ('sub_title', models.CharField(blank=True, max_length=100, verbose_name="Kurs nomi pasiga so'z ixtiyoriy")),
                ('about1', models.TextField(verbose_name='Kurs haqida 1')),
                ('about2', models.TextField(blank=True, verbose_name='Kurs haqida 2 ixtiyoriy')),
                ('to_students_title', models.CharField(blank=True, max_length=100, verbose_name="O'quvchilar uchun matn sarlavhasi ixtiyoriy")),
                ('to_students_text', models.TextField(blank=True, verbose_name="O'quvchilar uchun matn asosiy ixtiyoriy")),
                ('course_date', models.CharField(max_length=200, verbose_name='Kurs davom etish vaqti')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
