from ManejadorPaciente import ManejadorPaciente
from vistaPaciente import PacientesView

if __name__ == '__main__':
    vista = PacientesView()
    manejador = ManejadorPaciente(vista)
    manejador.CargaLista()
    vista.setControlador(manejador)
    manejador.start()
