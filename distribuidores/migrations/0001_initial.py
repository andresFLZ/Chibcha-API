# Generated by Django 4.2.7 on 2023-12-01 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('metodosDePago', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_Categoria', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombreCategoria', models.CharField(max_length=20, verbose_name='nombre de categoría')),
                ('comision_pct', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='comisión')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'db_table': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Distribuidor',
            fields=[
                ('id_distri', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombreDistr', models.CharField(max_length=20, verbose_name='Nombre del distribuidor')),
                ('numeroDominios', models.IntegerField(blank=True, default=0, null=True, verbose_name='Numero de dominios')),
                ('correo', models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='Correo corporativo')),
                ('solicitud', models.BooleanField(default=True, verbose_name='solicitud para ser distribuidor')),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distribuidores.categoria', verbose_name='Categoría')),
                ('id_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuarios', verbose_name='usuario')),
            ],
            options={
                'verbose_name': 'distribuidor',
                'verbose_name_plural': 'distribuidores',
                'db_table': 'Distribuidor',
            },
        ),
        migrations.CreateModel(
            name='PagoComisiones',
            fields=[
                ('id_comision', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('ValorPagar', models.IntegerField(blank=True, default=0, null=True, verbose_name='Valor a pagar')),
                ('pagado', models.BooleanField(default=False, verbose_name='Esta pagado')),
                ('id_distri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distribuidores.distribuidor', verbose_name='Distribuidor')),
                ('id_metodoDePago', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='metodosDePago.metodosdepago', verbose_name='Método de pago')),
            ],
            options={
                'verbose_name': 'PagoComision',
                'verbose_name_plural': 'PagoComisiones',
                'db_table': 'Pagocomisiones',
            },
        ),
    ]
