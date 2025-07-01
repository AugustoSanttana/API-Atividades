import requests

EscolaService_URL = "http://localhost:8000"

class EscolaService:

    def validar_entidades(self, professor_id: int, aluno_id: int) -> dict:

        valida_aluno = requests.get(f"http://localhost:8000/alunos/{aluno_id}")
        valida_professor = requests.get(f"http://localhost:8000/professores/{professor_id}")

        return {"valida_aluno_status_code": valida_aluno.status_code,
                "valida_professor_status_code": valida_professor.status_code}