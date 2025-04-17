from pet import Pet

# Test all methods step by step
my_pet = Pet("KOKO")

print("Initial status:")
my_pet.get_status()
print()

print("After eating:")
my_pet.eat()
my_pet.get_status()
print()

print("After sleeping:")
my_pet.sleep()
my_pet.get_status()
print()

print("After playing:")
my_pet.play()
my_pet.get_status()
print()

print("Training tricks:")
my_pet.train("sit")
my_pet.train("roll over")
my_pet.show_tricks()
