#---------------------------------------------------------------------------------------------------
#   Script by:-  VEDANT VINAYAK KULKARNI
#---------------------------------------------------------------------------------------------------
import os
import random

path1 = "D:\\Data\\D\\PYTHON_PROJECTS\\MiniProjectVS\\Landmark\\dataset\\train\\angry\\"
path2 = "D:\\Data\\D\\PYTHON_PROJECTS\\MiniProjectVS\\Landmark\\dataset\\train\\disgust\\"
path3 = "D:\\Data\\D\\PYTHON_PROJECTS\\MiniProjectVS\\Landmark\\dataset\\train\\fear\\"
path4 = "D:\\Data\\D\\PYTHON_PROJECTS\\MiniProjectVS\\Landmark\\dataset\\train\\happy\\"
path5 = "D:\\Data\\D\\PYTHON_PROJECTS\\MiniProjectVS\\Landmark\\dataset\\train\\neutral\\"
path6 = "D:\\Data\\D\\PYTHON_PROJECTS\\MiniProjectVS\\Landmark\\dataset\\train\\sad\\"
path7 = "D:\\Data\\D\\PYTHON_PROJECTS\\MiniProjectVS\\Landmark\\dataset\\train\\surprise\\"


angry = list()
disgust = list()
fear = list()
happy = list()
neutral = list()
sad = list()
surprise = list()


for filename in os.listdir(path1):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        angry.append(filename)
    else:
        continue
    
for filename in os.listdir(path2):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        disgust.append(filename)
    else:
        continue

for filename in os.listdir(path3):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        fear.append(filename)
    else:
        continue

for filename in os.listdir(path4):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        happy.append(filename)
    else:
        continue

for filename in os.listdir(path5):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        neutral.append(filename)
    else:
        continue

for filename in os.listdir(path6):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        sad.append(filename)
    else:
        continue

for filename in os.listdir(path7):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        surprise.append(filename)
    else:
        continue

randoms = []
randoms1 = []

for i in range(0,300):
    randoms.append(random.randint(0,3001))

for i in range(0,200):
    randoms1.append(random.randint(0,436))

