
__version__ = "0.1.0"

def compute_stats(numbers):
    n = len(numbers)
    if n == 0:
        return 0, None, None
    mean = sum(numbers)/n
    var = sum((x-mean)**2 for x in numbers)/n
    std = var**0.5
    return n, mean, std

if __name__ == '__main__':
    print('v', __version__, compute_stats([1,2,3,4,5]))
