# FastAPI Project

Este projeto simples de FastAPI cadastra pessoa e idade. Foi desenvolvido com o objetivo de criar uma API para gerenciamento de cadastros de pessoas. A aplicação foi conteinerizada usando Docker e também pode ser executada em um ambiente Kubernetes, utilizando Minikube para testes locais. Além disso, a integração com o banco de dados PostgreSQL foi feita através do SQLAlchemy.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- **`app/`**: Contém os principais arquivos da aplicação.
  - **`database.py`**: Configuração da conexão com o banco de dados.
  - **`main.py`**: Configuração do FastAPI e definição dos endpoints.
  - **`models.py`**: Definição dos modelos de dados para SQLAlchemy.
- **`Dockerfile`**: Usado para construir a imagem Docker da aplicação.
- **`docker-compose.yml`**: Orquestra os serviços necessários para rodar a aplicação em containers.
- **`requirements.txt`**: Lista de dependências Python necessárias para o projeto.

## Como Configurar o Projeto

### Pré-requisitos

Para rodar este projeto, você precisará ter instalado:

- **Docker**: Para criar e gerenciar os containers.
- **Minikube**: Para testar a aplicação em um ambiente Kubernetes localmente.
- **Git**: Para clonar o repositório.

### Passos para Configuração

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/luizpires28/my_fastapi_project.git
   cd my_fastapi_project

2. **Construir e iniciar os containers com Docker:**

   ```bash
   docker-compose up --build


    3. Configuração do Banco de Dados:
O projeto utiliza PostgreSQL como banco de dados, e a URL de conexão configurada é: plaintext
postgresql://root:1234@db:5432/teste
Certifique-se de que o banco de dados está rodando corretamente dentro do container.

## Rodando a Aplicação

### Com Docker

Para rodar a aplicação com Docker, basta utilizar o comando:

```bash
docker-compose up

### Com Minikube (Kubernetes)

1. **Inicie o Minikube:**

   ```bash
   minikube start

2. **Aplique as configurações Kubernetes:**

   ```bash
   kubectl apply -f all-resources.yml

3. **Acesse o serviço FastAPI através do IP do Minikube. Exemplo de acesso:**

   ```bash
   minikube service nome-do-serviço --url

## Endpoints Disponíveis

- **POST /pessoa**: Adiciona uma nova pessoa ao banco de dados.
- **GET /lista**: Retorna uma lista de todas as pessoas cadastradas.

### Exemplo de requisição para adicionar uma pessoa:

```json
{
  "nome": "João",
  "idade": 30
}

## Deploy Contínuo com Argo CD

O projeto está preparado para deploy contínuo utilizando o Argo CD.

Repositório: [GitHub - my_fastapi_project](https://github.com/luizpires28/my_fastapi_project)

## Conclusão

Este README serve como guia para configurar e entender a estrutura do projeto. Com as instruções acima, é possível rodar a aplicação tanto em ambiente local quanto em um cluster Kubernetes.
