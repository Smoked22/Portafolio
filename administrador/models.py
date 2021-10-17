from django.db import models


class Boleta(models.Model):
    id_boleta = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.DateField()
    monto = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'boleta'


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nom_ciudad = models.CharField(max_length=40)
    comuna_id_comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='comuna_id_comuna', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cliente(models.Model):
    c_rut = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    telefono = models.BigIntegerField(blank=True, null=True)
    correo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nom_comuna = models.CharField(max_length=40)
    region_id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='region_id_region', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comuna'


class DetalleOrden(models.Model):
    comentarios = models.CharField(max_length=80, blank=True, null=True)
    cantidad = models.BigIntegerField()
    estado_orden = models.CharField(max_length=25)
    orden_id_orden = models.ForeignKey('Orden', models.DO_NOTHING, db_column='orden_id_orden', blank=True, null=True)
    menu_item_id_menuitem = models.ForeignKey('MenuItem', models.DO_NOTHING, db_column='menu_item_id_menuitem', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_orden'


class DetalleReceta(models.Model):
    instruccion = models.CharField(max_length=400)
    receta_id_receta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='receta_id_receta', blank=True, null=True)
    ingrediente_id_ingrediente = models.ForeignKey('Ingrediente', models.DO_NOTHING, db_column='ingrediente_id_ingrediente', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_receta'


class DetalleReserva(models.Model):
    cant_mesas = models.BigIntegerField()
    estado_reserva = models.CharField(max_length=10)
    mesa_id_mesa = models.ForeignKey('Mesa', models.DO_NOTHING, db_column='mesa_id_mesa', blank=True, null=True)
    reserva_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='reserva_id_reserva', blank=True, null=True)
    cant_personas = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'detalle_reserva'


class Empleado(models.Model):
    e_rut = models.BigIntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    prim_nom = models.CharField(max_length=30)
    seg_nom = models.CharField(max_length=25, blank=True, null=True)
    prim_apell = models.CharField(max_length=30)
    sec_apell = models.CharField(max_length=25)
    genero = models.CharField(max_length=25)
    telefono = models.BigIntegerField(blank=True, null=True)
    fec_nac = models.CharField(max_length=30)
    salario = models.BigIntegerField()
    rol_empleado_id_rol = models.ForeignKey('RolEmpleado', models.DO_NOTHING, db_column='rol_empleado_id_rol')
    correo = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado'


class GuiaDespacho(models.Model):
    id_envio = models.AutoField(primary_key=True)
    tammanio = models.CharField(max_length=15)
    gd_desc = models.CharField(max_length=80, blank=True, null=True)
    cantidad = models.CharField(max_length=20)
    u_medida = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)
    monto_neto = models.CharField(max_length=20)
    iva = models.BigIntegerField()
    total = models.CharField(max_length=12)
    suministro_id_sumplemento = models.ForeignKey('Suministro', models.DO_NOTHING, db_column='suministro_id_sumplemento', blank=True, null=True)
    fec_envio = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'guia_despacho'


class Ingrediente(models.Model):
    id_ingrediente = models.AutoField(primary_key=True)
    nom_ingrediente = models.CharField(max_length=40)
    i_desc = models.CharField(max_length=60)
    stock = models.BigIntegerField()
    unidad_de_medida = models.CharField(max_length=20)
    guia_despacho_id_envio = models.ForeignKey(GuiaDespacho, models.DO_NOTHING, db_column='guia_despacho_id_envio', blank=True, null=True)
    fec_caduc = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'ingrediente'


class Menu(models.Model):
    id_menu = models.AutoField(primary_key=True)
    tipo_menu = models.CharField(max_length=30)
    desde = models.DateField()
    hasta = models.DateField()

    class Meta:
        managed = False
        db_table = 'menu'


class MenuItem(models.Model):
    id_menuitem = models.AutoField(primary_key=True)
    mi_nombre = models.CharField(max_length=35)
    mi_desc = models.CharField(max_length=80)
    precio = models.CharField(max_length=10)
    tamannio = models.CharField(max_length=20)
    menu_id_menu = models.ForeignKey(Menu, models.DO_NOTHING, db_column='menu_id_menu', blank=True, null=True)
    receta_id_receta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='receta_id_receta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_item'


class Mesa(models.Model):
    id_mesa = models.AutoField(primary_key=True)
    capacidad = models.BigIntegerField()
    estareservada = models.FloatField()
    tieneorden = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mesa'


class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    fecha = models.CharField(max_length=16)
    hora = models.CharField(max_length=16)
    mesa_id_mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='mesa_id_mesa', blank=True, null=True)
    boleta_id_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='boleta_id_boleta')

    class Meta:
        managed = False
        db_table = 'orden'


class Proveedor(models.Model):
    rut_social = models.CharField(primary_key=True, max_length=18)
    giro = models.CharField(max_length=30, blank=True, null=True)
    p_nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=80)
    p_correo = models.CharField(max_length=80)
    p_telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=60)
    ciudad_id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_id_ciudad', blank=True, null=True)
    razon_social = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Receta(models.Model):
    id_receta = models.AutoField(primary_key=True)
    nom_receta = models.CharField(max_length=20)
    porcion = models.CharField(max_length=25)
    r_desc = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'receta'


class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nom_region = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'region'


class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    fec_reserv_hecha = models.DateField()
    fec_reser = models.DateField()
    empleado_e_rut = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_e_rut', blank=True, null=True)
    cliente_c_rut = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_c_rut')
    origen_reserv = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'reserva'


class RolEmpleado(models.Model):
    id_rol = models.AutoField(primary_key=True)
    rol_desc = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'rol_empleado'


class Suministro(models.Model):
    id_suministro = models.AutoField(primary_key=True)
    tamannio = models.CharField(max_length=25)
    nombre = models.CharField(max_length=40)
    s_desc = models.CharField(max_length=80, blank=True, null=True)
    proveedor_rut_social = models.ForeignKey(Proveedor, models.DO_NOTHING, db_column='proveedor_rut_social', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suministro'


class Transaccion(models.Model):
    id_transaccion = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.DateField()
    tipo_pago = models.CharField(max_length=30)
    monto = models.CharField(max_length=12)
    boleta_id_boleta = models.ForeignKey(Boleta, models.DO_NOTHING, db_column='boleta_id_boleta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaccion'

class Usuario(models.Model):
    rut = models.CharField(max_length=16,unique=True)
    Nombre_de_usuario = models.CharField(max_length=25)
    password = models.CharField(max_length=40)

    def str(self):
        return self.Nombre_de_usuario
