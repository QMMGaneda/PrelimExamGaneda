#Create a pytest to check the following:
#1. if the grade is passed (greater than or equal to 50) 
#2. if the conversion of the temperature from celcius to fahrenheit is correct
#3. if the area of the square is correct

def test_grade():
    num = 50 # you can modify this
    assert num >= 50

def test_temp():
    C = 100 # you can modify this
    F = (C*1.8) + 32
    assert F == 212

def test_area():
    l = 5 # you can modify this
    area = l*l

    assert area == 25