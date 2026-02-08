def findSubarray(self, arr):
        prefix_sum = 0
        count = 0

        freq = {}
        freq[0] = 1   # Important

        for num in arr:

            prefix_sum += num

            if prefix_sum in freq:
                count += freq[prefix_sum]
                freq[prefix_sum] += 1
            else:
                freq[prefix_sum] = 1

        return count