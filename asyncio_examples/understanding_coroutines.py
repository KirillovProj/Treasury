import asyncio
import inspect


# Notice that async function is called a coroutinefunction and actually returns coroutine.
async def main():
    return 'Hello World!'


print(type(main))  # <class 'function'>
print(inspect.iscoroutinefunction(main))  # True

coro = main()

print(type(coro))  # <class 'coroutine'>
print(inspect.iscoroutine(coro))  # True


# Here you can see that coroutine is a generator that returns coroutinefunction's return value in StopIteration error
try:
    coro.send(None)  # Function that initiates coroutine, None is passed because it has required positional arg
except StopIteration as e:
    print(e)  # Hello World!

print('========================')


# This is a basic model of how event loop works, around send() and throw() functions.
async def main_2():
    try:
        while True:
            await asyncio.sleep(0)
    except asyncio.CancelledError:
        print('Going for the second awaitable')
        while True:
            await asyncio.sleep(0)

coro = main_2()
coro.send(None)
coro.throw(asyncio.CancelledError)
coro.send(None)





