Markdown
# 🌅 Projeto Nova Aurora - Sistema Multidisciplinar de Inscrição

Este projeto consiste em uma aplicação web desenvolvida em **Flask (Python)** integrada a um banco de dados **MySQL**. O sistema gerencia o cadastro de candidatos para quatro cursos (ADS, Engenharia, Administração e Marketing), organizando as informações em tabelas específicas e oferecendo uma tela de login para validação dos dados.

A aplicação foi totalmente conteinerizada utilizando **Docker** e está pronta para o deploy na nuvem da **AWS (Amazon Web Services)**.

---

## 🛠️ Tecnologias Utilizadas

| Componente | Tecnologia | Versão |
| :--- | :--- | :--- |
| **Back-end** | Python / Flask | 3.0.3 |
| **Banco de Dados** | MySQL Server | 8.0 |
| **Driver de Conexão** | mysql-connector-python | 8.4.0 |
| **Containers** | Docker & Docker Compose | - |
| **Infraestrutura** | AWS EC2 (Ubuntu Server) | 22.04 LTS |

---

## 📂 Estrutura Principal do Projeto

```text
├── app.py                  # Código-fonte Flask (Rotas e conexão com o banco)
├── Dockerfile              # Instruções de build da imagem Python
├── docker-compose.yml      # Orquestração dos serviços (Web + DB)
├── requirements.txt        # Dependências limpas do projeto
└── templates/              # Páginas HTML da aplicação
    ├── index.html
    ├── inscricao.html
    ├── login.html
    ├── sucesso.html
    └── erro.html
🚀 Como Executar Localmente (Ambiente Docker)
Graças à conteinerização, você não precisa instalar o Python ou o MySQL nativamente na sua máquina para testar o projeto.

1. Pré-requisitos
Ter o Docker Desktop instalado e ativo.

Ter o MySQL Workbench (opcional, para visualizar as tabelas).

2. Passo a Passo
Navegue até a pasta do projeto no seu terminal:

Bash
cd caminho/para/o/projeto
Suba a infraestrutura completa com o Docker Compose:
(Este comando vai baixar as imagens, compilar o ambiente Flask, instalar os pacotes e iniciar o banco de dados automaticamente)

Bash
docker compose up --build
Acesse a aplicação no seu navegador:
👉 http://localhost:5000

🗄️ Conexão com o Banco de Dados (MySQL Workbench)
Para inspecionar as tabelas criadas e os dados salvos dentro do container, utilize as seguintes credenciais de conexão local:

Hostname: 127.0.0.1 (ou localhost)

Porta: 3306

Usuário: root

Senha: fatec

Database: nova_aurora_db

☁️ Deploy na Nuvem (AWS EC2)
A arquitetura do sistema foi projetada para rodar de forma isolada em produção dentro de uma instância AWS EC2 (Free Tier).

📐 Fluxo de Configuração na Nuvem
Provisionamento da Instância:

Sistema Operacional: Ubuntu Server 22.04 LTS.

Tipo de Instância: t2.micro (Nível Gratuito).

Regras de Rede (Security Groups):
Para liberar o acesso público ao site e permitir os testes da banca/professor, foram configuradas as seguintes regras de entrada:

Porta 22 (SSH): Liberação para administração remota via terminal.

Porta 5000 (Custom TCP): Porta de escuta do container Flask (0.0.0.0:5000).

Preparação do Ambiente Linux (Instalação via SSH):

Bash
# Atualizar pacotes do Ubuntu
sudo apt update && sudo apt upgrade -y

# Instalar Docker e Docker Compose V2
sudo apt install docker.io docker-compose-v2 -y

# Dar permissão ao usuário padrão rodar o Docker
sudo usermod -aG docker $USER
(Nota: É necessário deslogar e logar novamente no terminal SSH após adicionar o usuário ao grupo do Docker)

Inicialização em Produção:
O código é clonado do repositório para o servidor da Amazon e executado em segundo plano (detached mode):

Bash
docker compose up --build -d
A aplicação passa a ficar disponível globalmente através do IP Público fornecido pela AWS: http://IP_PUBLICO_AWS:5000.

🛑 Como Encerrar a Aplicação
Para parar os serviços locais sem perder os dados armazenados, use o comando:

Bash
docker compose down
Os dados inseridos nas tabelas persistirão de forma segura no seu HD através do volume configurado no arquivo compose (mysql_data).


---

### 💡 Lembrete rápido sobre o Git:
Antes de subir para o GitHub, crie um arquivo chamado `.gitignore` do lado do seu `app.py` e coloque apenas isso dentro dele:
```text
venv/
__pycache__/
*.pyc