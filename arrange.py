def arrangeMain(i, time, speed):
    string_time = str()
    # Arranging "i" variable 
    string_i = arrangei(i)
    # Arranging "speed" variable
    string_speed = arrangespeed(speed)
    # Arranging "time" variable
    string_time = arrangeTime(time)
    return string_i, string_time, string_speed

def arrangeTime(time):
    string_time = 0 
    if time < 10:
        string_time = f"  {time}"
    elif time < 100:
        string_time = f" {time}"
    elif time < 1000:
        string_time = f"{time}"
    return string_time

def arrangei(i):
    i += 1
    string_i = str()
    if i < 10:
        string_i = f"0{i}"
    else:
        string_i = f"{i}"
    return string_i

def arrangeWords(answers, words):
    answers2, words2 = [], []
    for i in words:
        missingspace = 16 - len(i)
        i += " "*missingspace
        words2.append(i)

    for i in answers:
        missingspace = 16 - len(i)
        i += " "*missingspace
        answers2.append(i)
    return words2, answers2

def arrangespeed(speed):
    string_speed = str()
    if speed < 10:
        string_speed = f"  {speed}"
    elif speed < 100:
        string_speed = f" {speed}"
    elif speed < 1000:
        string_speed = f"{speed}"
    return string_speed
