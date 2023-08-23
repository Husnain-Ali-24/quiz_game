condition=True
while condition==True:
 print("Wellcome to the Quiz ")
 print("In which language do you want to take the test? \na) Python\nb) c++")
 choice1=input()
 if choice1=="a":
  print("Total Questions:10\nTotal Marks:100")
  score=0
  a=0
  while a<10:
   List=["1. Who developed Python Programming Language?\na) Wick van Rossum\nb) Rasmus Lerdorf\nc) Guido van Rossum\nd) Niene Stom","2. Which type of Programming does Python support?\na) object-oriented programming\nb) structured programming\nc) functional programming\nd) all of the mentioned",
   "3. Is Python case sensitive when dealing with identifiers?\na) no\nb) yes\nc) machine dependent\nd) none of the mentioned","4. Which of the following is the correct extension of the Python file?\na) .python\nb) .pl\nc) .py\nd) .p",
   "5. Is Python code compiled or interpreted?\na) Python code is both compiled and interpreted\nb) Python code is neither compiled nor interpreted\nc) Python code is only compiled\nd) Python code is only interpreted","6. All keywords in Python are in _________\na) Capitalized\nb) lower case\nc) UPPER CASE\nd) None of the mentioned",
   "7. Which of the following is used to define a block of code in Python language?\na) Indentation\nb) Key\nc) Brackets\nd) All of the mentioned","8. Which keyword is used for function in Python language?\na) Function\nb) def\nc) Fun\nd) Define","9. Which of the following character is used to give single-line comments in Python?\na) //\nb) #\nc) !\nd) /*",
   "10. Python supports the creation of anonymous functions at runtime, using a construct called __________\na) pi\nb) anonymous\nc) lambda\nd) none of the mentioned"]
   print(List[a])
   Correct_options=[{"c":"Guido van Rossum"},{"d":"all of the mentioned"},{"b":"yes"},{"c":".py"},{"a":"Python code is both compiled and interpreted"},{"d":" None of the mentioned"},{"a":"Indentation"},{"b":"def"},{"b":"#"},{"c":"lambda"}]
   Input=input()
   if Input in Correct_options[a].keys():
    print("Correct")
    score+=10
   else:
    print("Uncorrect")
    print('Correct Option is:')
    correct=Correct_options[a].values()
    for i in correct:
     print(i)
   a+=1
  print(f"Final Score :{score}")
 elif choice1=="b":
  print("Total Questions:10\nTotal Marks:100")
  score=0
  a=0
  while a<10:
   List=["1. Who invented C++?\na) Dennis Ritchie\nb) Ken Thompson\nc) Brian Kernighan\nd) Bjarne Stroustrup","2. What is C++?\na) C++ is an object oriented programming language\nb) C++ is a procedural programming language\nc) C++ supports both procedural and object oriented programming language\nd) C++ is a functional programming language",
   "3. Which of the following is the correct syntax of including a user defined header files in C++?\a) #include [userdefined]\nb) #include “userdefined”\nc) #include <userdefined.h>\nd) #include <userdefined>","4. Which of the following is used for comments in C++?\na) /* comment */\nb) // comment */\nc) // comment\nd) both // comment or /* comment */",
   "5. Which of the following user-defined header file extension used in c++?\na) hg\nb) cpp\nc) h\nd) hf","6. Which of the following is a correct identifier in C++?\na) VAR_1234\nb) $var_name\nc) 7VARNAME\nd) 7var_name","7. Which of the following is not a type of Constructor in C++?\na) Default constructor\nb) Parameterized constructor\nc) Copy constructor\nd) Friend constructor",
   "8. Which of the following approach is used by C++?\na) Left-right\nb) Right-left\nc) Bottom-up\nd) Top-down","9. Which of the following is used to terminate the function declaration in C++?\na) ;\nb) ]\nc) )\nd) :","10. Which keyword is used to define the macros in c++?\na) #macro\nb) #define\nc) macro\nd) define"]
   print(List[a])
   Correct_options=[{"d":"Bjarne Stroustrup"},{"c":"C++ supports both procedural and object oriented programming language"},{"b":"#include “userdefined”"},{"d":"both // comment or /* comment */"},{"c":"h"},{"a":"VAR_1234"},{"d":"Friend constructor"},{"c":"Bottom-up"},{"a":";"},{"b":"#define"}]
   Input=input()
   if Input in Correct_options[a].keys():
    print("Correct")
    score+=10
   else:
    print("Uncorrect")
    print('Correct Option is:')
    correct=Correct_options[a].values()
    for i in correct:
     print(i)
   a+=1
  print(f"Final Score :{score}")
 check=input("Do you want to play again? 'yes' or 'no' ")
 if check=="no":
  condition=False
 elif check=="yes":
  condition=True