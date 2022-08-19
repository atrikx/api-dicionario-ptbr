from bs4 import BeautifulSoup
from aiohttp import ClientSession
from responseModel import Response


class API:
    url = f"https://www.dicio.com.br/"
    __classSinonimos = 'adicional sinonimos'
    typeParse = 'html.parser'

    async def pesquisar_palavra(self, palavra: str):
        async with ClientSession() as s, s.get(self.url+palavra) as r:
            pageResponse = await r.text()
            return BeautifulSoup(pageResponse, self.typeParse)

    async def sinonimos(self, palavra):
        soup = await self.pesquisar_palavra(palavra)
        sinonimos = soup.find(class_=self.__classSinonimos)
        resultado = [tag.text.strip() for tag in sinonimos.find_all('a')]
        return await Response().Sinonimos(resultado)


