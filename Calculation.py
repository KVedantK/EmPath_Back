#---------------------------------------------------------------------------------------------------
#   Script by:-  VEDANT VINAYAK KULKARNI
#---------------------------------------------------------------------------------------------------

import pandas as pd
import csv

def Eucledian(x,y):
    x = list(x)
    y = list(y)

    x1 = x[1] + x[2] + x[3]
    y1 = x[6] + x[7] + x[8]
    
    x2 = y[1] + y[2] + y[3]
    y2 = y[6] + y[7] + y[8]

    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    print("x1 = {}, y1 = {}, x2 = {}, y2 = {}".format(x1,y1,x2,y2))
    return (((x2-x1)**2) + ((y2-y1)**2))**0.5


column_names = ['emotion', 'Top', 'Bottom', 'Left', 'Right', 'Chin']
df = pd.read_csv("CleanLipsNew.csv", names=column_names)
Emotions = df.emotion.to_list()
Top = df.Top.to_list()
Bottom = df.Bottom.to_list()
Left = df.Left.to_list()
Right = df.Right.to_list()
Chin = df.Chin.to_list()
print(Top)
Fields_Eucledian = ['emotion','T_L','T_R','B_L','B_R','B_C']
with open('EucledianNew.csv','a') as ef:
    csvwriter = csv.writer(ef)
    csvwriter.writerow(Fields_Eucledian)
    for i in range(1,823):
        print("Element {}/823 being written...".format(i))
        current_emotion = Emotions[i]
        Top_Left = Eucledian(Top[i],Left[i])
        Top_Right = Eucledian(Top[i],Right[i])
        Bottom_Left = Eucledian(Bottom[i],Left[i])
        Bottom_Right = Eucledian(Bottom[i],Right[i])
        Bottom_Chin = Eucledian(Bottom[i],Chin[i])

        print("points {}, {}, {}, {}, {}, {} are under process".format(Emotions[i],Top[i],Bottom[i],Left[i],Right[i],Chin[i]))

        row = [current_emotion,Top_Left,Top_Right,Bottom_Left,Bottom_Right,Bottom_Chin]
        csvwriter.writerow(row)

        print("Data Written Successfully...")
        print("*************************************************************************************")





