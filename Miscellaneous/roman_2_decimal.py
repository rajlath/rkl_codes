def decimal_to_roman(n):
    '''
    convert a decima number to roman format
    param s : string - roman number
    rets  r : a decimal number
    '''
    digits = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    romans = ['M','CM','D','CD','C','CX','L','XL','X','IX','V','IV','I' ]
    rets   = ''
    while n:
        for i in range(len(digits)):
            while n >= digits[i]:
                rets += romans[i]
                n -= digits[i]

    return rets


print(decimal_to_roman(521))
