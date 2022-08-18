import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI


app = FastAPI()


@app.get("/{palavra}")
async def sinonimos(palavra: str):
    url = f"https://www.dicio.com.br/{palavra}/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    sinonimos = soup.find(class_='adicional sinonimos')
    resultado = []
    for tag in sinonimos.find_all('a'):
        resultado.append(tag.text.strip())
    return resultado
