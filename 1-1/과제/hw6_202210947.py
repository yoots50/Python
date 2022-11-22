
import sympy as sp

x, k = sp.symbols('x k')

fx = sp.exp(2*x)*sp.sin(3*x)

fx1 = sp.diff(fx,x)

fx2 = sp.diff(fx,x,2)

sp.solve(fx2 + k*fx1 + 13*fx)

