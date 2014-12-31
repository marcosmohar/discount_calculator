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
	print calculate_discount(100.0, 10.0, 20.0)
	print calculate_discount(500.0, 50.0, 50.0)
	print calculate_discount(500.0, 80, 80)
	print calculate_discount(100.0, 110, 50)
	print calculate_discount(0, 50.0, 50.0)