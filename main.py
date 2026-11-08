
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from models import TranslationRequest, TranslationResponse


# Carrega as variaveis do arquivo .env
load_dotenv()

# Configuracao da aplicacao
app = FastAPI(
    title="TP2 - Parte 2 - Questao 2 - OpenAI",
    description="API de traducao com FastAPI, LangChain e OpenAI",
    version="1.0.0"
)

# Prompt para traducao de ingles para frances
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a professional translator. "
        "Translate the following English text into French. "
        "Keep the original meaning and context. "
        "Return only the French translation."
    ),
    (
        "human",
        "{text}"
    )
])


# Rota de traducao
@app.post(
    "/translate",
    response_model=TranslationResponse
)
def translate_text(request: TranslationRequest):

    # Verifica se a chave da API foi configurada
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=503,
            detail="Chave da API OpenAI nao configurada."
        )

    try:
        # Inicializa o modelo da OpenAI
        llm = ChatOpenAI(
            model="gpt-4.1-mini",
            temperature=0,
            max_tokens=1000,
            timeout=30,
            max_retries=1
        )

        # Cria a cadeia LangChain
        chain = prompt | llm

        # Envia o texto para traducao
        response = chain.invoke({
            "text": request.text
        })

        # Obtem o texto traduzido
        translated_text = response.content

        # Retorna a resposta JSON
        return TranslationResponse(
            original_text=request.text,
            translated_text=translated_text,
            source_language="English",
            target_language="French"
        )

    except Exception as error:

        # Mostra o tipo do erro no terminal
        print(
            f"Erro na integracao OpenAI: "
            f"{type(error).__name__}"
        )

        raise HTTPException(
            status_code=502,
            detail="Nao foi possivel obter a traducao da OpenAI."
        ) from error
