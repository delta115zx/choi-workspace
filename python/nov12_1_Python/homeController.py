from consoleScreen import ConsoleScreen
from player.playerDAO import PlayerDAO
from team.teamDAO import TeamDAO


if __name__ == "__main__":
    teamDAO = TeamDAO()
    playerDAO = PlayerDAO()
    
    while True:
        menu = ConsoleScreen.showMainMenu()

        if menu == "10":
            break
        elif menu == "1":
            team = ConsoleScreen.showRegTeamMenu()
            result = teamDAO.reg(team)
            ConsoleScreen.showResult(result)
        elif menu == "2":
            player = ConsoleScreen.showRegPlayerMenu()
            result = playerDAO.reg(player)
            ConsoleScreen.showResult(result)
        elif menu == "3":
            teams = teamDAO.getAll()
            ConsoleScreen.showTeams(teams)
        elif menu == "4":
            players = playerDAO.getAll()
            ConsoleScreen.showPlayers(players)
        elif menu == "5":
            pageCount = teamDAO.getPageCount("")
            pageNo = ConsoleScreen.showSelectPageNoMenu(pageCount)
            teams = teamDAO.get(pageNo, "")
            ConsoleScreen.showTeams(teams)
        elif menu == "6":
            pageCount = playerDAO.getPageCount("")
            pageNo = ConsoleScreen.showSelectPageNoMenu(pageCount)
            players = playerDAO.get(pageNo, "")
            ConsoleScreen.showPlayers(players)
        elif menu == "7":
            searchTxt = ConsoleScreen.showSearchMenu()
            pageCount = teamDAO.getPageCount(searchTxt)
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageNoMenu(pageCount)
            teams = teamDAO.get(pageNo, searchTxt)
            ConsoleScreen.showTeams(teams)
        elif menu == "8":
            searchTxt = ConsoleScreen.showSearchMenu()
            pageCount = playerDAO.getPlayerCount(searchTxt)
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageNoMenu(pageCount)
            players = playerDAO.get(pageNo, searchTxt)
            ConsoleScreen.showPlayers(players)
        elif menu == "9":
            searchTxt = ConsoleScreen.showSearchMenu()
            pageCount = playerDAO.getPlayerCount(searchTxt)
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageNoMenu(pageCount)
            players = playerDAO.get2(pageNo, searchTxt)
            ConsoleScreen.showPlayers2(players)
        elif menu == "11":
            players = playerDAO.getMaxSalary()
            ConsoleScreen.showPlayers2(players)
        elif menu == "12":
            name, what, info = ConsoleScreen.showUpateTeamMenu()
            result = teamDAO.update(name, what, info)
            ConsoleScreen.showResult(result)
        elif menu == "13":
            name, what, info = ConsoleScreen.showUpdatePlayerMenu()
            result = playerDAO.update(name, what, info)
            ConsoleScreen.showResult(result)
        elif menu == "14":
            name = ConsoleScreen.showDeleteTeamMenu()
            result = teamDAO.delete(name)
            ConsoleScreen.showResult(result)
        elif menu == "15":
            name = ConsoleScreen.showDeletePlayerMenu()
            result = playerDAO.delete(name)
            ConsoleScreen.showResult(result)



