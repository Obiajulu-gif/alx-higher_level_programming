#!/usr/bin/python3
"""script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument."""

if __name__ == '__main__':
    import MySQLdb
    import sys
    
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_search".format(sys.argv[0]))
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[1:5]
    
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password,
                         db=database_name)
    
    cursor = db.cursor()
    
    cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
    