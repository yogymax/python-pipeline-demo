print('first line added by python developer...!')


def addition(num1,num2):
    if type(num1)==int and type(num2)==int:
        if num1<=0 or num2<=0:
            raise Exception("Invalid Params")
        else:
            result = num1 + num2
            return result
    else:
        raise Exception("Invalid Types...!")