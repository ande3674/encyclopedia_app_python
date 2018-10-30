import sqlite3

DB_URL = 'jdbc:sqlite:C:/Users/ce691/PycharmProjects/quick_flickr\library.sqlite'
#DB_FILE = 'C:/Users/ce691/PycharmProjects/quick_flickr\library.sqlite'
#DB_FILE2 = 'quick_flickr\library.sqlite'
DB_FILE = 'library.sqlite'

SQL_INSERT_FLICKR = "INSERT OR IGNORE INTO flickr VALUES ('{name}', '{owner}', '{server}', '{ispublic}', '{isfriend}', '{farm}', '{id}', '{secret}', '{title}', '{isfamily}')"
SQL_INSERT_GIPHY = "INSERT OR IGNORE INTO giphy VALUES ('{name}', '{typ}', '{id}', '{slug}', '{url}')"
SQL_INSERT_UNSPLASH = "INSERT OR IGNORE INTO unsplash VALUES ('{name}', '{id}', '{width}', '{height}', '{description}', '{url}')"

SQL_QUERY_FLICKR = "SELECT * FROM flickr WHERE name LIKE "
SQL_QUERY_GIPHY = "SELECT * FROM giphy WHERE name LIKE "
SQL_QUERY_UNSPLASH = "SELECT * FROM unsplash WHERE name LIKE "

CREATE_TABLE_FLICKR = "CREATE TABLE IF NOT EXISTS flickr (name TEXT, owner TEXT, server TEXT, ispublic TEXT, " \
                      "isfriend TEXT, farm TEXT, id TEXT PRIMARY KEY, secret TEXT, title TEXT, isfamily TEXT);"
CREATE_TABLE_GIPHY = "CREATE TABLE IF NOT EXISTS giphy (name TEXT, type TEXT, id TEXT PRIMARY KEY, slug TEXT, url TEXT);"
CREATE_TABLE_UNSPLASH = "CREATE TABLE IF NOT EXISTS unsplash (name TEXT, id TEXT PRIMARY KEY, width TEXT, height TEXT, description TEXT, url TEXT);"

SELECT_ALL_FLICKR = "SELECT farm, server, id, secret  FROM flickr"
SELECT_ALL_GIPHY = "SELECT id FROM giphy"
SELECT_ALL_UNSPLASH = "SELECT url FROM unsplash"

def createTables():
    conn = sqlite3.connect('library.sqlite')

    conn.execute(CREATE_TABLE_FLICKR)
    conn.execute(CREATE_TABLE_GIPHY)
    conn.execute(CREATE_TABLE_UNSPLASH)

    print('Tables created successfully!')

    conn.close()


def insert_flickr(name, owner, server, ispublic, isfriend, farm, id, secret, title, isfamily):
    sql = SQL_INSERT_FLICKR.format(name=name, owner=owner, server=server, ispublic=ispublic,
                                             isfriend=isfriend, farm=farm, id=id, secret=secret,
                                             title=title, isfamily=isfamily)
    # Connecting to the database
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute(sql)
    except sqlite3.DatabaseError:
        print('Error adding row to flickr table')
    conn.commit()
    conn.close()

def insert_giphy(name, typ, id, slug, url):
    sql = SQL_INSERT_GIPHY.format(name=name, typ=typ, id=id, slug=slug, url=url)
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute(sql)
    except sqlite3.DatabaseError:
        print('Error adding row to giphy table')
    conn.commit()
    conn.close()

def insert_unsplash(name, id, width, height, description, url):
    sql = SQL_INSERT_UNSPLASH.format(name=name, id=id, width=width, height=height, description=description, url=url)
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute(sql)
    except sqlite3.DatabaseError:
        print('Error adding row to unsplash table')
    conn.commit()
    conn.close()

def query_flickr(search_term):
    sql_statement = SQL_QUERY_FLICKR + "'%" + search_term + "%'"
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute(sql_statement)
    except sqlite3.DatabaseError:
        print('Error querying table.')
    all_rows = c.fetchall()
    conn.commit()
    conn.close()
    return all_rows

def query_giphy(search_term):
    sql_statement = SQL_QUERY_GIPHY + "'%" + search_term + "%'"
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute(sql_statement)
    except sqlite3.DatabaseError:
        print('Error querying table.')
    all_rows = c.fetchall()
    conn.commit()
    conn.close()
    return all_rows

def query_unsplah(search_term):
    sql_statement = SQL_QUERY_UNSPLASH + "'%" + search_term + "%'"
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute(sql_statement)
    except sqlite3.DatabaseError:
        print('Error querying table.')
    all_rows = c.fetchall()
    conn.commit()
    conn.close()
    return all_rows

def get_all_flickr():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute(SELECT_ALL_FLICKR)
    except sqlite3.DatabaseError:
        print('Error')
    all_rows = c.fetchall()
    conn.commit()
    conn.close()
    return all_rows

def get_all_giphy():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute(SELECT_ALL_GIPHY)
    except sqlite3.DatabaseError:
        print('Error')
    all_rows = c.fetchall()
    conn.commit()
    conn.close()
    return all_rows

def get_all_unsplash():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute(SELECT_ALL_UNSPLASH)
    except sqlite3.DatabaseError:
        print('Error')
    all_rows = c.fetchall()
    conn.commit()
    conn.close()
    return all_rows

rows = get_all_flickr()
print(rows)
