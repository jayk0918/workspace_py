import cx_Oracle

cx_Oracle.init_oracle_client(lib_dir=r'')
conn = cx_Oracle.connect('admin', 'Jayk09180918', 'phonedb_high')
cs = conn.cursor()

rank = 1
title = '외계+인 1부'
filePath = '/Users/jaykim0918/Downloads/BufferedWriter/e5225545-b0c7-4dbb-8b4e-a6086de94f76.jpg'

sql = '''
    insert into movie values(seq_movie_no.nextval, :rank, :title, :filePath)
'''

cs.execute(sql, rank=rank, title=title, filePath=filePath)
conn.commit()

cs.close()
conn.close()