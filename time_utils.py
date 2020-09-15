def millis(t1, t2):
    micros_diff = (t2 - t1).microseconds
    delta = micros_diff // 1000
    print("millis: ", delta)
    return delta


def micros(t1, t2):
    delta = (t2 - t1).microseconds
    print("micros: ", delta)
    return delta
