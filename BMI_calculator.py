#BMI(BODY MASS INDEX) Calculator mini project using python
#it is used to calculate whether a person will have healthy body weight for their height
"""1 foot = 0.3048 meters
5.5 feet = 5.5 * 0.3048 = 1.6764 meters"""
#obese means person having fatty body
"""1meter=3.28084feet
1.75
meters
x
3.28084
=
5.74147
feet
≈
5.74
feet
1.75metersx3.28084=5.74147feet≈ 
5.74feet"""
#code starts from below
data = True
def BMI(weight,height):
    print("Weight :",weight)
    print("height :",height)
    data = weight/((height*0.3048)**2)
    print("BMI value :",data)
    if data <=18.0:
        print("You are categorized as : Under_weight")
    elif data >=18.0 and data <=25.9:
        print("You are categorized as :Normal_weight")
    elif data >25.9 and data <=30.0:
        print("You are categorized as :Over_weight")
    else:
        print("You are categorized as :obese")
print(BMI(68.0,5.0)) 

