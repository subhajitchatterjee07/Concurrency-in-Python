import asyncio

async def myCoroutine():
    print("Simple Event loop example")

def main():
    # define an instance of an event loop 
    loop = asyncio.get_event_loop()
    #tell this event loop to run until all the tasks assigned to it are completed.
    #This example  just the execution of coroutine() coroutine.
    loop.run_until_complete(myCoroutine())
    #tidying up loop by calling close()
    loop.close()

if __name__ =='main':
    main()