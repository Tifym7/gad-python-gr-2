class Fractie(object):
    """o fractie are numarator si numitor"""

    def __init__(self, nr, num):
        "setam numitorul si numaratorul"
        self.nr = nr
        self.num = num

    def __str__(self):
        """afisam fractia"""
        return f"{self.nr}/{self.num}"

    def __add__(self, other):
        new_nr = self.nr * other.num + other.nr * self.num
        new_num = self.num * other.num
        return Fractie(new_nr,new_num)

    def __sub__(self, other):
        new_nr = self.nr * other.num - other.nr * self.num
        new_num = self.num * other.num
        return Fractie(new_nr, new_num)

    def inverse(self):
        return Fractie(self.num,self.nr)