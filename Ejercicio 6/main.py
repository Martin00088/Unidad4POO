from ManejadorProvincia import ManejadorProvincia
from vistaProvincia import ProvinciaView

if __name__ == '__main__':
    vista = ProvinciaView()
    manejador = ManejadorProvincia(vista)
    manejador.CargaLista()
    vista.setControlador(manejador)
    manejador.start()
