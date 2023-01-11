"The Visitor Pattern Use Case Example"
from car_parts import Car
from visitor import PrintPartsVisitor, TotalPriceVisitor

CAR = Car("DeLorean")

# Print out the part name and sku using the PrintPartsVisitor
CAR.accept(PrintPartsVisitor())

# Calculate the total prince of the parts using the TotalPriceVisitor
TOTAL_PRICE_VISITOR = TotalPriceVisitor()
CAR.accept(TOTAL_PRICE_VISITOR)
print(f"Total Price = {TOTAL_PRICE_VISITOR.total_price}")
