def bmi_app():
    height = input('How tall are you?')
    weight = input('How much do you weight')
    bmi_value = int(weight)/(int(height)/100)**2
    print('Your BMI value is {}'.format(round(int(bmi_value),2)))
    if bmi_value < 18.5:
        print('You\'d better than eat more!')
    elif bmi_value >=18.5 and bmi_value <= 24:
        print('Good Job!')
    else:
        print('You\'d better do some exercises')