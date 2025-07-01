## Descrição da API

A API de Atividades é responsável por gerenciar atividades associadas a professores e alunos. Ela permite listar todas as atividades, buscar uma atividade por ID e criar novas atividades. A validação das entidades (aluno e professor) é feita por meio de requisições a outro microsserviço.


## Instruções de Execução com Docker

### Pré-requisitos

* Docker
* Docker Compose

### Passos para executar o projeto

1. Clone este repositório:


git clone https://github.com/AugustoSanttana/API-Atividades



2. Execute o Docker Compose:


docker-compose up --build

## Arquitetura Utilizada

O projeto segue uma arquitetura modular baseada em:

* Blueprints do Flask: para separar rotas de atividades.
* Camada de Modelos: responsável por interações com o banco de dados.
* Validação Externa via HTTP: a API de atividades faz chamadas para outra API (API de Escola) para validar alunos e professores.
* SQLAlchemy com execução direta de SQL: utilizado para realizar queries com maior controle e performance.
* Docker: para facilitar a configuração e orquestração dos serviços.



## 🔗 Integração entre Microsserviços

O sistema é composto por dois microsserviços principais:

### 1. API de Atividades (porta 8000)

* Responsável pelo CRUD de atividades.
* Realiza requisições HTTP para validar se os IDs de alunos e professores existem.

### 2. API de Escola (porta 8000 – outra aplicação, não inclusa neste repositório)

* Disponibiliza endpoints para buscar informações de alunos e professores.

### Comunicação entre serviços

Quando uma nova atividade é criada, a API de Atividades envia requisições HTTP do tipo GET para:

* `GET /alunos/<id>`
* `GET /professores/<id>`

Esses endpoints são providos pela API de Escola e são usados para validar a existência das entidades antes de inserir no banco.


