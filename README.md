# Controle de Abastecimentos

## Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/controle-abastecimentos.git
   cd controle-abastecimentos
2. Crie e ative o ambiente virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
4. Realize as migrações:
    ```bash
    python manage.py migrate
5. Endpoints da API

- `/api/tanques/`
- `/api/bombas/`
- `/api/abastecimentos/`

## Com esses passos, você terá o ambiente configurado e o servidor rodando.


# Executando o Frontend em React

Este projeto é um frontend em React para gerar relatórios de abastecimentos em formato PDF.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado o seguinte:

- Node.js - [Instalação do Node.js](https://nodejs.org/)
- npm (Node Package Manager) ou Yarn - Normalmente instalado com o Node.js

## Configuração do Projeto

1. **Instale as dependências**

   ```bash
   npm install
2. **Executando o Servidor de Desenvolvimento**
    ```bash
    npm start
## Isso iniciará o servidor de desenvolvimento do React. Por padrão, estará disponível em http://localhost:3000.

## Nos Endpoints do FrontEnd basta tirar a flag API

- `http://localhost:3000/` 
- `http://localhost:3000/abastecimentos` 
- `http://localhost:3000/relatorio-abastecimentos` 

## Contatos
- [LinkedIn](https://www.linkedin.com/in/emeson-borges-1539b3126/)

- [Instagram](https://www.instagram.com/engemesonborges/)

