
def calculate_distance():
    '''
    Write a program that lets the user enter the initial height of the
    ball and the number of times the ball is allowed to continue bouncing. Output
    should be the total distance traveled by the ball.
    '''
    initial_height = int(input("Enter initial height of the ball :"))
    nos_of_bounce  = int(input("Enter number of bounces :"))
    current_height = initial_height
    bounce_done = 0
    dist_travelled = 0
    while bounce_done < nos_of_bounce:
        dist_travelled += current_height
        current_height *= 0.6
        dist_travelled += current_height
        bounce_done += 1
    print("Total distance travelled if dropped from height {} and bounced {} times is : {}. ".format(initial_height, nos_of_bounce, dist_travelled))

if __name__ == "__main__" :
    calculate_distance()


