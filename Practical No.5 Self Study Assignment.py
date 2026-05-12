#1. Advanced Data Visualization

#a) Span Selector (Interactive Range Selection)
import numpy as np
from matplotlib.widgets import SpanSelector

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

def onselect(xmin, xmax):
    print("Selected range:", xmin, xmax)

span = SpanSelector(ax, onselect, 'horizontal')
plt.title("Span Selector Example")
plt.show()

#b) Broken Horizontal Bar Plot
plt.figure()
plt.broken_barh([(10, 5), (20, 3)], (1, 0.5))
plt.title("Broken Horizontal Bar Plot")
plt.xlabel("Time")
plt.ylabel("Task")
plt.show()

#c) Watermarking Images Using Matplotlib
import matplotlib.image as mpimg

img = mpimg.imread("image.jpg")

plt.figure()
plt.imshow(img)
plt.text(20, 20, "CONFIDENTIAL", fontsize=20)
plt.axis("off")
plt.title("Watermarked Image")
plt.show()

#2. Apply Linear Regression and K-Nearest Neighbour
#Dataset: Salary vs Experience (Real-Life Example)

#Linear Regression
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([30000, 35000, 40000, 45000, 50000])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[6]])
print("Predicted Salary:", prediction)

#K-Nearest Neighbour Classifier
from sklearn.neighbors import KNeighborsClassifier

X = [[1, 100], [2, 150], [3, 200], [4, 250]]
y = ["Low", "Low", "Medium", "High"]

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

result = knn.predict([[3, 180]])
print("Predicted Category:", result)
