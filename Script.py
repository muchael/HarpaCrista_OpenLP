'''
Created on 19/08/2014

@author: Newton Muchael
'''

import sqlite3

def parse_row( row ):
    list = row[0].split('\n')
    print(list)

def main():
    conn = sqlite3.connect('harpa.db')
    c = conn.cursor()
    
    numero = (1,)
    
    for row in c.execute('SELECT verse FROM verses WHERE idanthem = ? AND ismainverse = 0', numero):
        parse_row(row)
        
        
    conn.close()
        
main()