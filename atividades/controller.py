from flask import Blueprint, jsonify, request
from atividades.model import ModelAtividades

atividades_blueprint = Blueprint('atividades', __name__)

@atividades_blueprint.route('/atividades', methods=['GET'])
def listar_atividades():
    atividades = ModelAtividades().listar_atividades()

    if not atividades:
        return jsonify(msg="nenhuma atividade encontrada"), 200

    return jsonify([atividade._asdict() for atividade in atividades]), 200

@atividades_blueprint.route('/atividades/<int:id_atividade>', methods=['GET'])
def get_atividade_id(id_atividade):
    atividade = ModelAtividades().get_atividade_por_id(id_atividade)
    if not atividade:
        return jsonify({'error': 'Atividade não encontrada'}), 404
    return jsonify(atividade), 200
  
@atividades_blueprint.route('/atividades', methods=['POST'])
def criar_atividade():
    data = request.get_json()
    professor_id = data.get("id_professor", "")
    aluno_id = data.get("id_aluno", "")
    titulo_atividade = data.get("titulo_atividade", "")
    response = ModelAtividades().criar_atividade(professor_id, aluno_id, titulo_atividade)

    if response.get("error"):
        return jsonify(response), 404
    
    return jsonify(response), 201
  