import cx_Oracle
from pymongo import MongoClient

# must include '&ssl_cert_reqs=CERT_NONE' at the end of connection string
mongoDB_connection_uri = 'connection_string&ssl_cert_reqs=CERT_NONE'
mongoDB_name = 'db_name'
mongoDB_collection_name = 'exportResult'

oracle_connection_string = "oracle_connection_string"

def get_state(name, code):
    sql = ("select STATE_ID as state from STATE where STATE_ID in " +
                          "(select STATE_ID from person " +
                          "where name = :name and code = :code)")
    oracle_db = cx_Oracle.connect(oracle_connection_string)
    oracle_cursor = oracle_db.cursor()
    oracle_cursor.execute(sql, [name, code])
    row = oracle_cursor.fetchone()
    if row is None:
        print('Cannot find state for ' + name + ' ' + code)
        return 'not found'
    else:
        for state in row:
            return state


def update_state():
    mongo_client = MongoClient(mongoDB_connection_uri)
    mongoDB_collection = mongo_client[mongoDB_name][mongoDB_collection_name]
    for document in mongoDB_collection.find({}, {"_id": 1, "name": 1, "code": 1}):
        state = get_state(document['name'], document['code'])
        print("update document" + document['_id'])
        mongoDB_collection.update_one({"_id": document['_id']}, {"$set": {"state": state}})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(get_state('202100603328', '@@@'))
    update_state()

