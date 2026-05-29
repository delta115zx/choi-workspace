"""
Oracle DB 전체 덤프 스크립트
사용자: delta115 / DB: 10.1.92.102:1521/XE
출력: db_backup/delta115_dump.sql
"""
import oracledb
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

HOST = os.getenv("ORACLE_HOST", "10.1.92.102")
PORT = int(os.getenv("ORACLE_PORT", "1521"))
SID  = os.getenv("ORACLE_SID", "XE")
USER = os.environ["ORACLE_USER"]
PASS = os.environ["ORACLE_PASS"]
OUT  = "delta115_dump.sql"

conn = oracledb.connect(user=USER, password=PASS, dsn=f"{HOST}:{PORT}/{SID}")
cur  = conn.cursor()

cur.execute("SELECT table_name FROM user_tables ORDER BY table_name")
tables = [row[0] for row in cur.fetchall()]

lines = []
lines.append(f"-- Oracle dump: {USER}@{HOST}:{PORT}/{SID}")
lines.append(f"-- Generated : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
lines.append(f"-- Tables    : {len(tables)}")
lines.append("")

for table in tables:
    print(f"  dumping {table}...")
    lines.append(f"-- ============================================================")
    lines.append(f"-- TABLE: {table}")
    lines.append(f"-- ============================================================")

    # 컬럼 정보 조회
    cur.execute("""
        SELECT column_name, data_type, data_length, data_precision, data_scale, nullable
        FROM user_tab_columns
        WHERE table_name = :t
        ORDER BY column_id
    """, t=table)
    columns = cur.fetchall()

    # CREATE TABLE
    col_defs = []
    for col_name, dtype, dlen, dprec, dscale, nullable in columns:
        if dtype == "NUMBER":
            if dprec is not None and dscale is not None:
                type_str = f"NUMBER({dprec},{dscale})"
            elif dprec is not None:
                type_str = f"NUMBER({dprec})"
            else:
                type_str = "NUMBER"
        elif dtype in ("VARCHAR2", "NVARCHAR2", "CHAR", "NCHAR"):
            type_str = f"{dtype}({dlen})"
        elif dtype == "FLOAT":
            type_str = f"FLOAT({dprec})" if dprec else "FLOAT"
        else:
            type_str = dtype
        null_str = "" if nullable == "Y" else " NOT NULL"
        col_defs.append(f"    {col_name} {type_str}{null_str}")

    lines.append(f"CREATE TABLE {table} (")
    lines.append(",\n".join(col_defs))
    lines.append(");")
    lines.append("")

    # 제약조건 (PK)
    cur.execute("""
        SELECT cc.column_name
        FROM user_constraints c
        JOIN user_cons_columns cc ON c.constraint_name = cc.constraint_name
        WHERE c.table_name = :t AND c.constraint_type = 'P'
        ORDER BY cc.position
    """, t=table)
    pk_cols = [row[0] for row in cur.fetchall()]
    if pk_cols:
        lines.append(f"ALTER TABLE {table} ADD PRIMARY KEY ({', '.join(pk_cols)});")
        lines.append("")

    # INSERT 데이터
    col_names = [col[0] for col in columns]
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    if rows:
        lines.append(f"-- {len(rows)} rows")
        for row in rows:
            values = []
            for val, (col_name, dtype, *_) in zip(row, columns):
                if val is None:
                    values.append("NULL")
                elif dtype in ("VARCHAR2", "NVARCHAR2", "CHAR", "NCHAR", "CLOB"):
                    escaped = str(val).replace("'", "''")
                    values.append(f"'{escaped}'")
                elif dtype == "DATE" or dtype.startswith("TIMESTAMP"):
                    values.append(f"TO_DATE('{val}', 'YYYY-MM-DD HH24:MI:SS')")
                else:
                    values.append(str(val))
            lines.append(f"INSERT INTO {table} ({', '.join(col_names)}) VALUES ({', '.join(values)});")
        lines.append("")
    else:
        lines.append("-- (no rows)")
        lines.append("")

cur.close()
conn.close()

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"\n완료: {OUT} ({len(lines)}줄, 테이블 {len(tables)}개)")
