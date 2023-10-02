import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,10])
y = np.array([0,200])
plt.plot(x,y)
plt.show()


x = [5,2,9,4,7]
y = [10,5,8,4,2]
plt.plot(x,y)
plt.show()


x = np.array([0,10])
y = np.array([0,200])
plt.plot(x,y,color = "red",linestyle = "dashed",linewidth = 2, marker = 'o', markerfacecolor = 'red', markersize = 12)
plt.xlabel("Number")
plt.ylabel("Values")
plt.title("Line plot")
plt.show()


x = [10,20,30,40,50]
y = [20,40,60,100,90]
plt.plot(x,y,label = "line1",marker = 'o',markersize = 12,markerfacecolor = 'red')
plt.plot(y,x,label = "line2",marker = '+',markersize = 12,markerfacecolor = 'green')
plt.xlabel("Number")
plt.ylabel("Value")
plt.legend()
plt.show()


x = [5,2,9,4,7]
y = [10,5,8,4,2]
plt.bar(x,y)
plt.show()


student = {"Maths":20,"science":15,"Social":30,"English":35}
subject = list(student.keys())
registeredno = list(student.values())
plt.bar(subject,registeredno,color = "orange",width = 0.5)
plt.xlabel("Courses")
plt.ylabel("Total Registered")
plt.title("Student Details")
plt.show()


import numpy as np
import matplotlib.pyplot as plt
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
CSE = [12, 30, 1, 8, 22]
ECE = [28, 6, 16, 5, 10]
MECH = [29, 3, 24, 25, 17]
br1 = np.arange(len(CSE))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
plt.bar(br1,CSE, color ='r', width = barWidth, edgecolor ='white', label ='CSE')
plt.bar(br2,ECE, color ='g', width = barWidth,edgecolor ='black', label ='ECE')
plt.bar(br3,MECH, color ='b',width = barWidth,edgecolor ='grey', label ='MECH')
plt.xlabel('Branch', fontweight ='bold', fontsize = 15)
plt.ylabel('Students passed', fontweight ='bold', fontsize = 15)
plt.show()


