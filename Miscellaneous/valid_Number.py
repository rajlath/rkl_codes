class Valid_Number(object):
    '''
    a class to verify if a number is a valid number
    '''
    def __init__(self):
        self.valid_chars = list(map(str,range(0, 10)))

    def is_valid_number(self, number):
        '''
        get a string
        return whether its Integer, Float , complex or not a number
        '''
        if self.is_integer(number, signed=True):
            return ("Integer")
        elif self.is_float(number):
            return ("Float")
        elif self.is_complex(number):
            return ("Complex")
        else:return("")

    def is_integer(self, nums, signed=True):
        if signed:
            if nums[0] in ["+", "-"]:
                nums = nums[1:]
        if all(x in self.valid_chars for x in nums):
            return True
        else:
            return False

    def is_float(self,nums):
        dots = nums.count(".")
        if dots != 1:return False
        ints, deci = [str(x) for x in nums.split(".")]
        if not self.is_integer(ints, True):return False
        if not self.is_integer(deci, False):return False
        return True

    def is_complex(self,nums):
        es = nums.count("e")
        if es != 1: return False
        ints, deci = [str(x) for x in nums.split("e")]
        if ints.count("."):
            if self.is_float(ints)==False:return False
        else:
            if self.is_integer(ints, True)==False:return False
        if not self.is_integer(deci, False):return False
        return True




v = "-10.."
res= Valid_Number().is_valid_number(v)
if res == '':
    print("{} is Not a valid number".format(v))
else:
    print("{} is a Valid {} number".format(v, res))

