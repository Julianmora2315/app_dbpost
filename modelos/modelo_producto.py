from sqlalchemy import Column, Integer, String, Text, DateTime, Date, DECIMAL, ForeignKey
from sqlalchemy.sql import func
from database import Base


class Rol(Base):
    __tablename__ = "roles"
    id_rol = Column(Integer, primary_key=True, autoincrement=True)
    nombre_rol = Column(String(50), nullable=False)


class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    telefono = Column(String(20))
    fecha_registro = Column(DateTime, default=func.now())
    id_rol = Column(Integer, ForeignKey("roles.id_rol"))


class Categoria(Base):
    __tablename__ = "categorias"
    id_categoria = Column(Integer, primary_key=True, autoincrement=True)
    nombre_categoria = Column(String(100), nullable=False)
    descripcion = Column(Text)


class Producto(Base):
    __tablename__ = "productos"
    id_producto = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    precio = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)
    fecha_cosecha = Column(Date)
    fecha_vencimiento = Column(Date)
    imagen = Column(String(255))
    id_categoria = Column(Integer, ForeignKey("categorias.id_categoria"))


class Carrito(Base):
    __tablename__ = "carrito"
    id_carrito = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    fecha_creacion = Column(DateTime, default=func.now())


class DetalleCarrito(Base):
    __tablename__ = "detalle_carrito"
    id_detalle_carrito = Column(Integer, primary_key=True, autoincrement=True)
    id_carrito = Column(Integer, ForeignKey("carrito.id_carrito"))
    id_producto = Column(Integer, ForeignKey("productos.id_producto"))
    cantidad = Column(Integer, nullable=False)


class PuntoEntrega(Base):
    __tablename__ = "puntos_entrega"
    id_punto = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    direccion = Column(String(150))
    ciudad = Column(String(100))


class Pedido(Base):
    __tablename__ = "pedidos"
    id_pedido = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"))
    fecha_pedido = Column(DateTime, default=func.now())
    e