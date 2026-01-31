#global variables



# import and input the neceassary variables
def get_user_info():
    weight=float(input('plaese inpout your weight (kg): '))
    height=float(input('plaese inpout your height (m): '))
    return weight,height
    

# calculation of bmi
def bmi_calculate(weight,height):
    bmi= weight // (height**2)
    return bmi


# describtion of situatation 
def bmi_result(bmi):
    print(f'your BMI is: {bmi}\nresult:')
    if bmi < 18.5:
        print ('Under Weight')
    elif 18.5 <= bmi < 25:
        print('Normal')
    elif 25 <= bmi < 30:
        print ('Over Weight')
    elif 30 <= bmi < 35:
        print('Obese')
    else:
        print('Extremely Obese ')
    

#main and final function
def main():
    weight,height= get_user_info()
    bmi=bmi_calculate(weight,height)
    bmi_result(bmi)
    
    
if __name__=="__main__":
    main()


