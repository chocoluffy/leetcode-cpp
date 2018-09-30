    [4, 5, 8], [3, 13], [7]
    [17, 16, 7]
    
    [17, 23] k = 2;
    
    [max(A), sum(A)]
    
    def find_min_max(A, k):
        def if_current_value(A, cap): # if current value (cap) can support a valid k partition.
            count_k = 0
            i = 0
            while i < len(A):
                if count_k > k:
                    return False
                curr_sum = 0
                while curr_sum <= cap and i < len(A):
                    curr_sum += A[i]
                    i += 1
                count_k += 1
            if count_k <= k:
                return True
            else:
                return False
            
        left = max(A)
        right = sum(A)
        while left < right:
            mid = left + (right - left) / 2
            if if_current_value(A, mid):
                # if current value cap can support, search the first half.
                right = mid
            else:
                # if cap cannot support, search the second half.
                left = mid + 1
        return right