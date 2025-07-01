from sqlalchemy import text
from database.database import DatabaseManager
from atividades.services import EscolaService


class ModelAtividades:

    def listar_atividades(self):
        return DatabaseManager().select_all("SELECT * FROM atividades")
      
    def get_atividade_por_id(self, id_atividade: int) -> dict:
        sql = f"SELECT * FROM atividades WHERE id_atividade = {id_atividade}"
        db = DatabaseManager()
        result = db.select_one(sql)
        if result:
            return dict(result._mapping)
        return {}
    
    def criar_atividade(self, professor_id: int, aluno_id: int, titulo_atividade: str) -> dict:
        # Valida aluno e professor
        valida_entidades = self.validar_entidades(aluno_id, professor_id)
        if valida_entidades != {}:
            return valida_entidades  # retorna o erro se houver

        # Monta SQL de insert
        sql = f"""
        INSERT INTO atividades (id_professor, id_aluno, titulo_atividade)
        VALUES ({professor_id}, {aluno_id}, '{titulo_atividade}')
        RETURNING id_atividade, id_professor, id_aluno, titulo_atividade
        """

        db = DatabaseManager()
        try:
            result = db.select_one(sql)
            if result:
                return dict(result._mapping)
            else:
                return {"error": "Erro ao criar atividade"}
        except Exception as e:
            return {"error": str(e)}

    
    def validar_entidades(self, aluno_id: int, professor_id: int) -> dict:

        response = EscolaService().validar_entidades(professor_id, aluno_id)

        if response["valida_aluno_status_code"] != 200:
            return {"error": "Aluno não existe"}
        
        if response["valida_professor_status_code"] != 200:
            return {"error": "Professor não existe"}
        
        return {}
