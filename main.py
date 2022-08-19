from classes import API
from fastapi import FastAPI

app = FastAPI(
    title="API Dicionário - Português Brasil",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1})

"""
# ================================= #

Created by https://github.com/atrikx/

# ================================= #
"""


@app.get("/{palavra}")
async def sinonimos(palavra: str):
    return await API().sinonimos(palavra)
