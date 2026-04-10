from player.player import Player
from team.team import Team


class ConsoleScreen:
    def showMainMenu():
        print("1) 팀등록")
        print("2) 선수등록")
        print("3) 전체팀 조회")
        print("4) 전체선수 조회")
        print("5) 팀 조회")
        print("6) 선수 조회")
        print("7) 팀 검색")
        print("8) 선수 검색")
        print("9) 선수 검색(팀정보포함)")
        print("10) 종료")
        print("11) 연봉제일 높은 선수")
        print("12) 팀 정보수정")
        print("13) 선수 정보수정")
        print("14) 팀 삭제")
        print("15) 선수 삭제")
        print("-----------")
        return input("뭐 : ")

    def showDeleteTeamMenu():
        return input("삭제할 팀 이름 : ")

    
    def showDeletePlayerMenu():
        return input("삭제할 선수 이름 : ")
    
    def showRegTeamMenu():
        name = input("팀 이름 : ")
        ceo = input("ceo 이름 : ")
        coach = input("감독 이름 : ")
        return Team(name, ceo, coach)
    
    def showRegPlayerMenu():
        name = input("선수 이름 : ")
        nickname = input("닉네임 : ")
        salary = input("연봉 : ")
        position = input("포지션 : ")
        t_name = input("팀 이름 : ")
        return Player(None, name, nickname, salary, position, t_name)
    
    def showResult(result):
        print(result)
        print("----------")

    def showTeams(teams):
        for team in teams:
            print(team.name)
            print(team.ceo)
            print(team.coach)
            print("---------")

    def showPlayers(players):
        for player in players:
            print(player.no)
            print(player.name)
            print(player.nickname)
            print(player.salary)
            print(player.position)
            print(player.t_name)
            print("----------")
    
    def showPlayers2(players):
        for player in players:
            print(player.no)
            print(player.name)
            print(player.nickname)
            print(player.salary)
            print(player.position)
            print(player.t_name)
            print(player.t_ceo)
            print(player.t_coach)
            print("--------")

    def showSearchMenu():
        return input("검색어 : ")

    def showSelectPageNoMenu(pageCount):
        return input("페이지(1 ~ %d) : " % pageCount)
    
    def showUpateTeamMenu():
        name = input("수정할 팀 이름 : ")
        print("--------")
        print("팀 이름, ceo, 감독")
        what = input("수정할 정보 : ")
        info = input("수정 내용 : ")
        return name, what, info
    
    def showUpdatePlayerMenu():
        name = input("수정할 선수 이름 : ")
        print("--------")
        print("닉네임, 연봉, 포지션")
        what = input("수정할 정보 : ")
        info = input("수정 내용 : ")
        return name, what, info
