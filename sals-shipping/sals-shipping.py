weight = float(input("Enter a weight (lbs) to check price comparison for Sally'shipping services: "))

#Ground Shipping
cost_ground = 0

if weight <= 0:
  cost_ground = "invalid - Enter a higher weight"
elif weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping cost £" + str(cost_ground))

# Premium Ground Shipping
cost_ground_premium = 125.00
print("Ground Shipping Premium £" + str(cost_ground_premium))


# Drone Shipping
cost_drone = 0

if weight <= 0:
  cost_drone = "Invalid - Enter a higher weight"
elif weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

print("Drone Shipping cost £" + str(cost_drone))