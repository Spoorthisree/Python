import numpy as np
arr=np.array([1,2,3,4,5])
print(arr[0])
print(arr[1:3])
print(arr.dtype)

import numpy as np
arr=np.array(["apple","banana"])
print(arr.dtype)

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print (newarr)

import numpy as np
arr=np.array([[1,2,3,4,5],[3,4,5,6,7]])
for x in arr:
    print(x)

import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([0,6])
ypoints=np.array([6,250])

plt.plot(xpoints, ypoints)
plt.show()

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
zpoints = np.array([3,8,1,10])
ypoints =np.array([1,2,3,4])

plt.plot(zpoints,ypoints,marker="*")
plt.show()

import matplotlib.pyplot as plt
 
# x-axis and y-axis values for plotting
x = [1, 2, 3, 4, 5, 6]
y = [3, 1, 4, 5, 3, 6]
 
# labels for x-asix
labels = ['A', 'B', 'C', 'D', 'E', 'F']
 
# Plotting x-axis and y-axis
plt.plot(x, y)
 
# naming of x-axis and y-axis
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
 
# naming the title of the plot
plt.title("Set X-Axis Values in Matplotlib")
 
# setting x-axis values
plt.xticks(x, labels,rotation=90)
 
plt.show()

import matplotlib.pyplot as plt
import numpy as np
zpoints = np.array([3,8,1,10])
ypoints =np.array([1,2,3,4])
plt.title("sports watch data")
plt.xlabel("average pulse")
plt.ylabel("calorie burnage")

plt.bar(x,y,color="hotpink")
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x = np.array([3,8,1,10])
y =np.array([1,2,3,4])
plt.scatter(x,y,color="orange")

x =np.array ([1, 2, 3, 4, 5, 6])
y = np.array([3, 1, 4, 5, 3, 6])
plt.scatter(x,y,color="hotpink")

plt.show()

import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1,color="green")
plt.plot( x2, y2,color="orange")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabeles=["python","sql","R","RM"]

plt.pie(y,labels=mylabeles)
plt.show() 
