@router.get(
    "/pokemons/pages/{number}",
    tags=["pokemons"],
    summary=EndpointDocs["get_pokemons_per_page"]["summary"],
    description=EndpointDocs["get_pokemons_per_page"]["description"],
)
async def get_pokemons_per_page(
    number: int,
    limit: int = Query(20, description="Número de Pokémons por página"),
    format: str = Query("json", description="Formato da resposta: 'json' ou 'xml'"),
):
    """
    Endpoint para obter Pokémons por página.

    - **number**: Número da página.
    - **limit**: Número de Pokémons por página.
    - **format**: Formato da resposta (json ou xml).
    """
    pokemons = await Controller.get_pokemons_per_page(
        page=number, limit=limit, format=format
    )
    return pokemons
