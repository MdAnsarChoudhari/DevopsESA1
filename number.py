import pytest

def check_number(num):
    if num%2==0:
        even_odd="The Number is even "
    else:
        even_odd="The Number is odd "

    
    count=0
    for i in range(1, num+1):
        if num%i==0:
            count=count+1

    if count==2:
        prime="The number is prime"
    else:
        prime="The number is not prime"


    return even_odd, prime


if __name__=="__main__":

    print(check_number(7))