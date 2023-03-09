# Documentação da API

## Tabela de Conteúdos

-   [Visão Geral](#1-visão-geral)

-   [Diagrama ER](#2-diagrama-er)

-   [Documentação](#3-documentação)

-   [Rodando localmente](#4-rodando-localmente)

## 1. Visão Geral

Visão geral do projeto, um pouco das tecnologias usadas.

-   **[Python](https://www.python.org/)**

-   **[Django](https://www.django-rest-framework.org/api-guide/authentication/)**

-   **[Drf spectacular](https://drf-spectacular.readthedocs.io/en/latest/)**

-   **[Postgres](https://www.postgresql.org/)**

## 2. Diagrama ER

![Diagrama ER](https://github.com/m5-projeto-final-lucira-grupo28/api-rede-social/blob/develop/DER.png?raw=true)

[ Voltar para o topo ](#tabela-de-conteúdos)

Diagrama ER da API definindo as relações entre as tabelas do banco de dados.

## 3. Documentação

[ Voltar para o topo ](#tabela-de-conteúdos)

Link com a **[Documentação](Em breve)**

## 4. Rodando localmente

[ Voltar para o topo ](#tabela-de-conteúdos)

### 4.1 Crie seu ambiente virtual:

Clone o projeto em sua máquina e instale o ambiente virtual com o comando:

```bash
python -m venv venv
```

### 4.2 Ative seu venv:

Execute o comando em seu terminal:

```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```

### 4.3 Instalando componentes da aplicação

Execute o comando em seu terminal:

```bash
pip install -r requirements.txt
```

### 4.4 Preencha o arquivo .env com os dados do Postgres

```bash
Criei um arquivo .env, seguindo como base o arquivo .env.exemple
```

### 4.5 Executando as migrações com o banco de dados

Execute o comando em seu terminal:

```bash
python manage.py migrate
```

### 4.6 Rodando o servidor localmente

Execute o comando em seu terminal:

```bash
python manage.py runserver
```
