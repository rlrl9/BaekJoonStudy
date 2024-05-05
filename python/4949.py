while True:
    st = input()
    stack=[]
    if st =='.':
        break
    else:
        for s in st:
            if s=='.':
                if len(stack)==0:
                    print('yes')
                else:
                    print('no')
                break
            elif s =='(' or s =='[':
                stack.append(s)
            elif s ==')':
                if len(stack)!=0 and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(s)
            elif s ==']':
                if len(stack)!=0 and stack[-1]=='[':
                    stack.pop()
                else:
                    stack.append(s)