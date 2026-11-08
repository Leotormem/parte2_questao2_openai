# TP2 — Parte 2, Questão 2: Tradução com OpenAI e LangChain

## Descrição

Neste projeto desenvolvi uma API de tradução de inglês para francês utilizando FastAPI, LangChain e a API da OpenAI.

O objetivo é receber um texto em inglês através de uma requisição HTTP, enviar esse texto para um modelo da OpenAI por meio do LangChain e retornar a tradução em JSON.

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- LangChain
- LangChain OpenAI
- Pydantic
- Python-dotenv
- API da OpenAI

## Estrutura do projeto

```text
parte2_questao2_openai/
├── main.py
├── models.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env (somente local)
```

## Funcionamento

A aplicação recebe um texto em inglês pela rota `POST /translate`.

O FastAPI recebe a requisição e utiliza o Pydantic para validar os dados.

O LangChain prepara um prompt solicitando a tradução e gerencia a chamada ao modelo `gpt-4.1-mini` da OpenAI.

Quando a chamada é concluída corretamente, a aplicação retorna o texto original e a tradução para o francês em formato JSON.

## Arquitetura da aplicação

```text
Usuário / Swagger UI
        |
        v
FastAPI - POST /translate
        |
        v
Pydantic - Validação do JSON
        |
        v
LangChain - ChatPromptTemplate
        |
        v
LangChain - ChatOpenAI
        |
        v
API da OpenAI - gpt-4.1-mini
        |
        v
LangChain - Resposta do modelo
        |
        v
FastAPI - Resposta JSON
```

## Instalação

Crie um ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

## Configuração da API

É necessário possuir uma chave de API da OpenAI e acesso ao modelo utilizado.

Crie um arquivo `.env` dentro da pasta do projeto e configure:

```text
OPENAI_API_KEY=sua_chave_secreta
```

O arquivo `.env` não deve ser enviado ao GitHub.

## Execução

Inicie a aplicação:

```powershell
python -m uvicorn main:app --reload
```

Abra a documentação Swagger UI:

http://127.0.0.1:8000/docs

## Exemplo de requisição

Rota `POST /translate`:

```json
{
  "text": "Hello, how are you today?"
}
```

Quando a integração estiver disponível, a resposta terá a seguinte estrutura:

```json
{
  "original_text": "Hello, how are you today?",
  "translated_text": "Bonjour, comment allez-vous aujourd'hui ?",
  "source_language": "English",
  "target_language": "French"
}
```

O JSON acima representa o formato esperado, não o resultado de uma execução bem-sucedida nesta atividade.

## Testes realizados

A aplicação foi iniciada localmente com Uvicorn e a rota `POST /translate` foi testada utilizando o Swagger UI.

O FastAPI recebeu corretamente o JSON, mas a tentativa de integração com a OpenAI retornou HTTP 502 (Bad Gateway).

O código possui tratamento de exceções para identificar falhas na comunicação com o serviço externo.

A causa exata do erro não foi confirmada. Uma possibilidade é a ausência de créditos disponíveis para utilização da API.

Por esse motivo, não foi possível validar uma tradução real utilizando a OpenAI durante os testes.

## Limitações

A integração depende de conexão com a internet, disponibilidade da API, credenciais válidas e limites de utilização da conta.

O uso do serviço também pode gerar custos relacionados à quantidade de tokens processados.

A utilização do LangChain facilita a integração e a organização das chamadas, mas não elimina a latência e os custos do serviço externo.

## Conclusão

Consegui implementar a estrutura da API com FastAPI e LangChain, incluindo o recebimento de dados, a configuração do modelo e o tratamento de erros.

A tradução real não foi validada devido à falha encontrada durante a chamada à OpenAI. O projeto permanece preparado para novos testes quando houver acesso disponível à API.

## Autor

Leonardo Luiz Tormem