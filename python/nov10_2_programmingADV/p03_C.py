# Controller
#   상황 판단해서, M이 필요하면 M소환, V가 필요하면 V소환
#   프로그램 전체의 진입점
#   PL급 back-end개발자
from p03_M import Calculator
from p03_V import ConsoleScreen


if __name__ == "__main__":
    x, y = ConsoleScreen.getXY()
    z = Calculator.getHab(x, y)
    ConsoleScreen.printResult(z)