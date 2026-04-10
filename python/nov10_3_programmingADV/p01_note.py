# 프로젝트가 커지면
#   C/M/V가 여러개 -> C도 많아짐
#   프로그램의 진입점 역할하는 첫C 이름을
#       homeController or mainController
######################
# p02_doctor.py : M - 계산(DAO)
# p02_guest.py : M - 데이터 표현용(DTO)
########################
# DAO/DTO패턴 : MVC패턴인데, DB작업
#   MVC패턴
#       DAO(Data Access Object) : DB관련 작업하는 M
#       DTO(Data Transfer/Temp Object) : 데이터를 묶어다니는 M
#           DTO, VO(Value Object), Bean

# AOP적인 생각 : 어떤 DB작업을 하든지 공통된 부분이 존재
#               -> 따로 정리 해야겠다
# 그 정리하는거는 이번 프로젝트 뿐만 아니라, 앞으로 계속 사용될 듯
# => DB관련 라이브러리를 만들어야겠다