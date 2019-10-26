
import requests
import sys

arguments=sys.argv
url=arguments[1]
filename=arguments[2]
path=arguments[3]

def downloadfile(filename,url,path):
    downloadedresponse=requests.get(url)
    newfile=open("{path}{filename}".format(path=path,filename=filename),'wb')
    newfile.write(downloadedresponse.content)
    newfile.close()

downloadfile(filename,url,path)