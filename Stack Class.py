# Stack class
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

sol_stack = Stack()
#input file
file = open("mazeinput.txt","r")
# program doesn't need size of maze
rows_columns=file.readline()
#rows and columns
starting_row,starting_col=file.readline().split(',')
ending_row,ending_col=file.readline().split(',')
#2d maze array
maze = []
for line in file.read().splitlines():
    maze.append(list(line))
#search for valid cells
def search(x,y):
    if maze[x][y]== '*':
        return False
    elif maze[x][y] == 1:
        return False
    elif (x,y) == (int(ending_row),int(ending_col)):
        sol_stack.push((x, y))
        return True

    maze[x][y]=1
    sol_stack.push((x, y))

    if x==len(maze) and search(x-1,y) or y==len(maze) and search(x,y-1) or 0<=x<len(maze) and search(x+1,y) or 0<=y<len(maze) and search(x,y+1):
        return True

search (int(starting_row),int(starting_col))
#adding and printing stack items
move = []
while sol_stack.isEmpty()!= True :
    last_item = sol_stack.pop()
    move.append(last_item)

for i in range(len(move)-1,-1,-1):
    print (move[i])
for line in maze :
    print(line)