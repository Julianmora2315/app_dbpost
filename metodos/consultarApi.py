from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from modelos import modelo_producto
from esquema import eschema

router = APIRouter()


# ─── ROLES ───────────────────────────────────────────
@router.get("/roles")
def get_roles(db: Session = Depends(get_db)):
    return db.query(modelo_producto.Rol).all()

@router.get("/roles/{id_rol}")
def get_rol(id_rol: int, db: Session = Depends(get_db)):
    rol = db.query(modelo_producto.Rol).filter(modelo_producto.Rol.id_rol == id_rol).first()
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol

@router.post("/roles")
def crear_rol(rol: eschema.Rol, db: Session = Depends(get_db)):
    nuevo = modelo_producto.Rol(nombre_rol=rol.nombre_rol)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.delete("/roles/{id_rol}")
def borrar_rol(id_rol: int, db: Session = Depends(get_db)):
    item = db.query(modelo_producto.Rol).filter(modelo_producto.Rol.id_rol == id_rol).first()
    if not item:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    db.delete(item)
    db.commit()
    return f"Rol {id_rol} eliminado"


# ─── USUARIOS ────────────────────────────────────────
@router.get("/usuarios")
def get_usuarios(db: Session = Depends(get_db)):
    return db.query(modelo_producto.Usuario).all()

@router.get("/usuarios/{id_usuario}")
def get_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(modelo_producto.Usuario).filter(modelo_producto.Usuario.id_usuario == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/usuarios")
def crear_usuario(usuario: eschema.Usuario, db: Session = Depends(get_db)):
    nuevo = modelo_producto.Usuario(
        nombre=usuario.nombre,
        correo=usuario.correo,
        password=usuario.password,
        telefono=usuario.telefono,
        id_rol=usuario.id_rol
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.delete("/usuarios/{id_usuario}")
def borrar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    item = db.query(modelo_producto.Usuario).filter(modelo_producto.Usuario.id_usuario == id_usuario).first()
    if not item:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(item)
    db.commit()
    return f"Usuario {id_usuario} eliminado"


# ─── CATEGORIAS ──────────────────────────────────────
@router.get("/categorias")
def get_categorias(db: Session = Depends(get_db)):
    return db.query(modelo_producto.Categoria).all()

@router.post("/categorias")
def crear_categoria(categoria: eschema.Categoria, db: Session = Depends(get_db)):
    nuevo = modelo_producto.Categoria(
        nombre_categoria=categoria.nombre_categoria,
        descripcion=categoria.descripcion
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.delete("/categorias/{id_categoria}")
def borrar_categoria(id_categoria: int, db: Session = Depends(get_db)):
    item = db.query(modelo_producto.Categoria).filter(modelo_producto.Categoria.id_categoria == id_categoria).first()
    if not item:
        raise HTTPException(status_code=404, detail="Categoria no encontrada")
    db.delete(item)
    db.commit()
    return f"Categoria {id_categoria} eliminada"


# ─── PRODUCTOS ───────────────────────────────────────
@router.get("/productos")
def get_productos(db: Session = Depends(get_db)):
    return db.query(modelo_producto.Producto).all()

@router.get("/productos/{id_producto}")
def get_producto(id_producto: int, db: Session = Depends(get_db)):
    producto = db.query(modelo_producto.Producto).filter(modelo_producto.Producto.id_producto == id_producto).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@router.post("/productos")
def crear_producto(producto: eschema.Producto, db: Session = Depends(get_db)):
    nuevo = modelo_producto.Producto(
        nombre=producto.nombre,
        descripcion=producto.descripcion,
        precio=producto.precio,
        stock=producto.stock,
        fecha_cosecha=producto.fecha_cosecha,
        fecha_vencimiento=producto.fecha_vencimiento,
        imagen=producto.imagen,
        id_categoria=producto.id_categoria
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.delete("/productos/{id_producto}")
def borrar_producto(id_producto: int, db: Session = Depends(get_db)):
    item = db.query(modelo_producto.Producto).filter(modelo_producto.Producto.id_producto == id_producto).first()
    if not item:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(item)
    db.commit()
    return f"Producto {id_producto} eliminado"


# ─── PUNTOS DE ENTREGA ───────────────────────────────
@router.get("/puntos")
def get_puntos(db: Session = Depends(get_db)):
    return db.query(modelo_producto.PuntoEntrega).all()

@router.post("/puntos")
def crear_punto(punto: eschema.PuntoEntrega, db: Session = Depends(get_db)):
    nuevo = modelo_producto.PuntoEntrega(
        nombre=punto.nombre,
        direccion=punto.direccion,
        ciudad=punto.ciudad
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.delete("/puntos/{id_punto}")
def borrar_punto(id_punto: int, db: Session = Depends(get_db)):
    item = db.query(modelo_producto.PuntoEntrega).filter(modelo_producto.PuntoEntrega.id_punto == id_punto).first()
    if not item:
        raise HTTPException(status_code=404, detail="Punto no encontrado")
    db.delete(item)
    db.commit()
    return f"Punto {id_punto} eliminado"


# ─── PEDIDOS ─────────────────────────────────────────
@router.get("/pedidos")
def get_pedidos(db: Session = Depends(get_db)):
    return db.query(modelo_producto.Pedido).all()

@router.post("/pedidos")
def crear_pedido(pedido: eschema.Pedido, db: Session = Depends(get_db)):
    nuevo = modelo_producto.Pedido(
        id_usuario=pedido.id_usuario,
        estado=pedido.estado,
        total=pedido.total,
        id_punto_entrega=pedido.id_punto_entrega
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.delete("/pedidos/{id_pedido}")
def borrar_pedido(id_pedido: int, db: Session = Depends(get_db)):
    item = db.query(modelo_producto.Pedido).filter(modelo_producto.Pedido.id_pedido == id_pedido).first()
    if not item:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    db.delete(item)
    db.commit()
    return f"Pedido {id_pedido} eliminado"