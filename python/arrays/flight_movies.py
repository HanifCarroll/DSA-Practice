'''
Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length. 
'''

def solve(flight_length, movie_lengths):
    movies = set()
    for length in movie_lengths:
        target = flight_length - length
        if target in movies:
            return True
        else:
            movies.add(length)
    return False

flight_length = 130
movie_lengths = [30, 45, 90, 120, 50, 75, 80, 60, 140]
print(solve(flight_length, movie_lengths))

def level_order(root):
    if not root:
        return
    q = []
    q.append(root)
    while q:
        current = q.pop(0)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
        print(current)