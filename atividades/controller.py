from flask import Blueprint, jsonify
from atividades.model import ModelAtividades

atividades_blueprint = Blueprint('atividades', __name__)

atividades_blueprint.route('/', methods=['GET'])
def listar_atividades():
    atividades = ModelAtividades.listar_atividades()
    return jsonify(atividades)

atividades_blueprint.route('/atividade/<int:id_atividade>', methods=['GET'])
def get_atividade_id(id_atividade):
  atividade = ModelAtividades.get_atividade_id(id_atividade)
  if not atividade:
      return jsonify({'error': 'Atividade não encontrada'}), 404
  return jsonify(atividade)
  
atividades_blueprint.route('/atividade', methods=['POST'])
def criar_atividade():
    atividade = ModelAtividades.criar_atividade()
    if not atividade:
        return jsonify({'error': 'Erro ao criar atividade'}), 400
    return jsonify(atividade), 201
  
atividades_blueprint.route('/atividade/<int:id_atividade>/professor', methods=['PUT'])