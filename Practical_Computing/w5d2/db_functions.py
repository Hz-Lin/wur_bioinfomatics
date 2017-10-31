import MySQLdb

def connect_db():
    db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="pcb", db="plants_vs_humans")
    return db

def close_db(db):
    db.close()

def get_targets():

    db = connect_db()
    my_cursor = db.cursor()

    SQL = """SELECT DISTINCT target FROM blast_result"""
    num_res = my_cursor.execute(SQL)
    
    targets = [] 
    for row in my_cursor:
        targets.append(row[0])

    my_cursor.close()
    close_db(db)

    return targets

def get_rows_for_target(target_id,e_value=10.0):

    SQL = """SELECT query,target,evalue,description
    	    FROM blast_result, protein
    	    WHERE blast_result.query = protein.ID
    	    AND blast_result.target LIKE '%%%s'
            AND blast_result.evalue <= 10.0;""" %target_id

    db = connect_db()
    my_cursor = db.cursor()
    num_res = my_cursor.execute(SQL)

    rows = my_cursor.fetchall()

    my_cursor.close()
    close_db(db)

    return rows

def get_queries_sequence_for_target_seq(target_id):

    SQL = """SELECT ID, sequence, query, target
	    FROM protein, blast_result
	    WHERE blast_result.query = protein.ID
	    AND blast_result.target LIKE '%%%s';"""%target_id

    db = connect_db()
    my_cursor = db.cursor()
    num_res = my_cursor.execute(SQL)

    fasta_filename = 'target_id.fasta'
    fasta_file = open(fasta_filename,'w')

    # write the FASTA file
    for row in my_cursor:
        print row
        header = '>' + row[0] + '\n'
        fasta_file.write(header)
        seq = row[1]
        if len(seq) <= 60:
            fasta_file.write(header)
        else:
            count = len(seq)//60 + 1
            start_index = 0
            end_index = 60
            for n in range(0,count):
                if n < count:
                    seq_line = seq[start_index:end_index] + '\n'
                    fasta_file.write(seq_line)
                if n == count:
                    seq_line = seq[start_index:len(seq)] + '\n'
                start_index += 60
                end_index += 60
                    
    
    fasta_file.close()
    my_cursor.close()
    close_db(db)

    return num_res

if __name__ == "__main__":
    print get_targets() 
    print get_rows_for_target("1433E_HUMAN")