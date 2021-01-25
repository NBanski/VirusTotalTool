import sqlite3, json

from modules.local.databaseBasic import connectDb
from modules.network.apiRequests import getReport, getUrlScan, getFileReport

def sqliteWildcard(keyword):
    keyword = "'%" + keyword + "%'"
    return keyword

def insertReport(id):
    # Taking response from HTTP API.
    data = getReport(id)
    data = data.json()
    # Here we have to check response code.
    if data["response_code"] == 0:
        table_name = "not_found"
        x = 3
    if data["response_code"] == 1:
        table_name = "reports"
        x = 10
    # Here we're exctracting key values from JSON data to create SQL query.
    columns = list(data.keys())[:x]
    values = list(data.values())[:x]
    sql_string = 'INSERT INTO {} '.format(table_name)
    sql_string += "(" + ", ".join(columns) + ")\nVALUES " + "("
    for _ in values:
        sql_string += "'" + str(_) + "'" + ", "
    sql_string = sql_string[:-2] + ")"
    try:
        db = connectDb()
        db.executescript(sql_string)
    except sqlite3.IntegrityError as e:
        print(e)

def insertFileReport(fileHash):
    # Taking response from HTTP API.
    data = getFileReport(fileHash)
    data = data.json()
    # Here we have to check response code.
    if data["response_code"] == 0:
        tableName = "file_not_found"
        x = 3
    elif data["response_code"] == 1:
        tableName = "file_reports"
        x = 11
    # Extracting key values from JSON data do create SQL query.
    columns = list(data.keys())[1:x]
    values = list(data.values())[1:x]
    sqlString = 'INSERT INTO {} '.format(tableName)
    sqlString += "(" + ", ".join(columns) + ")\nVALUES " + "("
    for _ in values:
        sqlString += "'" + str(_) + "'" + ", "
    sqlString = sqlString[:-2] + ")"
    try:
        db = connectDb()
        db.executescript(sqlString)
    except sqlite3.IntegrityError as e:
        print(e)

def extractReportByUrl(url):
    sql_string = "SELECT * FROM reports WHERE url LIKE {} ORDER BY scan_date DESC".format("'%" + url + "%'")
    try:
        db = connectDb()
        report = db.execute(sql_string).fetchone()
        rep_url = report[2]
        rep_positives = report[8]
        rep_all = report[9]
        rep_time = report[4]
        rep_data = rep_url + " - " + rep_positives + "/" + rep_all + " at " + rep_time
        return rep_data
    except sqlite3.IntegrityError as e:
        print(e)
    except TypeError as e:
        try:
            sql_string = "SELECT * FROM not_found WHERE resource LIKE {}".format("'%" + url + "%'")
            not_found = db.execute(sql_string).fetchone()
            url = not_found[1]
            return (url + " not found in the dataset.")
        except TypeError as e:
            print(e)
            return("Incorrect input.")

def extractReportById(id):
    sql_string = "SELECT * FROM reports WHERE scan_id LIKE {} ORDER BY scan_date DESC".format("'" + id + "'")
    try:
        db = connectDb()
        report = db.execute(sql_string).fetchone()
        rep_url = report[2]
        rep_positives = report[8]
        rep_all = report[9]
        rep_time = report[4]
        rep_data = rep_url + " - " + rep_positives + "/" + rep_all + " at " + rep_time
        return rep_data
    except sqlite3.IntegrityError as e:
        print(e)
    except TypeError as e:
        print(e)
        try:
            sql_string = "SELECT * FROM not_found WHERE resource LIKE {}".format("'" + id + "'")
            not_found = db.execute(sql_string).fetchone()
            url = not_found[1]
            return (url + " not found in the dataset.")
        except TypeError as e:
            print(e)
            return("Incorrect input.")

def extractReportByHash(hash):
    sql_string = "SELECT * FROM file_reports WHERE resource LIKE {} ORDER BY scan_date DESC".format("'" + hash + "'")
    try:
        db = connectDb()
        report = db.execute(sql_string).fetchone()
        # rep_hash = str(report[2])
        rep_positives = str(report[8])
        rep_all = str(report[7])
        rep_time = str(report[4])
        rep_data = (rep_positives + "/" + rep_all + " at " + rep_time)
        return rep_data
    except sqlite3.IntegrityError as e:
        print(e)
    except TypeError as e:
        print(e)
        try:
            sql_string = "SELECT * FROM file_not_found WHERE resource LIKE {}".format("'" + id + "'")
            not_found = db.execute(sql_string).fetchone()
            url = not_found[1]
            return (url + " not found in the dataset.")
        except TypeError as e:
            print(e)
            return("Incorrect input.")

def queryUrlScan(url):
    try:
        data = getUrlScan(url)
        data = data.json()
        scanId = data["scan_id"]
        return scanId
    except KeyError:
        return {"response_code" : "0"}

def searchDatabase(url):
    get_tables = "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%';"
    tables = connectDb().execute(get_tables).fetchall()
    tables_list = []
    for tup in tables:
        for _ in tup:
            tables_list.append(_)
    all_results = []
    for _ in tables_list:
        if _ == "reports":
            sql_string = "SELECT * FROM " + _ + " WHERE url LIKE " + sqliteWildcard(url)
            results = connectDb().execute(sql_string).fetchall()
            for tup in results:
                report_url = tup[2]
                report_result = tup[8] + "/" + tup[9]
                report_date = tup[4]
                res_data = report_url + " " + report_result + " " + report_date
                all_results.append(res_data)
        if _ == "not_found":
            sql_string = "SELECT * FROM " + _ + " WHERE resource LIKE " + sqliteWildcard(url)
            results = connectDb().execute(sql_string).fetchall()
            for tup in results:
                all_results.append(tup[1] + " wasn't found in the dataset.")
    return(all_results)