from math import ceil
from Choi.choiDBManager import ChoiDBManager


class ProductDAO:
    def __init__(self):
        self.productPerPage = 6
        self.setAllProductCount()

    def update(self, no, name, price, stock):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = (
                "UPDATE DEC03_PRODUCT SET p_name = '%s', p_price = %s, p_stock = %s WHERE p_no = %s"
                % (name, price, stock, no)
            )
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return {"result": "수정 성공"}
            return {"result": "수정 실패"}

        except Exception as e:
            print(e)
            return {"result": "수정 실패"}
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def delete(self, no):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = "delete from dec03_product where p_no = %d" % int(no)
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return "삭제 성공"
            return "삭제 실패"

        except Exception as e:
            print(e)
            return "삭제 실패"
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getDetail(self, no):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = "select * from dec03_product where p_no = %d" % int(no)
            cur.execute(sql)

            for no, name, price, stock, p_s_no in cur:
                return {
                    "no": no,
                    "name": name,
                    "price": price,
                    "stock": stock,
                    "p_s_no": p_s_no,
                }
        except Exception as e:
            print(e)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def getProductCount(self, search):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            search = "%" + search + "%"

            sql = "SELECT count(*) FROM dec03_product WHERE p_name LIKE '%s'" % (search)
            cur.execute(sql)

            for c in cur:
                return c[0]
        except Exception as e:
            print(e)
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

            sql = (
                "SELECT * from( SELECT rownum AS rn, p_no, p_name, p_price, p_stock, p_s_no FROM ( SELECT * FROM dec03_product WHERE P_NAME LIKE '%s' ORDER BY p_name, p_price )) WHERE rn >= %s AND rn <= %s"
                % (search, start, end)
            )
            cur.execute(sql)

            products = []

            for _, no, name, price, stock, p_s_no in cur:
                products.append(
                    {
                        "no": no,
                        "name": name,
                        "price": price,
                        "stock": stock,
                        "p_s_no": p_s_no,
                    }
                )
            result = {"pageCount": pageCount, "products": products}
            return result
        except Exception as e:
            print(e)
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def reg(self, n, p, s, p_s_no):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = (
                "insert into dec03_product values (dec03_seq.nextval, '%s', %s, %s, %s)"
                % (n, p, s, p_s_no)
            )

            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                self.allProductCount += 1
                return {"result": n + " 등록 성공"}
            return {"result": n + " 등록 실패"}
        except Exception as e:
            print(e)
            return {"result": n + " 등록 실패"}
        finally:
            ChoiDBManager.closeConCur(con, cur)

    def setAllProductCount(self):
        try:
            con, cur = ChoiDBManager.makeConCur(
                "delta115/cjy0115@195.168.9.232:1521/xe"
            )

            sql = "SELECT count(*) FROM dec03_product order by p_name, p_price"
            cur.execute(sql)

            for c in cur:
                self.allProductCount = c[0]
        except Exception as e:
            print(e)
        finally:
            ChoiDBManager.closeConCur(con, cur)
