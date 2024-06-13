from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.routes.endpoints import router as all_endpoints
import httpx

app = FastAPI(
    title="PokéAPI Rocketman",
    description="API para consulta de Pokémons - Bernardo Andrade | berdfandrade@gmail",
    version="1.0.0",
)

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite essas origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, PUT, DELETE, etc)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

app.include_router(all_endpoints)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)