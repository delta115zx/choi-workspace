from math import ceil
from Choi.choiDBManager import ChoiDBManager


class ProductDAO:
    def __init__(self):
        self.productPerPage = 5
        self.setAllProductCount()

    def reg(self, name, price):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = "INSERT INTO dec09_product VALUES('%s', %s)" % (name, price)

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return {"result": name + " 등록성공"}
            return {"result": name + " 등록실패"}
        except Exception as e:
            print(e)
            return {"result": name + " 등록실패"}
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def get(self, pageNo, search):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            productCount = self.allProductCount
            if search != "":
                productCount = self.getProductCount(search)

            pageCount = ceil(productCount / self.productPerPage)

            search = "%" + search + "%"
            pageNo = int(pageNo)
            start = (pageNo - 1) * self.productPerPage + 1
            end = pageNo * self.productPerPage

            sql = "SELECT * FROM ( SELECT rownum AS rn, p_name, p_price FROM ( SELECT * FROM dec09_product WHERE p_name LIKE '%s' ORDER BY p_name) )WHERE rn >= %s AND rn <= %s" % (search, start, end)

            cur.execute(sql)

            products = []
            for _, name, price in cur:
                products.append({"name": name, "price": price})
            result = {"pageCount": pageCount, "products": products}
            return result
        except Exception as e:
            print(e)
            return None
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getProductCount(self, search):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            search = "%" + search + "%"

            sql = "SELECT count(*) FROM dec09_product WHERE p_name LIKE '%s'" % (search)
            cur.execute(sql)

            for c in cur:
                return c[0]
        except Exception as e:
            print(e)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def setAllProductCount(self):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = "SELECT count(*) FROM dec09_product order by p_name"
            cur.execute(sql)

            for c in cur:
                self.allProductCount = c[0]
        except Exception as e:
            print(e)
        finally:
            ChoiDBManager.closeConCur(con, cur)
