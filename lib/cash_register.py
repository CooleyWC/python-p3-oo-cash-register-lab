#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0, items=None):
    self.discount = discount
    self.total = total
    self.items = [] if items == None else items
    self.last_transaction = 0

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, discount):
    self._discount = discount
  
  @property
  def total(self):
    return self._total
  
  @total.setter
  def total(self, total):
    self._total = total

  @property
  def items(self):
    return self._items
  
  @items.setter
  def items(self, items):
    self._items = items

  def add_item(self, title, price, quantity=1):
    items_to_extend = [title] * quantity
    self.items.extend(items_to_extend)
    sub_total = price * quantity
    self.total += sub_total
    self.last_transaction = sub_total
    return self.items

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      difference_of_discount = int(self.total * (self.discount * .01))
      self.total = self.total - difference_of_discount
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    self.total -= self.last_transaction
    self.last_transaction = 0
    
    


