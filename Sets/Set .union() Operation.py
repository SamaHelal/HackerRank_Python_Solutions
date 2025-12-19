n = int(input())
A = set(map(int, input().split()))

m = int(input())
B = set(map(int, input().split()))

union_set = A.union(B)

print(len(union_set))
