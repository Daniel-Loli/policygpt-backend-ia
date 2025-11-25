import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from app.models.policy_schema import policy_schema

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")

def analyze_policy(text: str):
    prompt = f"""
    Analiza la siguiente póliza de seguro vehicular. 
    Extrae coberturas, exclusiones, deducibles, condiciones especiales y un resumen.
    Devuelve la información usando el function calling.

    Texto:
    {text}
    """

    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}],
        functions=[policy_schema],
        function_call={"name": "extract_policy"}
    )

    # Tomar los argumentos generados por el modelo
    fn_args = response.choices[0].message.function_call.arguments

    import json
    return json.loads(fn_args)
def test_openai_connection():
    try:
        response = client.chat.completions.create(
            model=deployment,
            messages=[{"role": "user", "content": "ping"}],
            max_tokens=5
        )
        return True

    except Exception as e:
        print("❌ Error en test de conexión:", e)
        return False
