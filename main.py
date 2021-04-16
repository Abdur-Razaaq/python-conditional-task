# The program should ask the driver to give their current speed in km/h and the average allowed speed of the road.
# If the speed is less than 60, it should print “OK”.
# For every 5km/h the driver drives above the speed limit, he should get 1 demerit.
# If the driver gets more than 12 demerit points, the function should print “Time to go to jail!”


current_speed = float(input("Enter your current speed: "))
average_allowed_speed = float(input("Enter the average allowed speed: "))

# To use method 1 close off method 2 with multiline comment tags

"""
# Method 1

if current_speed >= average_allowed_speed + 65:
    print("You have received more than 12 demerits. Time to go to jail!")

elif current_speed >= average_allowed_speed + 60:
    print("You have received 12 demerits.")

elif current_speed >= average_allowed_speed + 55:
    print("You have received 11 demerits")

elif current_speed >= average_allowed_speed + 50:
    print("You have received 10 demerits")

elif current_speed >= average_allowed_speed + 45:
    print("You have received 9 demerits")

elif current_speed >= average_allowed_speed + 40:
    print("You have received 8 demerits")

elif current_speed >= average_allowed_speed + 35:
    print("You have received 7 demerits")

elif current_speed >= average_allowed_speed + 30:
    print("You have received 6 demerits")

elif current_speed >= average_allowed_speed + 25:
    print("You have received 5 demerits")

elif current_speed >= average_allowed_speed + 20:
    print("You have received 4 demerits")

elif current_speed >= average_allowed_speed + 15:
    print("You have received 3 demerits")

elif current_speed >= average_allowed_speed + 10:
    print("You have received 2 demerits")

elif current_speed >= average_allowed_speed + 5:
    print("You have received 1 demerit")

elif current_speed >= average_allowed_speed:
    print("You have not received demerits")

else:
    print("OK!")
"""


# To use method 2 close off method 1 with multiline comment tags



# Method 2

demerit = (current_speed - average_allowed_speed) // 5


if current_speed >= average_allowed_speed:
    print("Demerit Point(s): " + str(int(demerit)))
    if demerit > 12:
        print("Time to go to jail!")

else:
    print("OK!")

# Built two methods. Method 1 is longer but it was the idea that came two me first.
# Method 2 took a bit to figure out as an equation was not something I thought of.
# Method 2 is much shorter but was slightly more trickier for me to build.
