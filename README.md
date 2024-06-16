# PokéAPI Rocketman

PokéAPI Rocketman é uma API que fornece informações sobre Pokémons, consumindo dados da [PokéAPI](https://pokeapi.co/). Esta API foi desenvolvida por Bernardo Andrade (berdfandrade@gmail) para o teste davaga de desenvolvedor fullstack na Rocketman tech.

### Deploy 
A aplicação se encontra em produção [aqui]([https://fast-poke-api.vercel.app/]).

## Funcionalidades

- **Listagem de Pokémons**: Obtenha uma lista de todos os Pokémons em ordem alfabética.
- **Listagem paginada de Pokémons**: Obtenha uma lista paginada de Pokémons.
- **Informações de um Pokémon específico**: Obtenha informações detalhadas de um Pokémon específico pelo nome.
- **Suporte a formatos JSON e XML**: Receba os dados em formato JSON ou XML.

## Endpoints

### 1. Listar todos os Pokémons

#### Requisição

```http
GET /pokemons
```

#### Parâmetros de Query

- `format` (opcional): Especifique o formato da resposta (`json` ou `xml`). Padrão é `json`.

#### Exemplo de Requisição

```http
GET /pokemons?format=xml
```

#### Resposta

- **200 OK**: Lista de todos os Pokémons ordenados por nome.

### 2. Listar Pokémons com Paginação

#### Requisição

```http
GET /pokemons/page
```

#### Parâmetros de Query

- `page_number` (opcional): Número da página que deseja obter. Padrão é `1`.
- `format` (opcional): Especifique o formato da resposta (`json` ou `xml`). Padrão é `json`.

#### Exemplo de Requisição

```http
GET /pokemons/page?page_number=2&format=xml
```

#### Resposta

- **200 OK**: Lista paginada de Pokémons.

### 3. Obter informações de um Pokémon específico

#### Requisição

```http
GET /pokemon/{name}
```

#### Parâmetros de Path

- `name`: Nome do Pokémon que deseja buscar.

#### Parâmetros de Query

- `format` (opcional): Especifique o formato da resposta (`json` ou `xml`). Padrão é `json`.

#### Exemplo de Requisição

```http
GET /pokemon/pikachu?format=xml
```

#### Resposta

- **200 OK**: Informações detalhadas do Pokémon especificado.
- **404 Not Found**: Pokémon não encontrado.

## Instalação

Para rodar esta API localmente, siga os passos abaixo:

1. Clone este repositório:
    ```sh
    git clone https://github.com/berdfandrade/poke-test
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd poke-test
    ```
3. Crie um ambiente virtual e ative-o:
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```
5. Inicie a aplicação:
    ```sh
    uvicorn app:app --reload
    # ou 
    fastapi dev 
    ```

## Estrutura do Projeto

```plaintext

├── app.py
├── Dockerfile
├── pytest.ini
├── README.md
├── requirements.txt
├── src
│   ├── controllers
│   │   ├── helpers
│   │   │   ├── fetch_pokemons.py
│   │   │   └── xml_helpers.py
│   │   ├── __init__.py
│   │   ├── main_controller.py
│   ├── __init__.py
│   └── routes
│       ├── endpoints_docs.py
│       ├── endpoints.py
│       ├── __init__.py
│       ├── metodo.py
├── start.sh
├── tests
│   └── test_main.py
└── vercel.json

```

## Deploy no Vercel

1. Faça login no [Vercel](https://vercel.com/).
2. Crie um novo projeto e selecione o repositório da sua aplicação.
3. Configure o arquivo `vercel.json` conforme abaixo:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/app.py"
    }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "Access-Control-Allow-Origin",
          "value": "https://pokedex-front-peach.vercel.app"
        },
        {
          "key": "Access-Control-Allow-Methods",
          "value": "GET,POST,OPTIONS"
        },
        {
          "key": "Access-Control-Allow-Headers",
          "value": "Content-Type, Authorization"
        }
      ]
    }
  ]
}
```

4. Faça o deploy.

