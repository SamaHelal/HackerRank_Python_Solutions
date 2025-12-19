n = int(input())
A = set(map(int, input().split()))

m = int(input())
B = set(map(int, input().split()))

intersection_set = A.intersection(B)

print(len(intersection_set))
