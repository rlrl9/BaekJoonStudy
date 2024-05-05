x,y,w,h=map(int,input().split())
l=[abs(x-w),abs(y-h),x,y]
print(min(l))