def calculate_discount(item_cost, relative_discount, total_discount):
  
  if relative_discount > 99.9 or total_discount > 99.9:
  	raise ValueError("The discount can't be higher than 100%")
  
  if item_cost <= 0.0:
    raise ValueError("You can't discount from zero")

  rd = item_cost * (relative_discount/100)
  td = (item_cost - rd) * (total_discount/100)
  rd = item_cost -rd

  return rd - td


if __name__ == '__main__':
  item = float(raw_input("Enter item cost: "))
  discount = float(raw_input("How much was the original discount: "))
  total = float(raw_input("What was the extra discount for the item:"))

  print "The price of your item after the discounts it ${}".format(calculate_discount(item, discount, total))
