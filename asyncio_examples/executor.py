# Basic setup for running blocking tasks using executor

import asyncio
import time


async def main():
    print(f'{time.ctime()} Hello asyncio!')
    await asyncio.sleep(1)
    print(f'{time.ctime()} Bye asyncio!')


def executor_main():
    time.sleep(0.5)
    print(f'{time.ctime()} Hello from Executor!')


loop = asyncio.get_event_loop()
task = loop.create_task(main())

loop.run_in_executor(None, executor_main)

loop.run_until_complete(task)


