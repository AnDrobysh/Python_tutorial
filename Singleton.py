class PenisInAss(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(PenisInAss, cls).__new__(cls)
        return cls.instance


p = PenisInAss()
print(p)

f = PenisInAss()
print(f)
