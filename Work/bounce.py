# bounce.py
#
# Exercise 1.5

drop_height = 100
bounce_factor = (3/5)
bounce = 0
bounce_height = drop_height

while bounce < 10:
    bounce_height = bounce_height * bounce_factor
    bounce = bounce + 1
    print(bounce, round(bounce_height, 4))


