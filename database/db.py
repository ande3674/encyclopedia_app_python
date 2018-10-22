import sqlite3

DB_URL = 'jdbc:sqlite:C:/Users/ce691/PycharmProjects/quick_flickr\library.sqlite'
DB_FILE = 'C:/Users/ce691/PycharmProjects/quick_flickr\library.sqlite'

SQL_INSERT_FLICKR = "INSERT INTO flickr VALUES ('{name}', '{owner}', '{server}', '{ispublic}', '{isfriend}', '{farm}', '{id}', '{secret}', '{title}', '{isfamily}')"
SQL_INSERT_GIPHY = "INSERT INTO giphy VALUES ('{name}', '{typ}', '{id}', '{slug}', '{url}')"
SQL_INSERT_UNSPLASH = "INSERT INTO unsplash VALUES ('{name}', '{id}', '{width}', '{height}', '{description}', '{url}')"

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

# s = SQL_INSERT_FLICKR.format(owner='150516435@n03', server='1931', ispublic=1, isfriend=0, farm=2, id='30545493287', secret='c65a0e8188', title='Megan & Buddy', isfamily=0)
# print(s)