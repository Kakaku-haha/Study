# 导入所有必要的库
import cv2
import os
def Vid2Pic(url,path,frameNum,file):
    cam = cv2.VideoCapture(url)
    currentframe = 0
    while ( True ):
        # reading from frame
        ret, frame = cam.read()
        
        if ret:
            # 如果视频仍然存在，继续创建图像
            name = path+"/" + file +str(currentframe)  + '.jpg'
            # 写入提取的图像
            if currentframe % frameNum == 0:#50帧一次
                cv2.imencode('.jpg',frame)[1].tofile(name.replace(".mp4",""))
                #cv2.imwrite(name, frame)   
            currentframe += 1
        else :
            break
    cam.release()
    cv2.destroyAllWindows()
path = "C:/Users/ZH/Downloads/vide"
files = os.listdir(path)
for file in files:
    print(file)
    Vid2Pic(path+"/"+file,"C:/Users/ZH/Downloads/V2P",50,file)