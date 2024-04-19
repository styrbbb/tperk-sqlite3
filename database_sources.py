from sqlalchemy import create_engine
conn = create_engine("sqlite:///C:\\sqlite\\epood_tperk.db")
r_set=conn.execute("SELECT * FROM tperk")
l1=[r for r in r_set.keys()] # List of column headers 
r_set = [list(r) for r in r_set]