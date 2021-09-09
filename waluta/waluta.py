
from euro import Euro

class Waluta(float):

    def __new__(cls, nazwa):

        if nazwa == 'euro':
            return float.__new__(cls, Euro())