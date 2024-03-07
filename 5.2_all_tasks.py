import asyncio
import time

async def myTask():
    time.sleep(1)
    print("Processing Task")

async def main():
    for i in range(5):
        asyncio.ensure_future(myTask())
        pending = asyncio.Task.all_tasks()
        print(pending)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("Completed all tasks")
loop.close()