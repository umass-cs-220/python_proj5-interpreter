class GlobalEnv:
    pass


class LocalEnv:
    pass


if __name__ == '__main__':
    g = GlobalEnv.empty()
    g = g.extend(['a', 'b'], [1, 2])
    print(g.lookup('a'))
    l = g.extend(['x', 'y'], [3, 4])
    print(l.lookup('a'))
    print(l.lookup('b'))
    print(l.lookup('x'))
    print(l.lookup('y'))
