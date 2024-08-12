def int_to_list (n):
    return list(map(int,str(n)))

def is_narcissistic (n):
    d = int_to_list(n)
    e = sum(map(lambda x : x**len(d),d))
    return e == n

print(*int_to_list (153), sep = ",")

inp_lst = ['Python', 'Java', 'Ruby', 'JavaScript']
size = len(inp_lst)
print(size)

print((is_narcissistic(153)))

n = 0
while n<10000000:
    if is_narcissistic(n):
        print (n)
    n = n+1
