class Response:
    sinonimos: dict = {}

    async def Sinonimos(self, resultado):
        self.sinonimos['sinonimos'] = resultado
        return self.sinonimos
