# 노트북에서 작업중인 Python프로그램
# OracleDB서버
########################################
# 컴퓨터 통신
#   Socket 카톡 : 실시간
#   HTTP : 안실시간
#   ...
##########################################
# Python - DB서버
#   안실시간이지만, HTTP통신은 아니고
#   그냥 별개의 통신
#   DB메이커 다양 다양한 메이커들간의 표준화된 통신방식같은게 없음
#   -> DB메이커별로 통신방식 다 다름
#   -> Python입장에서 그 통신방식을 다 챙겨? 불가능
#   -> Python - DB서버 연결기능은 없음 -> 진짜 만들어야
##################
# Python이 오피셜하게 만들어준건x
# 누군가 Python - OracleDB연결 기능을 만들었겠지
# -> 각 DB메이커에서 만들어준게 있음
#######################
# cx_Oracle.py(구버전) : cx_Oracle.py + instantclient
# oracledb.py : instantclient가 따로 없어도 되는데
#       포함된 ic가 oracleDB구버전 지원x
#       구버전 OracleDB랑 연결하려면 따로 instantclient있어야
#######################
# pip : 개발자들간의 공유문화를 중앙제어시스템
# 시작 - cmd
#   pip install 이름 -> 다운받아와서 사용가능하게 세팅까지 완료
#####################
# pip install oracledb

from oracledb import connect

# 구버전 OracleDB쓰고 있다면
# init_oracle_client(lib_dir="instantclient폴더경로")

# sqlplus써서 연결할때 주소쓰는 형식(아이디/비번@서버주소:포트/SID)
con = connect("delta115/cjy0115@195.168.9.10:1521/xe")

print(con)

con.close()