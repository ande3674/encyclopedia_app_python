import sqlite3

DB_URL = 'jdbc:sqlite:C:/Users/ce691/PycharmProjects/quick_flickr\library.sqlite'

SQL_INSERT_FLICKR = 'INSERT INTO flickr VALUES ({owner}, {server}, {ispublic}, {isfriend}, {farm}, {id}, {secret}, {title}, {isfamily})'
SQL_INSERT_GIPHY = 'INSERT INTO giphy VALUES ({typ}, {id}, {slug}, {url})'
SQL_INSERT_UNSPLASH = 'INSERT INTO unsplash VALUES ({id}, {width}, {height}, {description}, {url})'

def insert_flickr(owner, server, ispublic, isfriend, farm, id, secret, title, isfamily):
    sql = SQL_INSERT_FLICKR.format(owner=owner, server=server, ispublic=ispublic,
                                             isfriend=isfriend, farm=farm, id=id, secret=secret,
                                             title=title, isfamily=isfamily)
    # Connecting to the database
    conn = sqlite3.connect(DB_URL)
    c = conn.cursor()
    try:
        c.execute(sql)
    except sqlite3.DatabaseError:
        print('Error adding row to flickr table')
    conn.commit()
    conn.close()

def insert_giphy(typ, id, slug, url):
    sql = SQL_INSERT_GIPHY.format(typ=typ, id=id, slug=slug, url=url)
    conn = sqlite3.connect(DB_URL)
    c = conn.cursor()
    try:
        c.execute(sql)
    except sqlite3.DatabaseError:
        print('Error adding row to giphy table')
    conn.commit()
    conn.close()

def insert_unsplash(id, width, height, description, url):
    sql = SQL_INSERT_GIPHY.format(id=id, width=width, height=height, description=description, url=url)
    conn = sqlite3.connect(DB_URL)
    c = conn.cursor()
    try:
        c.execute(sql)
    except sqlite3.DatabaseError:
        print('Error adding row to unsplash table')
    conn.commit()
    conn.close()