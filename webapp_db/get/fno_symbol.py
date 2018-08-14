# -*- coding: utf-8 -*-
__author__ = "Rajesh Rao"
__copyright__ = "meh"
__status__ = "Development"

def fno_symbol(cursor):
    get_query = ''' 
    SELECT A.SYMBOL AS SYMBOL 
    FROM 
    SECURITIES.SECURITIES AS A, 
    SECURITIES.SECURITIES_TYPE AS B 
    WHERE 
    A.TYPE_ID = B.ID 
    AND 
    B.NAME = 'FNO';
    '''
    cursor.execute(get_query)
    result = cursor.fetchall()
    return result



