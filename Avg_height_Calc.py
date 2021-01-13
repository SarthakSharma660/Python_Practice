# write a program that calculates the average student height from a List of heights.
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

av_height=0
sum_height=0
i=0

for h in student_heights:
  sum_height=sum_height+student_heights[i]
  i+=1
  


av_height=sum_height/i 
print(round(av_height)) 