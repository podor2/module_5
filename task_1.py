def caching_fibonacci():
    cache = {0: 0, 1: 1}  #terms of fibonacci progression No 0 and 1 already included in cache dictionary for code cleanliness

    def fibonacci(n):
        if n < 0 :
            return 'Value is nod valid. Number should be positive'
        elif n not in cache.keys():
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n] 
    return fibonacci

