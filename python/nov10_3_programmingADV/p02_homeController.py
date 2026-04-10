
from p02_doctor import Doctor
from p02_consoleScreen import ConsoleScreen


if __name__ == "__main__":
    g = ConsoleScreen.getGuestInfo()
    Doctor.calculate(g)
    ConsoleScreen.printResult(g)