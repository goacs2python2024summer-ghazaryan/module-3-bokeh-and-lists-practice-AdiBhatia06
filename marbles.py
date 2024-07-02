import random

def marble_game(times):
     marbles = ['blue', 'blue', 'blue', 'red', 'red', 'black']
     results= []
     total= 0

     for _ in range(times):
        first_marble = random.choice(marbles)
        marbles.remove(first_marble)
        second_marble = random.choice(marbles)
        marbles.append(first_marble)
        if first_marble==second_marble:
            total += 1
        else:
            total -= 1
        
        results.append(total)

     return results
print(marble_game(5))