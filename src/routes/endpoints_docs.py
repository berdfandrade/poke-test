"""
    Documentação para os endpoints providos pela Swagger Docs
"""

# Exemplo de objeto de documentação dos endpoints
EndpointDocs = {
    'blank_route': {
        'summary': "Rota padrão",
        'description': "Rota padrão que retorna uma mensagem informativa.",
        'tags': ["root"]
    },
    'get_all_pokemons': {
        'summary': "Obter todos os Pokémons",
        'description': "Endpoint para obter todos os Pokémons disponíveis.",
        'tags': ["pokemons"]
    },
    'get_pokemons_per_page': {
        'summary': "Obter Pokémons por página",
        'description': "Endpoint para obter Pokémons por página.",
        'tags': ["pokemons"]
    },
    'get_pokemon_by_name': {
        'summary': "Obter Pokémon por nome",
        'description': "Endpoint para obter detalhes de um Pokémon por nome.",
        'tags': ["pokemons"]
    }
}
