class Car:
    def __init__(self, model, color, year, for_sale) :
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You are driving {self.model}")

    def stop(self):
        print(f"You've just stopped the {self.model}")
