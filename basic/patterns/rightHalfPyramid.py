def right_half_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces followed by stars
        print(' ' * (n - i) + '*' * i)

# Example: Generate a right half pyramid of height 5
right_half_pyramid(5)
