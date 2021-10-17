# Generated by Django 3.2.7 on 2021-09-22 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.DateField()),
                ('monto', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'boleta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.AutoField(primary_key=True, serialize=False)),
                ('nom_ciudad', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'ciudad',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('c_rut', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.BigIntegerField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False)),
                ('nom_comuna', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentarios', models.CharField(blank=True, max_length=80, null=True)),
                ('cantidad', models.BigIntegerField()),
                ('estado_orden', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'detalle_orden',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleReceta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruccion', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'detalle_receta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_mesas', models.BigIntegerField()),
                ('estado_reserva', models.CharField(max_length=10)),
                ('cant_personas', models.BigIntegerField()),
            ],
            options={
                'db_table': 'detalle_reserva',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('e_rut', models.BigIntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('prim_nom', models.CharField(max_length=30)),
                ('seg_nom', models.CharField(blank=True, max_length=25, null=True)),
                ('prim_apell', models.CharField(max_length=30)),
                ('sec_apell', models.CharField(max_length=25)),
                ('genero', models.CharField(max_length=25)),
                ('telefono', models.BigIntegerField(blank=True, null=True)),
                ('fec_nac', models.CharField(max_length=30)),
                ('salario', models.BigIntegerField()),
                ('correo', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GuiaDespacho',
            fields=[
                ('id_envio', models.AutoField(primary_key=True, serialize=False)),
                ('tammanio', models.CharField(max_length=15)),
                ('gd_desc', models.CharField(blank=True, max_length=80, null=True)),
                ('cantidad', models.CharField(max_length=20)),
                ('u_medida', models.CharField(max_length=30)),
                ('precio', models.CharField(max_length=30)),
                ('monto_neto', models.CharField(max_length=20)),
                ('iva', models.BigIntegerField()),
                ('total', models.CharField(max_length=12)),
                ('fec_envio', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'guia_despacho',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id_ingrediente', models.AutoField(primary_key=True, serialize=False)),
                ('nom_ingrediente', models.CharField(max_length=40)),
                ('i_desc', models.CharField(max_length=60)),
                ('stock', models.BigIntegerField()),
                ('unidad_de_medida', models.CharField(max_length=20)),
                ('fec_caduc', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'ingrediente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id_menu', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_menu', models.CharField(max_length=30)),
                ('desde', models.DateField()),
                ('hasta', models.DateField()),
            ],
            options={
                'db_table': 'menu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id_menuitem', models.AutoField(primary_key=True, serialize=False)),
                ('mi_nombre', models.CharField(max_length=35)),
                ('mi_desc', models.CharField(max_length=80)),
                ('precio', models.CharField(max_length=10)),
                ('tamannio', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'menu_item',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id_mesa', models.AutoField(primary_key=True, serialize=False)),
                ('capacidad', models.BigIntegerField()),
                ('estareservada', models.FloatField()),
                ('tieneorden', models.FloatField()),
            ],
            options={
                'db_table': 'mesa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.CharField(max_length=16)),
                ('hora', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'orden',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('rut_social', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('giro', models.CharField(blank=True, max_length=30, null=True)),
                ('p_nombre', models.CharField(max_length=45)),
                ('descripcion', models.CharField(max_length=80)),
                ('p_correo', models.CharField(max_length=80)),
                ('p_telefono', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=60)),
                ('razon_social', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id_receta', models.AutoField(primary_key=True, serialize=False)),
                ('nom_receta', models.CharField(max_length=20)),
                ('porcion', models.CharField(max_length=25)),
                ('r_desc', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'receta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('nom_region', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('fec_reserv_hecha', models.DateField()),
                ('fec_reser', models.DateField()),
                ('origen_reserv', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'reserva',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RolEmpleado',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('rol_desc', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'rol_empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Suministro',
            fields=[
                ('id_suministro', models.AutoField(primary_key=True, serialize=False)),
                ('tamannio', models.CharField(max_length=25)),
                ('nombre', models.CharField(max_length=40)),
                ('s_desc', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'suministro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id_transaccion', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.DateField()),
                ('tipo_pago', models.CharField(max_length=30)),
                ('monto', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'transaccion',
                'managed': False,
            },
        ),
    ]
