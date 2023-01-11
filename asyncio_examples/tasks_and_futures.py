import asyncio

future = asyncio.Future()
print(future.done())  # Checks if Future is completed, False

print(future.cancelled())  # False
future.cancel()
print(future.cancelled())  # True

future = asyncio.Future()
future.set_result(123)
print(future.result())  # 123
print(future.done())  # True
# Note that you can't cancel the future that is completed
future.cancel()
print(future.cancelled())  # False


