from matrix import *
import sys
import matplotlib.pyplot as plt

if sys.argv != 2:
    print("Error: Invalid format")
    print("Usage: python3 native_regression.py <filename>")
    sys.exit()

filename = sys.argv[1]
M = loadtxt(f"{filename}")
if M == None:
    sys.exit()
XY = transpose(M)

X = XY[0]
Y= XY[1]

Xp  = powers(X,0,1)
Yp  = powers(Y,1,1)
Xpt = transpose(Xp)

[[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

Y2 = []
for i in X:
    Y2.append(i*b+m)

plt.plot(X,Y, "ro")
plt.plot(X,Y2)
plt.show()
