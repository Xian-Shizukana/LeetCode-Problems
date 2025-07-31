def findPoisonedDuration(timeSeries:list[int], duration:int) -> int:
    count = 0

    for i in range(len(timeSeries)):
        if i == len(timeSeries) - 1:
            count += duration
            return count

        if timeSeries[i] + duration >= timeSeries[i+1]:
            count += timeSeries[i + 1] - timeSeries[i]
        else:
            count += duration

print(findPoisonedDuration([1,4], 2))

