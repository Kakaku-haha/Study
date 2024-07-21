import os
import re


findDuplicate = re.compile(r'(.*)\((.*)\)(.*)')
path = "C:/Users/ZH/Downloads/Pictures"
files = os.listdir(path)
s = []
i = 1
for file in files:
    print(file)
    if re.match(findDuplicate,file):
        #print(re.match(findDuplicate,file))
        print("重复")
        os.remove(path+'/'+file)
    i +=1
print(i)