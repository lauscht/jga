class Life:
    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass
    
    def __and__(self, other):
        return life

life = Life()

class Marriage:
    date = 1820

marriage = Marriage()

def jga_test(hint):
    return hint == 3