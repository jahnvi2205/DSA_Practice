def middle(self, a, b, c):
        if a>b:
            if a<c:
                return a
            else:
                return b if b>c else c
        else:
            if b<c:
                return b
            else:
                return a if a>c else c