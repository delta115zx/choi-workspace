# 외부파일에 있는거 불러오려면 import 필수
# 1)
# import animal.pet # import 패키지명.모듈명
# d = animal.pet.Dog("후추") # 패키지명.모듈명.클래스명...
# d.bark()
# d.printInfo()

# 2)
# import animal.pet as ap # import 패키지명.모듈명 as 별칭
# d = ap.Dog("후추")      # 별칭.클래스명...
# d.bark()
# d.printInfo()

# 3)
from animal.pet import Dog # from 패키지명.모듈명 import 가져올거
d = Dog("후추")            # 클래스명...
d.bark()
d.printInfo()

# 주로 3번 스타일 쓰겠지만 -> 1/2활용해야

# Windows에서 PYTHONPATH를 설정하면 프로젝트도 패키지처럼 인식해서...
# 1) 실제 Linux서버에서 실행 (on-premises)
# 2) MS에서 빌려온 Linux서버에서 실행(cloud(azure))