def transform(string):
    result = ""
    for i in range(1, len(string)):
        if string[i] == "#":
            result += string[i - 1].lower()
        else:
            result += string[i - 1]
    if string[-1] != "#":
        result += string[-1]
    return result.replace("#", "")
            
    
def solution(m, musicinfos):
    
    result = "(None)"
    resultTime = 0
    
    m = transform(m)
    length = len(m)
    print(m)
    
    for musicinfo in musicinfos:
        start, end, title, info = musicinfo.split(",")
        sHour, sMinute = list(map(int, start.split(":")))
        eHour, eMinute = list(map(int, end.split(":")))   
        time = (eHour - sHour) * 60 + eMinute - sMinute
        
        info = transform(info)
        infos = info * (time // len(info) + 1)
        infos = infos[:time]
        print(infos)
        if m in infos and time > resultTime:
            result = title
            resultTime = time

    return result