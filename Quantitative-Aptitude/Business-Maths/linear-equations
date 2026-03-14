#trying to solve equations two variables using cramer rule
# 2x + y = 5
# x + 3y = 10

import numpy as np

cramer = np.array([[2,1],[1,3]])
d1 = np.array([[5,10],[1,3]])
d2 = np.array([[2,1],[5,10]])
if np.linalg.det == 0:
    "No unique solution exists"
else:
     print(f"First soultion is {(np.linalg.det(d1))/(np.linalg.det(cramer))} and second solution is {(np.linalg.det(d2))/(np.linalg.det(cramer))}")

# extending the above framework for a more general instance even extending it for 3 variables
# gets the user input now
# can even solve for 3 variables

import numpy as np


x_var = list(map(float, input("Enter x coefficients separated with a space ").split()))
y_var = list(map(float, input("Enter y coefficients separated with a space: ").split()))
z_var = list(map(float, input("Enter z coefficients separated with a space(Enter 0 0 for 2 equations): ").split()))
coeff = list(map(float, input("Enter constants separated with a space ").split()))

if len(x_var) == len(y_var) == len(coeff) == 2:

    main = np.linalg.det([[x_var[0], y_var[0]],
                          [x_var[1], y_var[1]]])

    det1 = np.linalg.det([[coeff[0], y_var[0]],
                          [coeff[1], y_var[1]]])

    det2 = np.linalg.det([[x_var[0], coeff[0]],
                          [x_var[1], coeff[1]]])

    if main == 0:
        print("No unique solution exists")
    else:
        print(f"x = {det1/main}, y = {det2/main}")

elif len(x_var) == len(y_var) == len(z_var) == len(coeff) == 3:

    main = np.linalg.det([[x_var[0], y_var[0], z_var[0]],
                          [x_var[1], y_var[1], z_var[1]],
                          [x_var[2], y_var[2], z_var[2]]])

    det1 = np.linalg.det([[coeff[0], y_var[0], z_var[0]],
                          [coeff[1], y_var[1], z_var[1]],
                          [coeff[2], y_var[2], z_var[2]]])

    det2 = np.linalg.det([[x_var[0], coeff[0], z_var[0]],
                          [x_var[1], coeff[1], z_var[1]],
                          [x_var[2], coeff[2], z_var[2]]])

    det3 = np.linalg.det([[x_var[0], y_var[0], coeff[0]],
                          [x_var[1], y_var[1], coeff[1]],
                          [x_var[2], y_var[2], coeff[2]]])

    if main == 0:
        print("No unique solution exists")
    else:
        print(f"x = {det1/main}, y = {det2/main}, z = {det3/main}")

else:
    print("Unsupported variable number or some unexpected error")


#plotting lines to see equations solutions visually

import matplotlib.pyplot as plt

x_term =  float(input("Enter x coefficient "))
constant = float(input("Enter constant"))
x_term_2 = float(input("Enter x coefficient of 2nd equation "))
constant_2 = float(input("Enter constant of 2nd equation"))

x = np.linspace(0,20,1000)
y = (x_term * x) + constant

x_2 = np.linspace(0,20,1000)
y_2 = (x_term_2 * x_2) + constant_2

fig, ax = plt.subplots(figsize = (20,20), layout = "constrained")
ax.plot(x, y, label = "Equation 1", color = "red")
ax.plot(x_2, y_2, label = "Equation 2", color = "cyan")
ax.legend()
ax.grid()
ax.set_xticks(np.arange(0,20,0.5))
ax.set_yticks(np.arange(0,160,5))
plt.show()
