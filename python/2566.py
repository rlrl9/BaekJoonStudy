table = [list(map(int, input().split())) for _ in range(9)]
max_value=0
max_col=0
max_row=0
for i in range(9):
    for j in range(9):
        if max_value<=table[i][j]:
            max_value=table[i][j]
            max_col=i+1
            max_row=j+1
print(max_value)
print(max_col,max_row)