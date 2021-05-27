# Generated by Django 3.1.7 on 2021-04-02 08:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=15, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20, verbose_name='User Name')),
                ('phone', models.CharField(max_length=25, verbose_name='User Phone Number')),
                ('address', models.CharField(max_length=150, verbose_name='User Address')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Product Name')),
                ('description', models.TextField(max_length=2000, verbose_name='Product Description')),
                ('remainder', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Product Remainder')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Product Price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_category', to='shop.category', verbose_name='Product Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='OrderProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Product Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='shop.order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to='shop.product', verbose_name='Product to Buy')),
            ],
            options={
                'verbose_name': 'Order_Product',
                'verbose_name_plural': 'Order_Products',
                'db_table': 'order_products',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantity of item')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_product', to='shop.product', verbose_name='Product in Cart')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'db_table': 'items',
            },
        ),
    ]
