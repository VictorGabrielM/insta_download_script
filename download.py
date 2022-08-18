import json
import sys
import os

print(sys.argv[1],end= " ")

json_file = open(sys.argv[1],"r")
data = json.load(json_file)

urls_file = open("./data/urls.txt","w")

for i in data:
    if i['type'] == "Image":
        urls_file.write(i['displayUrl'] + "\n")
    
    elif i['type'] == "Sidecar":
        images = i['images']
        os.system("mkdir ./data/" + i['id'])
        urls_fileS = open("./data/" + i['id'] + "/urls_sidecar.txt" , "w")
        urls_fileS.write("\n".join(images))
        urls_fileS.close()
        os.chdir(os.getcwd() + "/data/" + i['id'])
        os.system("wget -i ./urls_sidecar.txt")
        os.chdir("../..")
    elif i['type'] == "Video":
        urls_file.write(i['videoUrl'] + "\n")        

json_file.close()
urls_file.close()

os.chdir("./data")
os.system("wget -i ./urls.txt")
os.chdir("..")