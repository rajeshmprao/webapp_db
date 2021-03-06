# -*- coding: utf-8 -*-
__author__ = "Rajesh Rao"
__copyright__ = "meh"
__status__ = "Development"
import time
def options_eod_data(cursor,
                        data):
    insert_query = '''
       INSERT INTO `SECURITIES_PRICE`.`FNO_EOD`
        (`SYMBOL`,
        `INSTRUMENT`,
        `DATE`,
        `STRIKE PRICE`,
        `EXPIRY`,
        `OPTION TYPE`,
        `OPEN`,
        `HIGH`,
        `LOW`,
        `CLOSE`,
        `SETTLE`,
        `OI`,
        `OI_CHANGE`)
        VALUES '''
    placeholder = ','.join(['%s']*13)
    placeholder = '(' + placeholder + ')'
    placeholder = ','.join([placeholder]*int(len(data)/13))
    insert_query += placeholder
    params = data
    try:
        cursor.execute(insert_query, params)
    except Exception as e:
        print(cursor.mogrify(insert_query, params))
        raise
        if e.args[0] == 1062:
            pass
        else:
            print(cursor.mogrify(insert_query, params))
            raise(e)
    return