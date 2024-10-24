class DigitRetrieve:
    def __call__(self, *args, **kwargs):
        try:
            res = int(args[0])
            return res
        except:
            return None

dg = DigitRetrieve()
d1 = dg("123")   # 123 (целое число)
d2 = dg("45.54")   # None (не целое число)
d3 = dg("-56")   # -56 (целое число)
d4 = dg("12fg")  # None (не целое число)
d5 = dg("abc")   # None (не целое число)

