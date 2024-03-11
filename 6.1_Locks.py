import asyncio
import time

async def myWorker(lock):
    print("Attempting to attain lock")
    ## acquire lock
    async with lock:
        #run critical section of code
        print("Currently Locked")
        time.sleep(2)
    # our worker releases the lock at this point.
    print("Unlocked Critical Section")

async def main():
    #instantiate the lock
    lock = asyncio.Lock()
    #await the execution of 2 myworker coroutines 
    #each with the samme instance passed in.
    await asyncio.wait([myWorker(lock), myWorker(lock)])

#start up a simple loop and run our main function.
#until complete.
lock = asyncio.Lock()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("All Tasks Completed")
loop.close()