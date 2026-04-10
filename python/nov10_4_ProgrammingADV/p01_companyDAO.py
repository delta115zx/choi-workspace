from Choi.choiDBManager import ChoiDBManager


class companyDAO:
    def reg(company):
        con, cur = ChoiDBManager.makeConCur("delta115/cjy0115@195.168.9.70:1521/xe")

        sql = "INSERT INTO nov10_company VALUES ('%s', '%s', '%s', %d)" % (company.name, company.addr, company.ceo, company.emp)

        cur.execute(sql)

        if cur.rowcount == 1:
            company.insertResult = "등록 성공"
            con.commit()
        else:
            company.insertResult = "등록 실패"

        ChoiDBManager.closeConCur(con, cur)