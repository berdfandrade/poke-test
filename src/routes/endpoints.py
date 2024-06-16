from fastapi import APIRouter, HTTPException, Query, Response
from src.controllers.main_controller import Controller
from src.routes.endpoints_docs import EndpointDocs

router = APIRouter()

@router.get(
    "/",
    tags=["root"],
    summary=EndpointDocs["blank_route"]["summary"],
    description=EndpointDocs["blank_route"]["description"],
)
async def blank_route():
    return {
        "MESSAGE": "PokéAPI Rocketman || Bernardo Andrade || A documentação se encontra em /docs"
    }


@router.get(
    "/pokemons",
    tags=["pokemons"],
    summary=EndpointDocs["get_all_pokemons"]["summary"],
    description=EndpointDocs["get_all_pokemons"]["description"],
)
async def get_all_pokemons(
    format: str = Query(
        "json", enum=["json", "xml"], description="Formato da resposta: 'json' ou 'xml'"
    )
):
    pokemons = await Controller.get_pokemons(format=format)
    return pokemons


@router.get(
    "/pokemons/pages/{page_number}",
    tags=["pokemons"],
    summary=EndpointDocs["get_pokemons_per_page"]["summary"],
    description=EndpointDocs["get_pokemons_per_page"]["description"],
)
async def get_pokemon_pages(
    page_number: int,
    format: str = Query(
        "json", enum=["json", "xml"], description="Formato da resposta: 'json' ou 'xml'"
    ),
):
    pokemons_data = await Controller.get_pokemons_per_page(page_number=page_number)
    return pokemons_data


@router.get(
    "/pokemon/{name}",
    tags=["pokemons"],
    summary=EndpointDocs["get_pokemon_by_name"]["summary"],
    description=EndpointDocs["get_pokemon_by_name"]["description"],
)
async def get_pokemon_by_name(
    name: str,
    format: str = Query(
        "json", enum=["json", "xml"], description="Formato da resposta: 'json' ou 'xml'"
    ),
):

    pokemon = await Controller.get_pokemon_per_name(name, format)
    return pokemon
