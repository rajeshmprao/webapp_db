# -*- coding: utf-8 -*-
__author__ = "Rajesh Rao"
__copyright__ = "Copyright 2018 Minance. All rights reserved"
__status__ = "Development"

import pymysql


def cursor_conn(username, password, host):
    """
    This function is used to connect to Webapp_db schema.

    Args:
       name (str):  The username to use.

       password(str): The password to use.

       host(str): ip of host

    Returns:
       :class:`pymysql_cursor`, :class:`pymysql_connection` if connected successfuly

       :class:`None`, :class:`None` if error in connecting

    """

    database_user = username
    database_password = password
    database_ip = host

    conn = pymysql.connect(host=database_ip,
                           user=database_user,
                           password=database_password,
                           connect_timeout=10,
                           cursorclass=pymysql.cursors.DictCursor,
                           charset='utf8')

    cursor = conn.cursor()
    conn.autocommit(True)
    return cursor, conn