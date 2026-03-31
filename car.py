
class Car:
  def __init__(self, make, model, year, price, mileage, id=None):
    self.make = make
    self.model = model
    self.year = year
    self.price = price
    self.mileage = mileage
    self.id = id

  def __str__(self):
    return (f"[Car ID: {self.id}] | Make: {self.make} | Model: {self.model} | "
            f"Year: {self.year} | Price: ${self.price:,.2f} | Mileage: {self.mileage:,} km")

  def to_tuple(self):
    return (self.make, self.model, self.year, self.price, self.mileage)