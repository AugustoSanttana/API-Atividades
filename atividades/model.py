from database.database import db

class ModelAtividades:
    def listar_atividades(self) -> list:
        return db

    def criar_atividade(self, atividade: dict) -> dict:
        db[].append(atividade)
        return atividade
      
    def get_atividade_id(self, id_atividade: int) -> dict:
        for atividade in db:
            if db['id_atividade'] == id_atividade:
                return atividade
        return {}
    
    def criar_atividade(self, atividade: dict) -> dict:
        db.append(atividade)
        return atividade
    """def validar_entidades(self, turma_id: int, professor_id: int) -> dict:

        response = reservasService().validar_entidades(turma_id, professor_id)

        if response["valida_turma_status_code"] != 200:
            return {"error": "Turma não existe"}
        
        if response["valida_professor_status_code"] != 200:
            return {"error": "Professor não existe"}
        
        return {}"""
