
# FastAPI Template Backend

Para organizar um repositório de uma API construída com FastAPI, esta estrutura oferece uma separação bem definida entre módulos, facilitando a escalabilidade e manutenção do projeto.

## Estrutura do Projeto

```plaintext
.
├── api/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── __init__.py
│   └── router.py
├── config/
|   ├── settings/
|   |   ├── __init__.py
|   |   ├── base.py
|   |   ├── development.py
|   |   ├── production.py
|   |   ├── qa.py
│   ├── __init__.py
│   ├── logging.py
│   └── settings.py
├── db/
|   ├── __init__.py
|   ├── base.py
|   └── session.py
├── models/
│   ├── __init__.py
│   └── user.py
├── messages/
│   ├── __init__.py
|   ├── error.py
│   └── user.py
├── repositories/
│   ├── __init__.py
│   └── user.py
├── schemas/
│   ├── __init__.py
│   └── user.py
├── security/
│   ├── __init__.py
│   ├── auth.py
│   └── security.py
├── services/
│   ├── __init__.py
│   └── user_service.py
├── tests/
│   ├── __init__.py
|   ├── end_to_end/
│   |   └── test_end_to_end.py
│   ├── security/
|   |   └── test_security.py
│   ├── unit/
│   │   ├── test_user.py
│   │   ├── test_item.py
│   └── └── test_schemas.py
├── scripts/
│   ├── start.sh
│   ├── pre_start.sh
│   └── test.sh
├── .env.example
├── .gitignore
├── .gitlint
├── .pre-commit-config.yaml
├── docker-compose.yml
├── Dockerfile
├── main.py
├── README.md
├── requirements.dev.txt
├── requirements.txt
└── setup.cfg
```

## Descrição das Pastas e Arquivos

A seguir, a descrição da função de cada pasta e arquivo dentro do projeto.

### **api/**
Contém os endpoints da API e as rotas que definem os pontos de acesso da aplicação.

