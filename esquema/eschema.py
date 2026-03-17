from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date


class Rol(BaseModel):
    nombre_rol: str

    class Config:
        from_attributes = True


class Usuario(BaseModel):
    nombre: str
    correo: str
    password: str
    telefono: Optional[str] = None
    id_rol: Optional[int] = None

    class Config:
        from_attributes = True


class Categoria(BaseModel):
    nombre_categoria: str
    descripcion: Optional[str] = None

    class Config:
        from_attributes = True


class Producto(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int
    fecha_cosecha: Optional[date] = None
    fecha_vencimiento: Optional[date] = None
    imagen: Optional[str] = None
    id_categoria: Optional[int] = None

    class Config:
        from_attributes = True


class PuntoEntrega(BaseModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    ciudad: Optional[str] = None

    class Config:
        from_attributes = True


class Pedido(BaseModel):
    id_usuario: Optional[int] = None
    estado: Optional[str] = None
    total: Optional[float] = None
    id_punto_entrega: Optional[int] = None

    class Config:
        from_attributes = True