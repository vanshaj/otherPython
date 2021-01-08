#!/bin/python
import os
import requests
import timeit
import threading

def downloadImage(imagePath,fileName):
   with open(fileName,'wb') as imageWrite: # will open the file in write mode as binary file
       response=requests.get(imagePath,stream=True) # will get the request but in the stream form i.e the whole data will not be loaded in memory directly instead it will be in chunks
       if not response.ok:
           print(response)
       for block in response.iter_content(1024): #here we mention the chunk size to iterate over the content in 1024 bytes
           if not block:
               break
           imageWrite.write(block)

def mythread(i):
        imagePath="https://fakeimg.pl/350x200/?text=Hell"+str(i)
        fileName="Hell"+str(i)
        filePath=os.getcwd()+'\\..\\resource\\'+fileName
        downloadImage(imagePath,filePath)

if __name__ == '__main__':
    start=timeit.default_timer()
    threads=[] # Creation of list of threads will store reference to all of our threads
    for i in range(10):
        thread = threading.Thread(target=mythread,args=(i,)) # will create a thread target will be the method to be executed for our thread and args will contain the arguments
        threads.append(thread) # will append the thread in our list
        thread.start() # will actually start the thread
    for i in threads:
        i.join() # will wait for all threads to execute before logging time
    end=timeit.default_timer()
    print(end-start)