- **routes/**: Diretório onde estão as definições específicas de rotas de cada módulo ou funcionalidade da aplicação.
  - **user.py**: Define as rotas relacionadas a usuários, como criação, leitura, atualização e exclusão (CRUD).
  
- **router.py**: Arquivo principal que inclui e organiza todas as rotas definidas no diretório `routes`. Ele conecta os diferentes módulos de rota e configura a aplicação FastAPI.

### **config/**
Armazena a configuração da aplicação, como variáveis de ambiente e configuração de logging.

- **settings/**: Subpasta com configurações para diferentes ambientes.
  - **base.py**: Contém a configuração básica e comum a todos os ambientes.
  - **development.py**, **production.py**, **qa.py**: Configurações específicas para ambientes de desenvolvimento, produção e qualidade (QA).
  
- **logging.py**: Configuração do sistema de logs da aplicação. Define como e onde as mensagens de log serão registradas (por exemplo, no console ou em arquivos).
  
- **settings.py**: Carrega as configurações de acordo com o ambiente em que a aplicação está rodando (desenvolvimento, produção ou QA).

### **db/**
Contém arquivos relacionados ao banco de dados, como a configuração de sessão e a base dos modelos ORM.

- **base.py**: Define a classe `Base` usando `declarative_base` do SQLAlchemy, a qual será herdada por todos os modelos do banco de dados.
  
- **session.py**: Contém a configuração de sessão do SQLAlchemy (por exemplo, criando uma sessão de banco de dados, `SessionLocal`, para ser usada nas interações com o banco).

### **models/**
Contém os modelos que representam as tabelas do banco de dados. Cada modelo geralmente é uma classe que herda de `Base` e mapeia uma tabela do banco.

- **user.py**: Define o modelo de dados para o `User`. Cada classe representa uma tabela no banco de dados e suas colunas são mapeadas como atributos da classe.

### **messages/**
Armazena mensagens de sucesso e erro que são retornadas pela API. Centraliza a definição de mensagens.

- **error.py**: Contém mensagens genéricas de erro que serão usadas nas respostas da API (por exemplo, "Falha na consulta", "Erro interno", etc.).
  
- **user.py**: Contém mensagens específicas relacionadas à criação, recuperação, atualização ou exclusão de usuários.

### **repositories/**
Contém as funções responsáveis pela interação direta com o banco de dados, como consultas, inserções, atualizações e exclusões de dados. Geralmente, isso abstrai a lógica de acesso ao banco para os serviços.

- **user.py**: Contém funções que manipulam diretamente os dados dos usuários no banco (exemplo: `create_user()`, `get_user()`).

### **schemas/**
Contém os schemas de dados, usados para validação e serialização das informações. Estes são os modelos que a API recebe e retorna em formato JSON.

- **user.py**: Define os schemas de dados do `User`, como os modelos Pydantic usados para validação de entrada e saída de dados (por exemplo, `UserCreate`, `UserResponse`).

### **security/**
Contém funcionalidades relacionadas à segurança da aplicação, como autenticação, autorização e criptografia.

- **auth.py**: Contém funções de autenticação, como geração de tokens JWT, verificação de senha, etc.
  
- **security.py**: Contém configurações de segurança, como verificação de permissões, middleware de segurança, etc.

### **services/**
Contém a lógica de negócios da aplicação. Aqui ficam as funções que orquestram a execução do fluxo da aplicação, interagindo com os repositórios e aplicando regras de negócios.

- **user_service.py**: Contém a lógica de negócios relacionada aos usuários (por exemplo, criar um usuário, verificar a existência, autenticar, etc.).

### **tests/**
Contém os testes automatizados da aplicação, organizados por tipo (unitários, de integração, de segurança, etc.).

- **end_to_end/**: Contém testes de ponta a ponta que verificam o funcionamento completo de uma funcionalidade da API. Esses testes simulam o uso real da API.
  - **test_end_to_end.py**: Testes de integração ou ponta a ponta.

- **security/**: Contém testes relacionados à segurança da aplicação, como autenticação, autorização, etc.
  - **test_security.py**: Testes relacionados ao sistema de segurança, como login, permissões de acesso, etc.

- **unit/**: Contém testes unitários que verificam funções isoladas, sem dependências externas.
  - **test_user.py**: Testes unitários para funções do serviço de usuário.
  - **test_item.py**: Testes unitários para funções relacionadas aos itens da aplicação.
  - **test_schemas.py**: Testes para validar os schemas de entrada e saída da API.

### **scripts/**
Contém scripts auxiliares para rodar e configurar a aplicação ou ambiente.

- **start.sh**: Script para iniciar a aplicação (provavelmente em um contêiner Docker ou diretamente no servidor).
  
- **pre_start.sh**: Scripts de preparação que podem configurar o ambiente ou banco de dados antes de iniciar a aplicação.
  
- **test.sh**: Script para rodar os testes automatizados.

### Arquivos na raiz do projeto

- **.env.example**: Exemplo do arquivo de configuração com variáveis de ambiente sensíveis, como credenciais de banco de dados, chave secreta, etc.

- **.gitignore**: Define quais arquivos ou pastas devem ser ignorados pelo Git, como arquivos de configuração locais, caches, etc.

- **Dockerfile**: Arquivo para construir a imagem Docker da aplicação, contendo instruções sobre como configurar o ambiente da aplicação.

- **main.py**: O ponto de entrada da aplicação FastAPI. Define a instância do FastAPI e inclui as rotas da API.

- **requirements.txt**: Contém as dependências do projeto, listando os pacotes necessários para rodar a aplicação (geralmente gerado com `pip freeze`).

- **README.md**: Documento com informações gerais sobre o projeto, como como rodá-lo, como contribuir, e sua estrutura.

- **setup.cfg**: Arquivo de configuração para ferramentas de linting, como o Flake8. Define regras de estilo e configurações específicas para garantir a consistência de código.


## Executando o projeto

### Configuração do Ambiente
O projeto usa variáveis de ambiente para configurações sensíveis. Siga os passos abaixo para configurá-las:

1. Copie o arquivo `.env.example` para `.env`:

    ```bash
    cp .env.example .env
    ```

2. Edite o arquivo `.env` para incluir suas configurações, como o URI do banco de dados, segredo para tokens JWT, entre outros parâmetros necessários.

### Instalar Dependências
Instale as dependências do projeto com o comando:

```bash
pip install -r requirements.dev.txt
```

#### Instalar sem as dependências de desenvolvimento (opcional)
Se caso queira instalar sem as dependências de desenvolvimento, utilize o comando:
```bash
pip install -r requirements.txt
```

### Instalação e configuração do pre-commit
O pre-commit serve para manter o padrão do projeto no momento do commit. Para instalá-lo e configurá-lo, use os comandos:

```bash
pip install pre-commit
pre-commit install
pre-commit install --hook-type commit-msg
```

### Executando o Projeto
Agora, você pode iniciar a aplicação. Existem duas formas principais: utilizando o Uvicorn diretamente ou com Docker.

#### Opção 1: Rodar no terminal
Inicie a aplicação com o comando:

```bash
fastapi dev main.py
```

#### Opção 2: Rodar com Docker
Se preferir rodar a aplicação em um contêiner Docker, utilize os seguintes comandos:

Compilar e executar os contêineres:

```bash
docker-compose up --build
```

A aplicação estará disponível em http://127.0.0.1:8000.

### Executando Testes
Para rodar os testes, utilize o comando:

```bash
pytest
```