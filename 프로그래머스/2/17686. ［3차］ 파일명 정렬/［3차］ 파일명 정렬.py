def translate(name):
    
    numberIdx = 0
    tailIdx = 0
    
    for i, c in enumerate(name):
        if c.isdigit() and numberIdx == 0:
            numberIdx = i
            continue
        if not c.isdigit() and numberIdx != 0 and tailIdx == 0:
            tailIdx = i
            continue
            
    if tailIdx > numberIdx + 5:
        tailIdx = numberIdx + 5
    elif tailIdx == 0:
        tailIdx = len(name)
    
    a = name[:numberIdx]
    b = name[numberIdx:tailIdx]
    c = ""
    if tailIdx == len(name):
        c = ""
    else:
        c = name[tailIdx:]
    
    return (a, b, c)


def solution(files):
    
    newFiles = [translate(file) for file in files]
    newFiles.sort(key=lambda x: (x[0].lower(), int(x[1])))
    
    result = []
    for newFile in newFiles:
        result.append("".join(newFile))
        
    return result
            