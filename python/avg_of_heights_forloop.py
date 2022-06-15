
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
x=student_heights
total_heights=0
for k in x:
  total_heights=total_heights+k
print("total heights = " ,total_heights)
avg=total_heights/k
print("avg of heights is = ",avg)