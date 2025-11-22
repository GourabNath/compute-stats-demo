
__version__ = "0.2.0"

def compute_stats(numbers):
    n = len(numbers)
    if n == 0:
        return 0, None, None, None

    nums = sorted(numbers)
    mean = sum(nums)/n
    var = sum((x-mean)**2 for x in nums)/n
    std = var**0.5

    # Median
    mid = n // 2
    if n % 2 == 1:
        median = nums[mid]
    else:
        median = (nums[mid-1] + nums[mid]) / 2

    return n, mean, std, median

if __name__ == '__main__':
    sample = [1,2,3,4,5]
    print('v', __version__, compute_stats(sample))
