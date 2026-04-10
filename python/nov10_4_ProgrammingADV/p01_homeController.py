

from p01_companyDAO import companyDAO
from p01_consoleScreen import ConsoleScreen


if __name__ == "__main__":
    c = ConsoleScreen.getCompanyInfo()
    companyDAO.reg(c)
    ConsoleScreen.printResult(c)