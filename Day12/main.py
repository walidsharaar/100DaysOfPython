
# scope

count = 1

def increase_count():

    count=2
    print(count)

increase_count()
print(count)

# there is no block scope
game_level = 3
enemies = ["Skeleton","Zombie","Alien"]
if game_level<5:
    new_enemy = enemies[0]
#within function it has local scope
print(new_enemy)
