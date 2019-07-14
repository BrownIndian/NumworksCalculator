from sympy.solvers import solve
from sympy import Symbol


def createEq():
    # Symbols
    d = Symbol('d')
    t = Symbol('t')
    a = Symbol('a')
    v = Symbol('v')
    v2 = Symbol('v2')
    varz = [d, t, a, v, v2]
    varz = ["d", "t", "a", "v", "v2"]

    # Kinematic Formulas
    formulas = [
        v*t + 0.5*a*t**2 - d,
        v - v2 + a*t,
        v**2 - v2**2 + 2*a*d,
        (v*t + v2*t) / 2 - d,
    ]

    # Assigning Each
    properFormulas = {}
    for var in varz:
        properFormulas[var] = [str(solve(formula, var)[0])
        for formula in formulas if len(solve(formula, var)) != 0]
    return properFormulas

def userEq():
    pfunx = createEq()
    for pfunc, values in pfunx.items():
        for num in range(0, len(values)):
            if values[num].find('**') > 0:
                values[num] = values[num].replace('**', '^')
            if values[num].find('*') > 0:
                values[num] = values[num].replace('*', '')
            if values[num].find('sqrt') > 0:
                values[num] = values[num].replace('sqrt', 'sqr')
    return pfunx
print(userEq())




