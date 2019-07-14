import math

compval = ""
uinp = []
matches = 0
count = 0


def var():
    # d = 0
    # t = 0
    # a = 0
    # v = 0
    # v2 = 0
    varz = ["d", "t", "a", "v", "v2"]
    for var in varz:
        exec(var + "=5")


def fun(num):
    if num == 0:
        return {
            'd': ['0.5*t*(a*t + 2.0*v)', '(-v**2 + v2**2)/(2*a)', 't*(v + v2)/2'],
            't': ['(-v + math.sqrt(2.0*a*d + v**2))/a', '(-v + v2)/a', '2*d/(v + v2)'],
            'a': ['2.0*(d - t*v)/t**2', '(-v + v2)/t', '(-v**2 + v2**2)/(2*d)'],
            'v': ['-0.5*a*t + d/t', '-a*t + v2', 'math.sqrt(-2*a*d + v2**2)', '2*d/t - v2'],
            'v2': ['a*t + v', 'math.sqrt(2*a*d + v**2)', '2*d/t - v']
        }
    return {
        'd': ['0.5t(at + 2.0v)', '(-v^2 + v2^2)/(2a)', 't(v + v2)/2'],
        't': ['(-v + sqr(2.0ad + v^2))/a', '(-v + v2)/a', '2d/(v + v2)'],
        'a': ['2.0(d - tv)/t^2', '(-v + v2)/t', '(-v^2 + v2^2)/(2d)'],
        'v': ['-0.5at + d/t', '-at + v2', 'sqr(-2ad + v2^2)', '2d/t - v2'],
        'v2': ['at + v', 'sqr(2ad + v^2)', '2d/t - v']
    }


def lpf(num):
    pfunx = fun(num)
    uinp = input("Type in d, t, a, v, or v2: ")
    global compval
    compval = uinp
    return [equ for pfunc, equ in pfunx.items() if pfunc == uinp][0]


def deq(num):
    def isfloat(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def feq(arr):
        varz = ["d", "t", "a", "v", "v2"]
        eqs = lpf(1)
        count = []
        dum = [1 if isinstance(arr[num], float) else 0 for num in range(0, len(arr))]
        for eq in eqs:
            dum2 = [1 if eq.find(var) >= 0 else 0 for var in varz]
            if len(dum2) == len(varz):
                count.append(len([num for num in range(0, len(arr)) if dum[num] == dum2[num]]))
        global matches
        matches = str(max(count))
        return str(count.index(max(count)))

    def arr():
        userInp = input("[d, t, a, v, v2]:\n").split(',')
        return [float(var) if var.isdigit() or var[1:].isdigit() or isfloat(var) else "" for var in userInp]

    ar = arr()
    global uinp
    uinp = ar
    global d
    global t
    global a
    global v
    global v2
    d = uinp[0]
    t = uinp[1]
    a = uinp[2]
    v = uinp[3]
    v2 = uinp[4]
    eq = feq(uinp)
    global count
    count = int(eq[0])
    return fun(num)[compval][count]


def sol():
    def prM(value):
        try:
            return eval(value)
        except (ValueError, TypeError):
            return False

    equ = deq(0)
    global count
    print(fun(1)[compval][count], "Matches:", matches)
    var()
    return prM(equ)

print(sol())
