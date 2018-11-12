# Generated by Django 2.1.3 on 2018-11-10 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wode', '0001_initial'),
        ('shouye', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elaluate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gondsScore', models.IntegerField()),
                ('serviceScore', models.IntegerField()),
                ('content', models.CharField(max_length=120)),
                ('image', models.ImageField(default='', upload_to='')),
                ('isShow', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spnum', models.IntegerField()),
                ('zzje', models.IntegerField()),
                ('order_status', models.CharField(max_length=20)),
                ('order_nu', models.IntegerField()),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wode.Customer')),
                ('f_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shouye.Food')),
                ('sname_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shouye.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='Order_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wode.xf_Address')),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wode.Customer')),
                ('f_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shouye.Food')),
                ('order_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dingdan.Order')),
                ('sname_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shouye.Seller')),
            ],
        ),
        migrations.AddField(
            model_name='history',
            name='order_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dingdan.Order'),
        ),
        migrations.AddField(
            model_name='elaluate',
            name='orderid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dingdan.Order'),
        ),
        migrations.AddField(
            model_name='elaluate',
            name='shopid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shouye.Seller'),
        ),
        migrations.AddField(
            model_name='elaluate',
            name='userid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wode.Customer'),
        ),
    ]
