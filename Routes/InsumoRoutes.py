from flask import Blueprint
from Controllers.InsumoController import InsumoController


ins_bp = Blueprint('insumo_bp', __name__)


# Listar todos los insumos
@ins_bp.route('/', methods=['GET'])
def listarInsumos():
    return InsumoController.listar()


# Crear un insumo
@ins_bp.route('/', methods=['POST'])
def crearInsumo():
    return InsumoController.crear()


# Actualizar un insumo
@ins_bp.route('/', methods=['PUT'])
def actualizarInsumo():
    return InsumoController.actualizar()


# Eliminar un insumo
@ins_bp.route('/<int:id>', methods=['DELETE'])
def eliminarInsumo(id):
    return InsumoController.eliminar(id)


# Buscar insumo por código
@ins_bp.route('/codigo/<codigo>', methods=['GET'])
def buscarInsumoPorCodigo(codigo):
    return InsumoController.buscarPorCodigo(codigo)


# Listar insumos por tipo
@ins_bp.route('/tipo/<tipo_insumo>', methods=['GET'])
def listarInsumosPorTipo(tipo_insumo):
    return InsumoController.listarPorTipo(tipo_insumo)