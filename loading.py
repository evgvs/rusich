from time import sleep 
def splash(count):
    for _i in range(count):
        print("\r|", end="")
        sleep(0.1)
        print("\r/", end="")
        sleep(0.1)
        print("\r-", end="")
        sleep(0.1)
        print("\r\\", end="")
        sleep(0.1)

    print("\r", end="")

def clearline():
    print("\r", end="")
    for _i in range(300):
        print(" ", end="")
    print("\r", end="")