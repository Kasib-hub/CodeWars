
import math

def find_next_square(sq):
    if math.sqrt(sq) == round(math.sqrt(sq)):
        square = (math.sqrt(sq) + 1) ** 2
        return round(square)
    else:
        return -1
    # Return the next square if sq is a square, -1 otherwise

print(find_next_square(114))

