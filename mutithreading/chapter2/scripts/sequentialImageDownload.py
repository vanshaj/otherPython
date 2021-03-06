#!/bin/python
import os
import requests
import timeit


def downloadImage(imagePath,fileName):
   with open(fileName,'wb') as imageWrite: # will open the file in write mode as binary file
       response=requests.get(imagePath,stream=True) # will get the request but in the stream form i.e the whole data will not be loaded in memory directly instead it will be in chunks
       if not response.ok:
           print(response)
       for block in response.iter_content(1024): #here we mention the chunk size to iterate over the content in 1024 bytes
           if not block:
               break
           imageWrite.write(block)

if __name__ == '__main__':
    start=timeit.default_timer()
    for i in range(10):
        imagePath="https://fakeimg.pl/350x200/?text=Hell"+str(i)
        fileName="Hell"+str(i)
        filePath=os.getcwd()+'\\..\\resource\\'+fileName
        downloadImage(imagePath,filePath)
    end=timeit.default_timer()
    print(end-start)
