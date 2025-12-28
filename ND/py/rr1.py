import numpy as np
import sympy as sp 




x0 = 0
y0 = 0
v0 = 6.73
a0 = 60


class projectileMotion:

    m = 0.6; # (*Масса мяча*)
    R = 0.12; # (*Радиус мяча*)
    r = 0.457/2; # (*Высота кольца*)
    L = 3; # (*Расстояние от баскетболиста до кольца*)

    mu = 0.0182
    kr = 6*3.14159 * mu * R
    g = 9.8

    def __init__(self, v0, a0, x0, y0, m=m, R=R, r=r, L=L, kr=kr, g=g):
        self.v0 = v0; self.a0 = np.deg2rad(a0)
        self.x0, self.y0 = x0, y0
        self.m = m; self.R = R; self.r = r; self.L = L; self.kr = kr
        self.v0x = v0 * np.cos(np.deg2rad(a0))
        self.v0y = v0 * np.sin(np.deg2rad(a0))
    
    def trajectory(self):
        # Вводим символы
        t = sp.Symbol("t")
        x, y = sp.Function("x")(t), sp.Function("y")(t)

        Eqx = sp.Eq(self.m * sp.diff(x, t, 2), 0) # Ур движ по Ox
        Eqy = sp.Eq(self.m * sp.diff(y, t, 2) - self.g * self.m, 0) # Ур движ по Oy

        init_cond = {
            x.subs(t, 0): self.x0,              # x(x) = x0
            sp.diff(x, t).subs(t, 0): self.v0x, # xx(0) = v0x
            y.subs(t, 0): self.y0,              # y(0) = y0
            sp.diff(y, t).subs(t, 0): self.v0y  # yy(0) = v0y
        }

        return Eqx.simplify(), Eqy.simplify(), init_cond
    
    def solve_trajectory(self):
        # Получаем уравнения движения
        Eqx, Eqy, init_cond = self.trajectory()


        t_sym = sp.Symbol('t')
        x_sol = sp.dsolve(Eqx, icd=init_cond, hint='best')
        y_sol = sp.dsolve(Eqy, icd=init_cond, hint='best')
            

            
        return x_sol, y_sol



one = projectileMotion(v0, a0, x0, y0)
print(one.solve_trajectory())
