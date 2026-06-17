# Portal Acadêmico Nova Aurora

## 📝 Descrição do Sistema
Este projeto consiste em um sistema web desenvolvido para o gerenciamento de inscrições acadêmicas, permitindo o cadastro de candidatos em diferentes cursos. A aplicação foi projetada com foco em arquitetura de microsserviços, utilizando Docker para containerização e garantindo portabilidade total entre ambiente local e servidor em nuvem.

## 🛠️ Tecnologias Utilizadas
* **Backend:** Python e Flask
* **Banco de Dados:** MySQL
* **Containerização:** Docker e Docker Compose
* **Infraestrutura:** AWS EC2
* **Gerenciamento de Código:** Git e GitHub

## 🚀 Funcionalidades Principais
* **Sistema de Inscrição:** Cadastro unificado com persistência de dados em banco MySQL.
* **Login Seguro:** Validação de acesso via CPF e E-mail, com busca inteligente em múltiplas tabelas.
* **Resiliência:** Tratamento de erros que permite ao sistema operar mesmo com variações na estrutura de tabelas.
* **Automação:** Inicialização automática do banco de dados e criação de tabelas na primeira execução.

## 📂 Estrutura de Pastas

.
├── app.py              
├── Dockerfile          
├── docker-compose.yml  
├── .env.example        
└── templates/          
🛠️ Como Instalar e Rodar
Pré-requisitos
Docker e Docker Compose instalados.

Git instalado.

# ✅Passo a passo

## Clone o repositório:

Bash
   git clone https://github.com/guilherme16092007/Integracao-FDB.git
   cd Integracao-FDB
Configure as variáveis de ambiente:

Bash
   cp .env.example .env
    Edite o arquivo .env com suas configurações de banco de dados
    
## Suba o sistema:

Bash
   docker compose up -d --build
🌐 Como Acessar
Local: http://seuip:5000


AWS EC2: http://http://100.56.75.22:5000


# 📸 Evidências da Atividade

Prints:

## Aplicação rodando na AWS EC2
<img width="1874" height="976" alt="image" src="https://github.com/user-attachments/assets/9c210915-8063-4b03-b07d-cfc8d94ff710" />


## Containers rodando
<img width="977" height="506" alt="image" src="https://github.com/user-attachments/assets/46fd002f-3678-445d-b75e-0701f83314f6" />


## Site no ar
<img width="1861" height="990" alt="image" src="https://github.com/user-attachments/assets/c110eab2-e915-432a-862e-b893b597263c" />



Projeto desenvolvido para a Atividade 5 - Design Inovador.
