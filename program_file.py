# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 23:37:28 2018

@author: SAYON
"""

import pandas as pd
df = pd.read_csv('dataset.csv')

def average_salary(A1,A2):
    sum_salary,count = 0,0
    for i in range(0,df.shape[0]):
        age = int(df['Age'][i])
        salary = float(df['Salary'][i])
        if(age>=A1 and age<A2):
            sum_salary += salary
            count +=1
    if(sum_salary!=0):   
        return (sum_salary/count)
    else:
        return 0
    
def maximum_avg_salary():
    multiple_of5 = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    avg_h,hA1,hA2 = 0,0,0
    min_age = min(df['Age']) // 5
    max_age = max(df['Age']) // 5
    for i in range(min_age,max_age+2):
        A1,A2 = multiple_of5[i-1],multiple_of5[i]
        avg_salary = average_salary(A1,A2)
        if avg_salary!=0 :
            print("Average Salary between",A1," and ",A2,"is",avg_salary)
            if(avg_salary>avg_h):
                avg_h = avg_salary
                hA1 = A1
                hA2 = A2
    print("\nMaximum Average Salary is :",avg_h," Range between ",hA1," and ",hA2)
    
    
def main():
    print("Enter Range to compute Average");
    try:
        min_age = min(df['Age'])
        max_age = max(df['Age'])
        print("Minimum Age: ",min_age," Maximum Age: ",max_age)
        A1 = int(input("Enter Starting Age Number: "));
        A2 = int(input("Enter Ending Age Number: "));
        if A1<min_age or A2>max_age or A1>A2:
            print("Range is not correct.")
        else:
            print("\nAverage Salary between ",A1," and ",A2," is ",average_salary(A1,A2+1))
    except:
        print("Wrong Fromat of Input. Only Integers.\n")
    
    
    
if __name__== "__main__":
  while(True):
      print("\n1. Average Salary between Age A1 and A2\n")
      print("2. Maximum Average Salary\n")
      print("3. Exit\n")
      ch = (input("Enter Choice : "))
      if(ch=='1'):
          main()
      elif(ch=='2'):
          maximum_avg_salary()
      elif(ch=='3'):
          break
      else:
          print("Wrong Choice. Try Again ")
 
  
    
