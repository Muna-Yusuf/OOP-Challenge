from pet import Pet

print("Creating pet: Max")
my_pet = Pet("Max")

print(f"{my_pet.name} is eating...")
my_pet.eat()

print(f"{my_pet.name} is playing...")
my_pet.play()

print(f"{my_pet.name} is sleeping...")
my_pet.sleep()

my_pet.train("roll over")
my_pet.train("play dead")

my_pet.get_status()
