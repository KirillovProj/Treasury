import asyncio


async def main():  # This is how you define async function
    print('Hello asyncio')
    await asyncio.sleep(1)
    print('Goodbye asyncio')


async def main_2():
    print('Hello world')
    await asyncio.sleep(3)
    print('Goodbye world')


async def main_3():
    print('Hello user')
    await asyncio.sleep(3)
    print('Goodbye user')

loop = asyncio.get_event_loop()  # Getting event loop, inside which async tasks will run
task = loop.create_task(main())  # This is how you create a task from your coroutine (call of async func)

task.set_name('main')  # Sets name for pending task
task.get_name()  # Get name of pending task
task.get_coro()  # Get current coroutine
task.get_loop()  # Get current loop in which task is

loop.run_until_complete(task)  # Run loop (Note: all tasks in loop will run) until passed coroutine/task is complete

print('=========================')

# asyncio.run(main())  # This will create event loop and run_until_complete passed coroutine, then close loop

group = asyncio.gather(main(), main_2(), main_3())  # This code will collect multiple tasks inside the loop
loop.run_until_complete(group)

print('=========================')

main_task = loop.create_task(main())
loop.create_task(main_2())
loop.create_task(main_3())
loop.run_until_complete(main_task)
pending = asyncio.all_tasks(loop=loop)  # This will get the list of all pending tasks
for coro in pending:
    coro.cancel()  # This will cancel coroutine/task. Note that main_2() and main_3() coro won't be completed since
                   # They will be canceled before that.


loop.close()  # This will close the loop for good


