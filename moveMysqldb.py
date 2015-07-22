import pymysql.cursors
#https://github.com/PyMySQL/PyMySQL
#http://www.pymssql.org/en/latest/pymssql_examples.html
#pip install pymysql
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             passwd='123456',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    #with connection.cursor() as cursor:
        # Create a new record
        #sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #for x in xrange(1,10000):
            #cursor.execute(sql, ('webmaster'+str(x)+'@python.org', str(x)+'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    #connection.commit()
    c1 = connection.cursor()
    c1.execute("select count(1) as c from users" )
    count = c1.fetchone()
    pageSize = 10 
    totalPage = count['c']/pageSize
    flag = True;
    currentPage = 0;
    while flag:
        pass
        if currentPage>totalPage:
            flag = False
        with connection.cursor() as cursor:
            # Read a single record
            offset = currentPage*pageSize
            sql = "SELECT * FROM `users` WHERE 1 limit "+str(offset)+","+str(pageSize)
            #print sql
            cursor.execute(sql)
            result = cursor.fetchall()
            #print(result)
            for row in result:
                pass
                #print row['email']
                with connection.cursor() as c2:
                    sql2 = "INSERT INTO `test`.`users2` (`email`, `password`) VALUES (%s, %s)"
                    #print sql2
                    c2.execute(sql2, (row['email'], row['password']))
                    connection.commit()
        currentPage = currentPage+1
finally:
    connection.close()