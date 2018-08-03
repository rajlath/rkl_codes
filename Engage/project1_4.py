def calculate_leibniz_pi():
    '''
    The German mathematician Gottfried Leibniz developed the following method
    to approximate the value of π:
    π/4 = 1 – 1/3 + 1/5 – 1/7 + …
    Write a program that allows the user to specify the number of iterations used in
    this approximation and displays the resulting value.
    '''
    ans  = 1
    odd  = True
    deno = 1
    nos_of_iteration = int(input("Enter number of iteration :"))
    iteration_done = 1
    while iteration_done < nos_of_iteration:
        deno += 2
        if odd :
            ans -= 1/deno
            odd = False
        else:
            ans += 1/deno
            odd = True
        iteration_done += 1
    print("After {} iteration value will be {} and pi value {} :".format(nos_of_iteration,ans, ans * 4))

if __name__ == "__main__"    :
    calculate_leibniz_pi()

