from worker import Worker
from time import sleep

def main():
    john = Worker("John", "Walevsky", "123", 40)
    john.clockIn()
    sleep(10)
    john.clockOut()


if __name__ == "__main__":
    main()