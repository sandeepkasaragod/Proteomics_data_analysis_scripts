import os
import threading
import sys
#Check if the dependency packages are installed
try:
    import concurrent.futures
except:
    print ("Module does not exist, run command in terminal/command_prompt: pip install futures")
    print ("installing module")
    pip.main(["install", "futures"])
    
try:
    import urllib.request
except:
    print ("Modules does not exist, run command in terminal/command_prompt: pip install urllib")
    print ("installing module")
    pip.main(["install", "urllib"])
        
from concurrent.futures import wait, ALL_COMPLETED

links = []
def read_links(infile):
    with open(infile) as f:
        for i in f:
          links.append(i.rstrip())

def download_file(url):
    try:
        extension = url.split('.')[-1]
        file_name = url.split('/')[-1].split('.')[0] + "." + extension
        urllib.request.urlretrieve(url, file_name)
    except IOError as e:
        print (e)
        print ("Path migh be the problem. Follow the below example to check if the link is working fine")
        print ("urllib.urlretrieve(http://test/test.txt, test.txt)")

def download(infile, num_threads):
    try:
        thread = int(num_threads)
        start = 0
        end = thread
        read_links(infile)
        iters = int((len(links)/thread))
        for i in range(iters):
            if i + 1 != iters:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    print ("Links currently downloading are")
                    print ([a for a in links[start:end]])
                    completed = [executor.submit(download_file, url) for url in links[start:end]]
                    wait(completed, return_when=ALL_COMPLETED)
                    start = end
                    end = end + thread

            else:
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    print ("Links currently downloading are")
                    print ([a + '\n' for a in links[start:]])
                    completed = [executor.submit(download_file, url) for url in links[start:]]
                    wait(completed, return_when=ALL_COMPLETED)

    except:
        e = sys.exc_info()[0]
        print (e)


if __name__== "__main__":
    if len(sys.argv) == 3:
        #create_dir(sys.argv[3])
        download(sys.argv[1], sys.argv[2])
    else:
        print ("Usage: Bulk_file_downloader.py <input_file> <threads>")
        print ("Example: Bulk_file_downloader.py D:\input_folder\input_file.txt 5")
