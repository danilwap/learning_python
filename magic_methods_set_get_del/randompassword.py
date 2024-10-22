import random
class RandomPassword:
    def __init__(self, psw_chars, min_length, max_length):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        password = ''
        for i in range(random.randint(self.min_length, self.max_length)):
            password += random.choice(self.psw_chars)

        return password


min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rp = RandomPassword(psw_chars, min_length, max_length)
lst_pass = [rp() for _ in range(3)]
print(lst_pass)