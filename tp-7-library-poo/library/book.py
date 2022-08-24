class Book():
    def __init__(self, title='', price=0, quantity=0):
        self._title = title
        self._price = float(created_at)
        self._quantity = float(quantity)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if len(title) > 1:
            self._title = title
        else:
            raise ValueError("Titre du film trop court")

    def price(self):
        pass

    def price(self, price):
        pass

    def quantity(self):
        pass

    def quantity(self, quantity):
        pass
