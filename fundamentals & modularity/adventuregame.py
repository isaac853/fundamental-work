
health = 100

def takeDamage(amount: int):
   global health
   health -= amount

   if health < 0:
      health = 0

def takePotion(newhealth, type: str):

    if type == "full":
       newhealth += 100

    if type == "medium":
        newhealth += 50
    if type == "lesser":
       newhealth += 20

    if newhealth > 100:
       newhealth = 100

    return newhealth

takeDamage(20)
print(health)

health = takePotion(health, "full")
print(health)