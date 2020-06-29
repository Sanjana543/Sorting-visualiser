from tkinter import *
from tkinter import ttk
import random
import time

#this is how my window is going to look
root = Tk()
root.title("Sorting Visualisation")
root.maxsize(900,600)
root.config(bg ="white")

#variables
selected_alg = StringVar()
data = []

def Bubblesort(data, draw, Time):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                draw(data, ["steelblue" if k==j or k==j+1 else "black" for k in range(len(data))])
                time.sleep(Time)
    draw(data,["steelblue" for k in range(len(data))])

def Selectionsort(data, draw, Time):
    for i in range(len(data)):
        min=i
        for j in range(i+1,len(data)):
            if data[min] > data[j]:
                min=j
        data[i], data[min] = data[min], data[i]
        draw(data, ["steelblue" if k==min or k==i else "black" for k in range(len(data))])
        time.sleep(Time)
    draw(data,["steelblue" for k in range(len(data))])

def Mergesort(data, draw, Time):
    Mergealg(data, 0, len(data)-1, draw, Time)
    
def Mergealg(data, left, right, draw, Time):
    if left < right:
        mid = (left + right)//2
        Mergealg(data, left, mid, draw, Time)
        Mergealg(data, mid+1, right, draw, Time)   
        Merge(data, left, mid, right, draw, Time)

def Merge(data, left, mid, right, draw, Time):
    draw(data, getColorArray(len(data), left, mid, right))
    time.sleep(Time)
    leftPart = data[left:mid+1]
    rightPart = data[mid+1:right+1]
    leftIndex = rightIndex = 0
    for dataIndex in range(left, right+1):
        if leftIndex < len(leftPart) and rightIndex < len(rightPart):
            if leftPart[leftIndex] <= rightPart[rightIndex]:
                data[dataIndex] = leftPart[leftIndex]
                leftIndex +=1
            else:
                data[dataIndex] = rightPart[rightIndex]
                rightIndex +=1
        elif leftIndex < len(leftPart):
            data[dataIndex] = leftPart[leftIndex]
            leftIndex +=1
        else:
             data[dataIndex] = rightPart[rightIndex]
             rightIndex +=1
    draw(data, ["steelblue" if x>=left and x<=right else "black" for x in range(len(data))])
    time.sleep(Time)

def getColorArray(length, left, mid, right):
    colorArray=[]
    for i in range(length):
        if i>=left and i<=right:
            if i<=mid:
                colorArray.append("white")
            else:
                colorArray.append("steelblue")
        else:
            colorArray.append("black")
    return colorArray
      
def draw(data, colorArray):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 600
    bar_width = canvas_width/(len(data)+1)
    offset = 30
    spacing = 10
    normalizedData = [i/max(data) for i in data]

    #enumerate is used to print data with count i.e., 0 datavalue
    for i, height in enumerate(normalizedData):
        #x0,x1,y0,y1 are edges of rect.
        x0 = i*bar_width+offset+spacing
        y0 = canvas_height-height*340
        x1 = (i+1)*bar_width+offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill = colorArray[i])
        #achor is used to show rel. pos.
        canvas.create_text(x0+2, y0, anchor = SW, text = str(data[i]))
    root.update_idletasks()    

def Generate():
   global data
   MinVal = int(Min.get())
   MaxVal = int(Max.get())
   size = int(Size.get())
  
   data = []
   for i in range(size):
        data.append(random.randrange(MinVal, MaxVal+1))
   draw(data, ["black" for k in range(len(data))])

def StartAlgorithm():
    global data
    if not data:
        return
    if alg_Menu.get() == 'Merge sort':
        Mergesort(data, draw, speed.get())
    elif alg_Menu.get() == 'Bubble sort':
        Bubblesort(data, draw, speed.get())
    else:
        Selectionsort(data, draw, speed.get())
    draw(data, ["steelblue" for x in range(len(data))])
    
#frame & canvas
frame = Frame(root, width = 600, height = 200, bg = "steelblue")
frame.grid(row = 0, column = 0, padx = 5, pady = 5)
canvas = Canvas(root, width = 600, height =380, bg = "white")
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)

#user interface area
label= Label(frame, text = "  Select  Algorithm:", bg = "steelblue")
label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)
alg_Menu = ttk.Combobox(frame, textvariable = selected_alg, values = ['Bubble sort', 'Merge sort', 'Selection sort'])
alg_Menu.grid(row =0, column = 1, padx = 5, pady = 5)
alg_Menu.current(0)

speed = Scale(frame, from_= 0.1, to=2.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed[s]")
speed.grid(row=0, column=2, padx=5, pady=5)
button=Button(frame, text = "Run", fg="white", command = StartAlgorithm, bg = "black").grid(row=0, column = 3, padx=5, pady=5)


Size = Scale(frame, from_= 3, to=25, resolution=1, orient=HORIZONTAL, label="Size")
Size.grid(row = 1, column = 0, padx = 5, pady = 5)


Min = Scale(frame, from_= 0, to=10, length=200, resolution=1, orient=HORIZONTAL, label="Min Size")
Min.grid(row = 1, column = 1, padx = 5, pady = 5)


Max = Scale(frame, from_= 10, to=100, length=200, resolution=1, orient=HORIZONTAL, label="Max Size")
Max.grid(row = 1, column = 2, padx = 5, pady = 5)

button=Button(frame, text = "Bars", fg="white", command = Generate, bg = "black").grid(row=1, column = 3, padx=5, pady=5)

root.mainloop()

