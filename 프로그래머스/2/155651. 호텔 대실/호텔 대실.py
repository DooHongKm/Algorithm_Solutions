def solution(book_time):
    
    book_time.sort(key=lambda x: x[1])
    end_time = list(map(int, book_time[-1][1].split(":")))
    end_time = end_time[0] * 60 + end_time[1] + 10
    
    book_time.sort()
    start_time = list(map(int, book_time[0][0].split(":")))
    start_time = start_time[0] * 60 + start_time[1] 

    book_times = {i: 0 for i in range(start_time, end_time + 1)}
    for time in book_time:
        start, end = time
        start = list(map(int, start.split(":")))
        start = start[0] * 60 + start[1]
        end = list(map(int, end.split(":")))
        end = end[0] * 60 + end[1]
        for i in range(start, end + 10):
            book_times[i] += 1

    return max(book_times.values())
                