import sqlite3

'''Module containing functions for database manipulation'''

def create_all_tables():
    '''Creates all six tables for database'''
    try:
        create_db_table_microphones()
        create_db_table_headphones()
        create_db_table_audio_mixers()
        create_db_table_capture_cards()
        create_db_table_gaming_laptops()
        create_db_table_webcams()
    except sqlite3.Error as db_error:
        print(f'A database error occured while creating tables: {db_error}')
    finally:
        print(f'Tables have been created if no error')

def create_db_connection():
    '''Creates database connection and returns that connnection'''
    db_name = 'amazon_products.db'
    db_connection = sqlite3.connect(db_name)
    return db_connection

def create_db_cursor(db_connection):
    '''Creates database cursor object and returns that cursor'''
    db_cursor_object = db_connection.cursor()
    return db_cursor_object



def create_db_table_headphones():
    '''Creates headphones table in database'''
    # Creates database connection
    db_connection = create_db_connection()
    #Creates cursor object
    db_cursor_object = create_db_cursor(db_connection)
    #Creates headphones table if not exists
    db_cursor_object.execute('''CREATE TABLE IF NOT EXISTS over_ear_headphones(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
    #Clears headphones table if data in it from previous use
    db_cursor_object.execute('DELETE FROM over_ear_headphones')
    db_connection.close()

def create_db_table_microphones():
    '''Creates microphones table in database'''
    # Creates database connection
    db_connection = create_db_connection()
    #Creates cursor object
    db_cursor_object = create_db_cursor(db_connection)
    # Creates usb microphones table if not exists
    db_cursor_object.execute('''CREATE TABLE IF NOT EXISTS usb_microphones(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
    # Clears usb_microphones table if data in it from previous use
    db_cursor_object.execute('DELETE FROM usb_microphones')
    db_connection.close()


def create_db_table_webcams():
    '''Creates webcams table in database'''
    # Creates database connection
    db_connection = create_db_connection()
    #Creates cursor object
    db_cursor_object = create_db_cursor(db_connection)
    # Creates webcams table if not exists
    db_cursor_object.execute('''CREATE TABLE IF NOT EXISTS webcams(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
    # Clears webcams table if data in it from previous use
    db_cursor_object.execute('DELETE FROM webcams')
    db_connection.close()


def create_db_table_capture_cards():
    '''Creates capture cards table in database'''
    # Creates database connection
    db_connection = create_db_connection()
    #Creates cursor object
    db_cursor_object = create_db_cursor(db_connection)
    # Creates capture cards table if not exists
    db_cursor_object.execute('''CREATE TABLE IF NOT EXISTS capture_cards(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
    # Clears capture_cards table if data in it from previous use
    db_cursor_object.execute('DELETE FROM capture_cards')
    db_connection.close()


def create_db_table_audio_mixers():
    '''Creates audio mixer table in database'''
    # Creates database connection
    db_connection = create_db_connection()
    #Creates cursor object
    db_cursor_object = create_db_cursor(db_connection)
    # Creates audio mixers table if not exists
    db_cursor_object.execute('''CREATE TABLE IF NOT EXISTS audio_mixers(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')
    # Clears audio_mixers table if data in it from previous use
    db_cursor_object.execute('DELETE FROM audio_mixers')
    db_connection.close()


def create_db_table_gaming_laptops():
    '''Creates gaming laptops table in database'''
    # Creates database connection
    db_connection = create_db_connection()
    #Creates cursor object
    db_cursor_object = create_db_cursor(db_connection)
    # Creates gaming laptops table if not exists
    db_cursor_object.execute('''CREATE TABLE IF NOT EXISTS gaming_laptops(
                                product_name TEXT,
                                rating REAL,
                                num_ratings INTEGER,
                                price REAL,
                                product_url TEXT);''')

    # Clears gaming_laptops table if data in it from previous use
    db_cursor_object.execute('DELETE FROM gaming_laptops')
    db_connection.close()
