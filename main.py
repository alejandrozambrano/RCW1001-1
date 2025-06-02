from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Middleware CORS si nécessaire
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Modifier selon tes besoins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def welcome():
    try:
        return {"message": "Hello from RCW Teccart"}
    except Exception as e:
        print(f'Exception : {e}')
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test")
async def bienvenue():
    try:
        return {"message": "You are in RCW GROUPE 1001"}
    except Exception as e:
        print(f'Exception : {e}')
        raise HTTPException(status_code=500, detail=str(e))