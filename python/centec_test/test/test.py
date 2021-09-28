
def demo():
    a = 1
    b = a
    print(f"a -> {hex(id(a))} -> {a}")
    print(f"b -> {hex(id(b))} -> {b}")
    a = 2  # create 2 and bound to a, b stays the same
    print(f"a -> {hex(id(a))} -> {a}")
    print(f"b -> {hex(id(b))} -> {b}")

    L1 = [1, 2, 3]
    L2 = L1.copy()
    print(f"L1 -> {hex(id(L1))} -> {L1}")
    print(f"L2 -> {hex(id(L2))} -> {L2}")
    L1[0] = 4  # update the first elem of L1
    print(f"L1 -> {hex(id(L1))} -> {L1}")
    print(f"L2 -> {hex(id(L2))} -> {L2}")

demo()
