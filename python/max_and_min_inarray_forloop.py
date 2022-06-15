student_scores=input("enter student scores : ").split()
for n in range(0,len(student_scores)):
 student_scores[n]=int(student_scores[n])
x= student_scores
print(x)
high =0
for marks in x:
  #highest  marks:
  if high<marks:
     high=marks
print("high mark is :",high)
low=marks
for marks in x:
  #lowest mark
  if low>marks:
    low=marks
print("lowest mark is :",low)