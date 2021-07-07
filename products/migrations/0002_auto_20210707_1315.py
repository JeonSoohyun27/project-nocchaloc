# Generated by Django 3.2.5 on 2021-07-07 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='create_at',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='hover_img_url',
            new_name='hover_image_url',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='main_img_url',
            new_name='main_image_url',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterModelTable(
            name='producttype',
            table='product_types',
        ),
    ]