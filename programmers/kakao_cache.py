def solution(cacheSize, cities):
    time = 0
    cache = []

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        lower = city.lower()
        if lower in cache:
            time += 1
            cache.remove(lower)
            cache.append(lower)
        else:
            time += 5
            if len(cache) < cacheSize:
                cache.append(lower)
            else:
                cache.pop(0)
                cache.append(lower)
    return time


"""
 ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
    5        5        5          5       5       5       5        5          5        5   

 ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
     5        5        5       1       1          1       1        1          1  
  ["Jeju", "Jeju", "Jeju", "Seoul", "Seoul", "Seoul", "Pangyo", "Pangyo", "Pangyo"]
       5      1       1       5       1         1       5        1          1  
"""