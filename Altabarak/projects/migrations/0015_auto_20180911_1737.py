# Generated by Django 2.0.6 on 2018-09-12 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20180910_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=60)),
                ('e_mail', models.EmailField(max_length=254)),
                ('text', models.CharField(max_length=500)),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
