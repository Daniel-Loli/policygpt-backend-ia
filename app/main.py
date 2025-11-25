from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.extract import router as extract_router

# NUEVO
from app.services.openai_client import test_openai_connection

app = FastAPI(
    title="PolicyGPT Enterprise – Backend IA",
    version="1.0.0"
)

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(extract_router)

@app.on_event("startup")
def startup_event():
    """
    Este test se ejecuta automáticamente
    cuando FastAPI inicia.
    """
    print("🔍 Verificando conexión con Azure OpenAI...")
    ok = test_openai_connection()

    if ok:
        print("✅ Conexión exitosa con Azure OpenAI")
    else:
        print("❌ Error al conectar con Azure OpenAI")
        print("⚠️ Revisa tu .env (KEY, ENDPOINT, DEPLOYMENT)")


@app.get("/")
def health():
    return {"status": "Backend IA funcionando"}
