import asyncio


async def main():
    lst = [i ** 2 for i in range(10)]

    async for value in AsyncIterable(lst):  # Declaration for async loop
        print(value)


class AsyncIterable:
    def __init__(self, data):
        self.data = data

    # Note that this method should be declared without "async" keyword
    def __aiter__(self):  # Must return instance of a class with implemented __anext__ method.
        self.iterable_data = iter(self.data)
        return self

    async def __anext__(self):
        try:
            n = next(self.iterable_data)
            await asyncio.sleep(1)  # Insert some non-blocking function here
        except StopIteration:
            raise StopAsyncIteration  # This will be a signal for async loop to end

        return n


asyncio.run(main())
