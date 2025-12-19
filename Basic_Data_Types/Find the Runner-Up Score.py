n = int(input())
arr = map(int, input().split())

arr = list(set(arr))
arr.remove(max(arr))
runner_up = max(arr)
print(runner_up)
