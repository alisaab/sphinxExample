class Mult:
    """
    Multiply by a constant
    """
    def __int__(self, cnst):
        self.constant = cnst

    def mult_one_num(self, a):
        """
        Multiply by a number

        :param a: the number to multiply by
        :type a: float
        :return: (float) mult result
        """
        return a * self.constant

    def mult_two_nums(self, a, b):
        """
        Multiply by two numbers
        
        :param a: the first number to multiply by
        :type a: float
        :param b: the second number to multiply by
        :type b: float
        :return: (float) mult result
        """
        return a * b * self.constant
