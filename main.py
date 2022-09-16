#YOUR CODE MUST INCLUDE:
#User Input
#Variables
#Change of Data Types
#Print Statements

#Test - 35%
#Large Project - 15%
#Small Project - 15%
#Classwork - 30%
#Participation - 5%

#So we start off by asking the user how many points he received on his tests.
print('Enter your score of first test (0-100):')
test1 = int(input())
print('Enter your score of second test (0-100):')
test2 = int(input())
average1 = (test1 + test2) / 2
#We then save the input in test 1 and 2, the input is also changed inot an integer and the average calculation is written. and we continue to do this for the rest of the subjects.
print('Enter your score of first large project (0-100):')
LP = int(input())
print('Enter your score of first small project (0-100):')
SP1 = int(input())
print('Enter your score of second small project (0-100):')
SP2 = int(input())
average2 = (SP1 + SP2) / 2
print('Enter your score of first class work (0-100):')
CW1 = int(input())
print('Enter your score of second class work (0-100):')
CW2 = int(input())
print('Enter your score of third class work (0-100):')
CW3 = int(input())
print('Enter your score of fourth class work (0-100):')
CW4 = int(input())
average3 = (CW1 + CW2 + CW3 + CW4) / 4
print('Enter your score of first participation (0-100):')
Par1 = int(input())
print('Enter your score of second participation (0-100):')
Par2 = int(input())
print('Enter your score of third participation (0-100):')
Par3 = int(input())
average4 = (Par1 + Par2 ) / 2
#Now we print the average (the variables turned on strings) with a formal answer.
print('Your average on tests is ' + str(average1) + '%.')
print()
print('Your average on large project is ' + str(LP) + '%.')
print()
print('Your average on small projects is ' + str(average2) + '%.')
print()
print('Your average on classwork is ' + str(average3) + '%.')
print()
print('Your average on participation is ' + str(average4) + '%.')
print()
#For this one I did differently, because each assingment have a different weight of each other, I took the variables that already exist and divided by 100, so I could get the 1%. with the 1%, I can multiplay by the real weight of that assingment.
averageF = (((average1 / 100) * 35)  + ((average2 / 100) * 15) + ((average3 / 100) * 30)  + ((average4 / 100) * 5) + ((LP / 100) * 15))
print('Your average on quarter is ' + str(averageF) + '%.')