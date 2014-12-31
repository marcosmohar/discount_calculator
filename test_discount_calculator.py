import unittest
from discount_calculator import calculate_discount

class discountCalculatorTest(unittest.TestCase):
  def testCalculateDiscount(self):
    discount = calculate_discount(500.0, 50.0, 50.0)
    
    self.assertEqual(discount, 125.0)

  def testNoRelativeDiscount(self):
  	discount = calculate_discount(500.0, 0.0, 50.0)
  	self.assertEqual(discount, 250.0)
  	

  def testNoTotalDiscount(self):
  	discount = calculate_discount(500.0, 50.0, 0.0)
  	self.assertEqual(discount, 250.0)

  def testAbsentItemCost(self):
  	with self.assertRaises(ValueError):
  		discount = calculate_discount(0.0, 50.0, 50.0)
  	

  def testExcesiveDiscount(self):
  	with self.assertRaises(ValueError):
  		discount = calculate_discount(100.0, 120.0, 50.0)

if __name__ == "__main__":
  unittest.main()