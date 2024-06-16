"""
    Documentação para os endpoints providos pela Swagger Docs
"""

# Exemplo de objeto de documentação dos endpoints
EndpointDocs = {
    "blank_route": {
        "summary": "Rota padrão",
        "description": "Rota padrão que retorna uma mensagem informativa.",
        "tags": ["root"],
    },
    "get_all_pokemons": {
        "summary": "Obter todos os Pokémons",
        "description": "Este endpoint é projetado para recuperar todos os Pokémons da API PokéAPI, ordená-los alfabeticamente e retornar a lista completa. O usuário pode escolher entre receber os dados em formato JSON ou XML.",
        "tags": ["pokemons"],
    },
    "get_pokemons_per_page": {
        "summary": "Obter Pokémons por página",
        "description": "Este endpoint permite aos usuários obter uma lista de Pokémons paginada. Ao invés de paginar com base na resposta da API original da PokéAPI, a lista completa de Pokémons é obtida primeiro, ordenada alfabeticamente, e depois paginada conforme solicitado. Isso garante que os resultados sejam sempre consistentes e ordenados de maneira previsível.",
        "tags": ["pokemons"],
    },
    "get_pokemon_by_name": {
        "summary": "Obter Pokémon por nome",
        "description": "Este endpoint permite que os usuários obtenham informações detalhadas sobre um Pokémon específico, utilizando seu nome. Os dados podem ser retornados em formato JSON ou XML, dependendo da preferência do usuário.",
        "tags": ["pokemons"],
    },
}
