# write a program which will mark a spot with an X.
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
i=int(position[0])-1
j=int(position[1])-1
map[j][i]="x"
print(f"{row1}\n{row2}\n{row3}")