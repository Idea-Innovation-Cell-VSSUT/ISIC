import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('data.txt', sep=" ", header=None , names=["a","b","c","d","e"])
x=df["b"].tolist()
print(x)
df['a'] = df['a'].map(lambda x: x.lstrip('+-').rstrip('\tReading:'))
y=df["a"].tolist()
print(y)

n=5
def divide_chunks(x, n):
    # looping till length l
    for i in range(0, len(x), n):
        yield x[i:i + n]

    # How many elements each


a=[]
b = list(divide_chunks(x, n))
print("The list is")
print(b)

for elements in b:
    val=(sum(elements)/5)
    a.append(val)

print("Final Values")
print(a)

fl=len(a)
time_array=[]
for i in range(fl):
    time_array.append(i)





plt.rcParams['figure.figsize'] = (10, 5)
plt.xlabel('Time (s)')
plt.ylabel('Thrust (N)')
plt.plot(time_array,a)
plt.show()

area=np.trapz(a, dx=5)
print("Area:")
print(area)
print("The Impulse is "+str(area)+" Ns")
mass_fuel=float(input("Enter the amount of Fuel Taken in Kg "))
specific_impulse=float(area/mass_fuel)
print(specific_impulse)
print("The Specific Impulse is "+str(specific_impulse)+" m/s")