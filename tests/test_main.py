import pytest
from fastapi import HTTPException
from fastapi.responses import Response
from httpx import AsyncClient
from src.controllers.main_controller import Controller
from src.controllers.helpers.xml_helpers import pokemons_to_xml
from app import app

@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"MESSAGE":"PokéAPI Rocketman || Bernardo Andrade || A documentação se encontra em /docs"}


BASE_URL = "https://pokeapi.co/api/v2/pokemon"

@pytest.mark.asyncio
async def test_get_pokemons(httpx_mock):
    mock_response = {
        "results": [
            {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
            {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"}
        ],
        "next": None
    }

    httpx_mock.add_response(url=BASE_URL, json=mock_response)
    
    pokemons = await Controller.get_pokemons(format="json")
    assert pokemons == sorted(mock_response["results"], key=lambda x: x["name"])

    xml_response = pokemons_to_xml(mock_response["results"])
    response = await Controller.get_pokemons(format="xml")
    assert response.body.decode() == xml_response

@pytest.mark.asyncio
async def test_get_pokemons_per_page(httpx_mock):
    page_number = 1
    mock_response = {
        "results": [
            {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon/1/"},
            {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon/2/"}
        ],
        "next": None
    }

    httpx_mock.add_response(url=BASE_URL, json=mock_response)

    pokemons = await Controller.get_pokemons_per_page(page_number=page_number, format="json")
    assert pokemons == sorted(mock_response["results"], key=lambda x: x["name"])

    xml_response = pokemons_to_xml(mock_response["results"])
    response = await Controller.get_pokemons_per_page(page_number=page_number, format="xml")
    assert response.body.decode() == xml_response

@pytest.mark.asyncio
async def test_get_pokemon_per_name(httpx_mock):
    name = "bulbasaur"
    mock_response = {
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "id": 1,
        "is_default": True,
        "order": 1,
        "weight": 69,
        "moves": []
    }

    url = f"{BASE_URL}/{name}"
    httpx_mock.add_response(url=url, json=mock_response)

    expected_response = mock_response.copy()
    del expected_response["moves"]

    pokemon = await Controller.get_pokemon_per_name(name=name, format="json")
    assert pokemon == expected_response

    xml_response = pokemons_to_xml(expected_response)
    response = await Controller.get_pokemon_per_name(name=name, format="xml")
    assert response.body.decode() == xml_response
