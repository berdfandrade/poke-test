import httpx
from fastapi import HTTPException, Query
from fastapi.responses import Response
from fastapi.responses import JSONResponse
import xml.etree.ElementTree as ET
from src.controllers.helpers.xml_helpers import dict_to_xml, pokemons_to_xml
from src.controllers.helpers.fetch_pokemons import fetch_pokemons_sorted

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

""" 

    Toda a lógica de negócio está embutida nesse controller.
    O Controller é uma classe, e cada método é uma função responsável
    por fazer requisições específicas para a Poké API original.

"""


class Controller:
    """
    
    Método [ GET ] para fazer [ REQ ] de todos os pokémons
    por ordem alfabética sem paginação, através do
    httpx | Existe a possibilidade de receber a data em XML
    """

    @staticmethod
    async def get_pokemons(format: str = "json"):
        pokemons = []
        url = BASE_URL

        async with httpx.AsyncClient() as client:
            while url:
                response = await client.get(url)
                if response.status_code != 200:
                    raise HTTPException(
                        status_code=response.status_code,
                        detail="Error fetching data from PokeAPI",
                    )

                data = response.json()
                pokemons.extend(data["results"])
                url = data["next"]

        # Ordenar os pokémons por nome
        pokemons_sorted = sorted(pokemons, key=lambda x: x["name"])

        # Caso seja o REQ seja por XML
        if format == "xml":
            return Response(
                content=pokemons_to_xml(pokemons_sorted), media_type="application/xml"
            )

        return pokemons_sorted

    """
    Método [ GET ] para fazer [ REQ ] de todos os pokémons
    através da paginação | Existe a possibilidade de receber a data em XML
    """

    @staticmethod
    async def get_pokemons_per_page(page_number: int = 1, format: str = "json"):
        all_pokemons = []

        async def fetch_all_pokemons():
            pokemons = []
            url = BASE_URL

            async with httpx.AsyncClient() as client:
                while url:
                    response = await client.get(url)
                    if response.status_code != 200:
                        raise HTTPException(
                            status_code=response.status_code,
                            detail="Error fetching data from PokeAPI",
                        )

                    data = response.json()  # <- Aqui está o problema
                    pokemons.extend(data["results"])
                    url = data["next"]

            return pokemons

        all_pokemons = await fetch_all_pokemons()
        all_pokemons_sorted = sorted(all_pokemons, key=lambda x: x["name"])

        start_index = (page_number - 1) * 20
        end_index = start_index + 20
        paginated_pokemons = all_pokemons_sorted[start_index:end_index]

        if format == "xml":
            return Response(
                content=pokemons_to_xml(paginated_pokemons), media_type="application/xml"
            )

        return paginated_pokemons

    """
    Método [ GET ] para fazer [ REQ ] de um pokémon espécifico
    através de seu nome. | Existe a possibilidade de receber a data em XML
    """

    @staticmethod
    async def get_pokemon_per_name(name: str, format: str = "json"):
        # Garantir que o nome está em lowercase
        name_to_be_search = name.lower()

        url = f"{BASE_URL}/{name_to_be_search}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail="Error fetching pokémon data",
                )
            data = response.json()

        # Remover o campo "moves" do dicionário de dados
        if "moves" in data:
            del data["moves"]

        # Caso a REQ seja por XML
        if format == "xml":
            return Response(content=pokemons_to_xml(data), media_type="application/xml")

        return data