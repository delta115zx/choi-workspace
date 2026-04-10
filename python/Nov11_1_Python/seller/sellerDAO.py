from math import ceil
from Choi.choiDBManager import ChoiDBManager
from seller.seller import Seller

# 메소드 첫번째 파라메터로 self를 넣냐 마냐 - static
# 멤버변수가 없다 -> 저장할게 없다 -> 객체를 안만들어도 된다
# -> 객체를 안만들고 사용가능한 static메소드

# 총 판매자 수 파악 : DB서버랑 통신해서... -> 부담스러움 -> 횟수를 줄이자
# -> 처음 한번만 세고, 변화가 일어나면 수동 카운팅


class SellerDAO:
    def __init__(self):
        self.setAllSellerCount() # 처음 한번만
        self.sellerPerPage = 3

    def get(self, pageNo, searchTxt):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            searchTxt = "%" + searchTxt + "%"
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.sellerPerPage + 1
            end = pageNo * self.sellerPerPage

            sql = ("SELECT * from ( SELECT rownum AS rn, s_no, s_name, s_addr, s_birthday from ( SELECT * FROM nov11_seller WHERE s_name LIKE '%s' OR s_addr LIKE '%s' ORDER BY s_name)) WHERE rn >= %s AND rn <= %s") % (searchTxt, searchTxt, start, end)
            cur.execute(sql)

            sellers = []
            for _, no, name, addr, birthday in cur:
                s= Seller(no, name, addr, birthday)
                sellers.append(s)
            return sellers
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getAll(self):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")
            sql = "select * from nov11_seller order by s_name"
            cur.execute(sql)

            sellers = []
            for no, name, addr, birthday in cur:
                s= Seller(no, name, addr, birthday)
                sellers.append(s)
            return sellers

            # return cur
            #  1) 16번줄에서 닫아서 없어짐
            #  2) V를 작업하는 사람은 Python을 잘 모르는 사람 -> 최대한 쓰기 쉽게 만들어줘야

        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getPageCount(self, searchTxt):
        if searchTxt == "":
            sellerCount = self.allSellerCount
        else:
            sellerCount = self.getSellerCount(searchTxt)
        return ceil(sellerCount / self.sellerPerPage)

    def reg(self, seller):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            sql = "INSERT INTO nov11_seller VALUES (nov11_seq.nextval, '%s', '%s', to_date(%s, 'YYYYMMDD'))" % (seller.name, seller.addr, seller.birthday)

            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                
                self.allSellerCount += 1
                print(self.allSellerCount)
                
                return "등록 성공"
            else: 
                return "등록 실패"
        except Exception as e:
            print(e)
            return "등록 실패"
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getSellerCount(self, searchTxt):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")
            searchTxt = "%" + searchTxt + "%"
            sql = "select count(*) from nov11_seller WHERE s_name LIKE '%s' OR s_addr LIKE '%s'" % (searchTxt, searchTxt)
            cur.execute(sql)

            for result in cur:
                return result[0]
        except Exception as e:
            print(e)
            return 0
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def setAllSellerCount(self):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")
            sql = "select count(*) from nov11_seller"
            cur.execute(sql)

            for result in cur:
                self.allSellerCount = (result[0]) # allSellerCount라는 멤버변수에 8세팅
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)