import asyncio


class Connection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # This function executes right before code within 'with' block
    async def __aenter__(self):
        self.conn = await self.get_conn(self.host, self.port)
        print('Entering context manager')
        return self.conn

    # This function executes after the last line of code within 'with' block
    async def __aexit__(self, exc_type, exc, tb):
        await self.close_conn()
        print('Leaving context manager')

    async def get_conn(self, host, port):
        pass

    async def close_conn(self):
        pass


async def main():
    async with Connection('localhost', 9001) as conn:
        print('Inside context manager')


asyncio.run(main())

# Entering context manager
# Inside context manager
# Leaving context manager
