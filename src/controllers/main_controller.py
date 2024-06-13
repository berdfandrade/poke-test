from fastapi import HTTPException
import httpx
# Criar um controller só, tendo em vista que são poq

class Controller:
    
    # Método para pegar [ TODOS ] os pokemons
    @staticmethod
    async def get_pokemons(number):
        pokemons = []
        url = "https://pokeapi.co/api/v2/pokemon"
        if number:
            url = f'{url}/?offset={number}&limit=20/'
        else:
            url = "https://pokeapi.co/api/v2/pokemon"                  
        async with httpx.AsyncClient() as client:
            while url:
                response = await client.get(url)
                if response.status_code != 200:
                    raise HTTPException(status_code=response.status_code, detail="Error fetching data from PokeAPI")
                
                data = response.json()
                pokemons.extend(data["results"])
                # url = data["next"]
        
        return pokemons