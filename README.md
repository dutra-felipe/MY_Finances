# MY Finances

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-5.1-green)

## Descrição

O **MY Finances** é uma aplicação web desenvolvida com Django para gerenciar portfólios de investimentos. Ele permite que usuários registrem, monitorem e analisem suas transações de compra e venda de ativos, bem como rastreiem dividendos e a valorização de seus investimentos ao longo do tempo.

## Funcionalidades

- Registro e gerenciamento de investimentos em ações, fundos imobiliários, entre outros tipos de ativos.
- Rastreamento de transações de compra (`inflow`) e venda (`outflow`).
- Cálculo automático da valorização do portfólio e dos dividendos.
- Atualização automática do inventário de investimentos e exclusão de ativos vendidos completamente.
- Integração com APIs externas para obter informações financeiras atualizadas.

## Pré-requisitos

- Python 3.8 ou superior
- Django 5.1
- Outros requisitos listados em `requirements.txt` e `requirements_dev.txt`

## Instalação

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/dutra-felipe/MY_Finances.git
    cd MY_Finances
    ```

2. **Crie um ambiente virtual**:

    ```bash
    python3 -m venv venv  #No Windows use python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. **Instale as dependências**:

    Para instalação em produção:
    ```bash
    pip install -r requirements.txt
    ```

    Para desenvolvimento:
    ```bash
    pip install -r requirements_dev.txt
    ```

4. **Execute as migrações**:

    ```bash
    python manage.py migrate
    ```

5. **Inicie o servidor de desenvolvimento**:

    ```bash
    python manage.py runserver
    ```

    Acesse a aplicação no navegador através do endereço: `http://localhost:8000`

## Uso

1. **Gerenciamento de Investimentos**:
    - Registre um investimento, mas atenção na hora de colocar o `symbol` (ativos brasileiros possuem ".SA" ao final do nome. Ex: "PETR4.SA")
    - Utilize as funcionalidades de compra (`inflow`) e venda (`outflow`) para atualizar seu portfólio.

2. **Visualização de Dividendos e Valorização**:
    - Acesse as páginas de relatórios para visualizar os dividendos recebidos e a valorização do portfólio.

3. **Exclusão de Investimentos**:
    - Caso a quantidade de um investimento atinja zero após uma venda, o investimento será automaticamente excluído da lista de investimentos.

## Contato

Para mais informações, sugestões ou feedback, entre em contato com Felipe Dutra via [dutrafelipe77@gmail.com](mailto:dutrafelipe77@gmail.com).
