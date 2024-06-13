from fastapi import FastAPI, HTTPException
from src.routes.endpoints import router as all_endpoints
import httpx

app = FastAPI()

app.include_router(all_endpoints)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)