from classes import API
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="API Dicionário - Português Brasil",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1})

"""
# ================================= #

Created by https://github.com/atrikx/

# ================================= #
"""


@app.get("/{palavra}", tags=["Sinônimos"])
async def sinonimos(palavra: str):
    sinonimos = await API().sinonimos(palavra)
    if not sinonimos:
        raise HTTPException(status_code=400, detail="Palavra inválida")
    return sinonimos
