import MySQLdb

def connect_db():
    """ Creates a connection to the plants_vs_humans database 
    Arguments:
        none
    Returns:
        database connection object
    """
    db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="pcb", 
                         db="plants_vs_humans")
    return db

def close_db(db):
    """ close the connection to the plants_vs_humans database 
    Arguments:
        db - database connection object
    Returns:
        Nothing
    """
    db.close()
    
    
def get_targets():
    """ retrieves all target IDs
    Arguments:
        None
    Returns:
        a list with all DISTINCT target IDs
    """
    
    db = connect_db()
    my_cursor = db.cursor()

    SQL = """SELECT DISTINCT(target)
            FROM blast_result;"""
    num_res = my_cursor.execute(SQL)
     
    targets = [] # this is where the target IDs should go
    for row in my_cursor:
        targets.append(row[0])

    my_cursor.close()
    close_db(db)

    return targets
    
def get_rows_for_target(target_id,e_value):
    """ select the rows in the database that match the target_id
    Arguments:
        target_id - string with the ID of the target
        e_value - float representing the e_value threshold
    Returns:
        the resulting rows
    """
    SQL = """SELECT query,target,evalue,description
    	    FROM blast_result,protein
    	    WHERE blast_result.query = protein.ID
    	    AND blast_result.target LIKE '%%%s'
            AND evalue <= %f;"""%(target_id,e_value)

    db = connect_db()
    my_cursor = db.cursor()
    num_res = my_cursor.execute(SQL)

    rows = my_cursor.fetchall()

    my_cursor.close()
    close_db(db)

    return rows
 
def get_queries_sequence_for_target_seq(target_id):
    """ Create a text file with the sequences for the queries matching 
        the given target in FASTA format
    Arguments:
        target_id - string with the ID of the target
    Returns:
        number of found queries for the target
    """
    SQL = """SELECT ID, sequence
    	    FROM blast_result,protein
    	    WHERE blast_result.query = protein.ID
    	    AND blast_result.target LIKE '%%%s'"""%target_id

    db = connect_db()
    my_cursor = db.cursor()
    num_res = my_cursor.execute(SQL)

    fasta_filename = "%s.fasta"%target_id
    fasta_file = open(fasta_filename,'w')

    rows = my_cursor.fetchall()
    for row in rows:
        fasta_id = row[0]
        sequence = row[1]
        fasta_file.write(">%s\n"%fasta_id)
        for i in range(0,len(sequence),60):
            fasta_file.write("%s\n"%sequence[i:i+60])
  
    fasta_file.close()
    my_cursor.close()
    close_db(db)

    return num_res
    
# The testing code below is not executed when db_functions is used as a module
if __name__ == "__main__":
    targets = get_targets()
    print "There are %s distinct targets in the database"%len(targets)
    
    rows = get_rows_for_target("1433E_HUMAN",0.001)
    print "There are %d rows for target 1433E_HUMAN"%len(rows) 
    print "This is the first row:",rows[0]
    
    target_id = "1433E_HUMAN"
    num_res = get_queries_sequence_for_target_seq(target_id)
    print "Save %d sequences in the fasta file %s.fasta"%(num_res,target_id)
