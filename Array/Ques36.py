def medianOf2(self, a, b):
        # ensure a is the smaller array
        if len(a) > len(b):
            a, b = b, a

        n, m = len(a), len(b)
        low, high = 0, n

        while low <= high:
            i = (low + high) // 2
            j = (n + m + 1) // 2 - i

            leftA = a[i-1] if i > 0 else float('-inf')
            rightA = a[i] if i < n else float('inf')

            leftB = b[j-1] if j > 0 else float('-inf')
            rightB = b[j] if j < m else float('inf')

            if leftA <= rightB and leftB <= rightA:
                if (n + m) % 2 == 1:
                    return max(leftA, leftB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2

            elif leftA > rightB:
                high = i - 1
            else:
                low = i + 1

        