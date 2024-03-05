import threading

## The simple function that will simply print hello world and the thread that is executing this
def myTask():
    print("Hello World:{}".format(threading.current_thread()))

## We create our first thread and pass it in our mTask() function

myThread = threading.Thread(target=myTask)
#original main thread
myTask()
#we start out the thread
myThread.start()