from entidad.Usuario import Usuario
from orden import Carrito
from gestorAplicacion.entidad.Usuario.tiposDeUsuario.comprador.Membresia import Membresia
from baseDatos.Impl.CompradorRepositorio import CompradorRepositorio

class Comprador(Usuario):
    def __init__(self, id, nombre, apellido, correo, membresia=Membresia.NINGUNA, saldo=100):
        super().__init__(id, nombre, apellido, correo)
        self._membresia = membresia
        self._saldo = saldo
        self._ordenes = []  
        self._devoluciones = []  
        self._resenasDeProductos = []
        self._productosComprados = []
        self._carrito = Carrito(id, self)

    def agregarProductoComprado(self,productoComprado):
        self._productosComprados.append(productoComprado)
    
    def getResenasDeProductos(self):
        return self._resenasDeProductos
    
    def getMembresia(self):
        return self._membresia
    
    def getOrdenes(self):
        return self._ordenes
   
    def obtenerCompradores(self):
        return CompradorRepositorio.obtenerCompradores
    
    
    def MasCompradorValor():
        comprasValorMaximo = 0
        masComprador = None

        for comprador in CompradorRepositorio.obtenerCompradores():
            comprasValor = 0

            for orden in comprador.getOrdenes():
                for productoTransaccion in orden.getProductoTransaccion():
                    comprasValor += productoTransaccion().getPublicacion().precio()

            if comprasValor > comprasValorMaximo:
                comprasValorMaximo = comprasValor
                masComprador = comprador

        if masComprador:
            return f"{masComprador.nombre} {masComprador.apellido} ha realizado compras por un valor máximo de {comprasValorMaximo}"
       
        else:
            return "No se encontró comprador con valor máximo de compras"
        
    def mas_comprador():

        tamanoOrdenes = 0
        masComprador = None

        for comprador in CompradorRepositorio.obtenerCompradores():
            if len(comprador.getOrdenes()) > tamanoOrdenes:
                tamanoOrdenes = len(comprador.getOrdenes())
                masComprador = comprador

        if masComprador:
            return f"{masComprador.nombre()} {masComprador.apellido()} con el ID {masComprador.getId()} y con el correo electrónico {masComprador.getCorreo()} con un total de {tamanoOrdenes} productos comprados"
        else:
            return "No se encontró comprador con órdenes"

        
        
    def agregarDevolucion(devolucion):
        if devolucion.get
    
    #Segui agregando implementaciones....
    