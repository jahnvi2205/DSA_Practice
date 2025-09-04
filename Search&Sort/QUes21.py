T = int(input())
for _ in range(T):
    N, Q = map(int, input().split())
    ranges = []
    for _ in range(N):
        A, B = map(int, input().split())
        ranges.append((A, B))

    ranges.sort()

    merged = []
    for A, B in ranges:
        if not merged or merged[-1][1] < A - 1:
            merged.append([A, B])
        else:
            merged[-1][1] = max(merged[-1][1], B)

    for _ in range(Q):
        K = int(input())
        ans = -1
        for A, B in merged:
            length = B - A + 1
            if K <= length:        
                ans = A + K - 1
                break
            K -= length            
        print(ans)
