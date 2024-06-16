import httpx 


async def fetch_pokemons_sorted():
        BASE_URL = "https://pokeapi.co/api/v2/pokemon"
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
        return pokemons_sorted
