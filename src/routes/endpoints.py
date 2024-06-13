import httpx
from fastapi import APIRouter
from src.controllers.main_controller import Controller

router = APIRouter() 

@router.get("/")
def read_root():
    return {"message": "POKE-API || ROCKETMAN - BERNARDO ANDRADE"}

@router.get('/pokemons/{number}')
async def fetch_all_pokemons(number):
    pokemons = await Controller.get_pokemons(number)
    return pokemons

@router.get('/pokemons/pages/{number}')
async def fetch_per_page(number):
    pokemons = await Controller.get_pokemon_pages(number)
    return pokemons