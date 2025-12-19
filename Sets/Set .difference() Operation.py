n = int(input())
A = set(map(int, input().split()))

m = int(input())
B = set(map(int, input().split()))

difference_set = A.difference(B)

print(len(difference_set))
