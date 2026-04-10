from math import ceil
from Choi.choiDBManager import ChoiDBManager
from product.product2 import Product2
from product.product import Product


class ProductDAO:
    def __init__(self):
        self.setAllProductCount()  # 처음 한번만
        self.productPerPage = 3

    def get(self, pageNo, searchTxt):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            searchTxt = "%" + searchTxt + "%"
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.productPerPage + 1
            end = pageNo * self.productPerPage

            sql = (
                "SELECT * from( SELECT rownum AS rn, p_no, p_name, p_price, p_cate, p_s_no from( SELECT * FROM nov11_product WHERE p_name LIKE '%s' OR p_cate LIKE '%s' ORDER BY p_name, p_price)) WHERE rn >= %s AND rn <= %s"
            ) % (searchTxt, searchTxt, start, end)
            cur.execute(sql)

            products = []
            for _, no, name, price, cate, s_no in cur:
                p = Product(no, name, price, cate, s_no)
                products.append(p)
            return products

        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def get2(self, pageNo, searchTxt):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            searchTxt = "%" + searchTxt + "%"
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.productPerPage + 1
            end = pageNo * self.productPerPage

            sql = "SELECT * "
            sql += "FROM ( "
            sql += "    SELECT rownum AS rn, p_no, p_name, p_price, p_cate, s_name, s_addr, s_birthday "
            sql += "    FROM ( "
            sql += "        SELECT p_no, p_name, p_price, p_cate, s_name, s_addr, s_birthday "
            sql += "        FROM nov11_seller, nov11_product "
            sql += "        WHERE s_no = p_s_no "
            sql += "            AND (p_name LIKE '%s' OR p_cate LIKE '%s') " % (
                searchTxt,
                searchTxt,
            )
            sql += "        ORDER BY p_name, p_price "
            sql += "    ) "
            sql += ") "
            sql += "WHERE rn >= %d AND rn <= %d" % (start, end)
            cur.execute(sql)

            products = []
            for _, no, name, price, cate, s_name, s_addr, s_birthday in cur:
                p = Product2(no, name, price, cate, s_name, s_addr, s_birthday)
                products.append(p)
            return products

        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getMaxPrice(self):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            sql = "SELECT p_no, p_name, p_price, p_cate, s_name, s_addr, S_BIRTHDAY FROM NOV11_SELLER, nov11_product WHERE s_no = p_s_no AND P_PRICE  = (SELECT max(p_price) FROM NOV11_PRODUCT) ORDER BY p_name, p_price"
            cur.execute(sql)

            products = []
            for no, name, price, cate, s_name, s_addr, s_birthday in cur:
                p = Product2(no, name, price, cate, s_name, s_addr, s_birthday)
                products.append(p)
            return products

        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getAll(self):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")
            sql = "SELECT * FROM nov11_product order by p_name, p_price"
            cur.execute(sql)

            products = []
            for no, name, price, cate, s_no in cur:
                p = Product(no, name, price, cate, s_no)
                products.append(p)
            return products

        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getPageCount(self, searchTxt):
        if searchTxt == "":
            productCount = self.allProductCount
        else:
            productCount = self.getProductCount(searchTxt)
        return ceil(productCount / self.productPerPage)

    def getProductCount(self, searchTxt):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")
            searchTxt = "%" + searchTxt + "%"
            sql = (
                "select count(*) from nov11_product WHERE p_name LIKE '%s' OR p_cate LIKE '%s'"
                % (searchTxt, searchTxt)
            )
            cur.execute(sql)

            for result in cur:
                return result[0]
        except Exception as e:
            print(e)
            return 0
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def reg(self, product):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

            sql = (
                "INSERT INTO nov11_product VALUES (nov11_seq.nextval, '%s', '%s', '%s', '%s')"
                % (product.name, product.price, product.cate, product.s_no)
            )

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                self.allProductCount += 1
                return "등록 성공"
            else:
                return "등록 실패"
        except Exception as e:
            print(e)
            return "등록 실패"
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def setAllProductCount(self):
        try:
            con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")
            sql = "select count(*) from nov11_product"
            cur.execute(sql)

            for result in cur:
                self.allProductCount = result[0]  # allProductCount라는 멤버변수에 세팅
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)
