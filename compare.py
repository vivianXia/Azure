#Author: Xia Lu

import cv2
import numpy as np
import glob
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("data", help = "Path")
args = vars(parser.parse_args())

index = {}
images = {}

for imagePath in glob.glob(args["data"]+"/*.png"):
	#print imagePath
	fname = imagePath[imagePath.rfind("/")+1:]
	image = cv2.imread(imagePath)
	images[fname] = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) 

	hist = cv2.calcHist([image],[0,1,2],None,[64,64,64],[0,256,0,256,0,256])
	hist = cv2.normalize(hist).flatten()
	index[fname] = hist

results={}

for(k,hist) in index.items():
	d = cv2.compareHist(index["doge.png"],hist,cv2.cv.CV_COMP_CORREL)
	results[k] = d

results = sorted([(hist,k)for (k,hist)in results.items()],reverse = True)

fig = plt.figure("Doge")

ax = fig.add_subplot(1,1,1)
ax.imshow(images["doge.png"])
plt.axis("off")

fig = plt.figure("correlation")

for(i,(hist,k)) in enumerate(results):
	print k
	print hist
	ax = fig.add_subplot(1, len(images), i + 1)
	plt.imshow(images[k])
	plt.axis("off")

plt.show()
	
