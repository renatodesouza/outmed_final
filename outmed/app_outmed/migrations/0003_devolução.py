# Generated by Django 2.2.3 on 2019-08-13 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_outmed', '0002_auto_20190812_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devolução',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.DateField(verbose_name='Data da venda')),
                ('Motivo', models.CharField(max_length=200, verbose_name='Motivo')),
                ('Titulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_outmed.Livros')),
                ('cod_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_outmed.Cliente')),
            ],
        ),
    ]
