#Student Performance analysis by using pandas & statistics module in python
import pandas as pd
import statistics as st
print(".........Sample Dataset..........")
dict = {
    "student_name" :["ben","john","gauri"],
    "subjects" : ["maths","physics","chemistry"],
    "marks" :["90,90,99","91,89,91","88,95,88"]
}
print(pd.DataFrame(dict))
print("!!Statistically Analyzing Each Student Performance!!")
class student():
    def __init__(self,student_name,maths,phy,chem):
        self.student_name = student_name
        self.maths = maths
        self.phy = phy
        self.chem = chem
    def show1(self):
        self.mean =round((self.maths+self.phy+self.chem)/3,2)
        print("Mean :",self.mean)
        self.median = st.median([self.maths,self.phy,self.chem])
        print("Median :",self.median)
        self.mode = st.mode([self.maths,self.phy,self.chem])
        print("Mode :",self.mode)
        self.variance = round(st.variance([self.maths,self.phy,self.chem]),2)
        print("Variance :",self.variance)
        self.standard_deviation = round(st.stdev([self.maths,self.phy,self.chem]),2)
        print("Standard_deviation :",self.standard_deviation)
    def show2(self):
        if a1.mean>a2.mean and a1.mean>a3.mean:
            print(a1.student_name,"is the top performance based on his average marks")
        elif a2.mean>a3.mean:
            print(a2.student_name,"is the top performance based on his average marks")  
        else:
            print(a3.student_name,"is the top performer based on his average marks")        
a1 = student("ben",90,90,99)
print("**********************************************************")  
print("Student Name :",a1.student_name)
print("Secured Marks in Each Subjects are....\n","maths :",a1.maths,"\n","phy :",a1.phy,"\n","chem :",a1.chem)
a1.show1()
a2 = student("john",91,89,91)
print("**********************************************************")  
print("Student Name :",a2.student_name)
print("Secured Marks in Each Subjects are....\n","maths :",a2.maths,"\n","phy :",a2.phy,"\n","chem :",a2.chem)
a2.show1()
a3= student("gauri",88,95,88)
print("**********************************************************")  
print("Student Name :",a3.student_name)
print("Secured Marks in Each Subjects are....\n","maths :",a3.maths,"\n","phy :",a3.phy,"\n","chem :",a3.chem)
a3.show1()
#displaying the condition
a1.show2()

