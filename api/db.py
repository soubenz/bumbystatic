from pymongo import MongoClient, DESCENDING
from pymongo.write_concern import WriteConcern
from pymongo.errors import DuplicateKeyError, OperationFailure
from bson.objectid import ObjectId
from bson.errors import InvalidId
from pymongo.read_concern import ReadConcern
from werkzeug.local import LocalProxy
from timeit import default_timer as timer
MFLIX_DB_URI = "mongodb://samartian:shakif94@mongodb-4498-0.cloudclusters.net:10023"


def get_db():
    """
    Configuration method to return db instance
    """
    # db = getattr(g, "_database", None)
    # MFLIX_DB_URI = ""
    # if db is None:
    """
    Ticket: Connection Pooling

    Please change the configuration of the MongoClient object by setting the
    maximum connection pool size to 50 active connections.
    """
    """
    Ticket: Timeouts

    Please prevent the program from waiting indefinitely by setting the
    write concern timeout limit to 2500 milliseconds.
    """

    db = MongoClient(
        MFLIX_DB_URI,
        # TODO: Connection Pooling
        # Set the maximum connection pool size to 50 active connections.
        # TODO: Timeouts
        # Set the write timeout limit to 2500 milliseconds.
    )["promotya"]
    return db


db = LocalProxy(get_db)

# def add_user(name, email, hashedpw):
#     """
#     Given a name, email and password, inserts a document with those credentials
#     to the `users` collection.
#     """
#     try:
#         # : User Management
#         # insert a user with the "name", "email", and "password" fields
#         new_user = {"email": email, "name": name, "password": hashedpw}

#         db.users.insert_one(new_user)
#         return {"success": True}
#     except DuplicateKeyError:
#         return {"error": "A user with the given email already exists."}

# def activate_tracking(_id, frequency):
#     return db.websites.update_one({'_id': ObjectId(_id)}, {'$set': {'isactivated': True, 'frequency': frequency}})

# def deactivate_tracking(_id):
#     return db.websites.update_one({'_id': ObjectId(_id)}, {'$set': {'isactivated': False}})

# def stop_tracking():
#     db.users.update_one({'x': 1}, {'$set': {'isactivated': 0}})
# def get_user(email):
#     """
#     Given an email, returns a document from the `users` collection.
#     """
#     # TODO: User Management
#     # Retrieve the user document corresponding with the user's email.
#     return db.users.find_one({"email": email})

# db = get_db()
# add_user("test", "test2", "sestg")


def get_influencers(size, page_num):
    size = int(size)
    page_num = int(page_num)
    # Calculate number of documents to skip
    skips = size * (page_num - 1)
    total = db.influencers.count_documents({})
    cursor = db.influencers.find({}, {"_id": 0}).skip(skips).limit(size)
    influencers = [x for x in cursor]
    return {"data": influencers, "total": total}


def get_all_influencers():
    total = db.influencers.estimated_document_count()
    start = timer()
    # cursor = db.influencers.find({}, {"_id": 0})
    # influencers = list(cursor)
    pipeline = [{
        '$bucket': {
            'groupBy': '$followers',
            'boundaries': [5000, 10000, 20000, 400000],
            'default': 'Other',
            'output': {
                'count': {
                    '$sum': 1
                },
                'data': {
                    '$push': '$$ROOT'
                }
            }
        }
    }]
    cursor = list(db.influencers.aggregate(pipeline, allowDiskUse=True))
    # for c in cursor:
    # print(c['username'])
    # influencers = [x for x in cursor]
    # influencers = [*cursor]
    end = timer()
    print(f"execution time (ms) {end - start} ")

    return {"data": cursor, "total": total}


def add_favorite(user_uid, influencer_username):
    update_data = {"favorites": influencer_username}
    r = db.users.update_one({"userUid": user_uid}, {"$push": {update_data}},
                            upsert=True)
    if r:
        return {"data": "success"}


def delete_favorite(user_uid, influencer_username):

    update_data = {"favorites": influencer_username}
    r = db.users.update_one({"userUid": user_uid}, {"$push": {insert_data}})
    if r:
        return {"data": "success"}


def get_influencer_detail(username):
    influencer = db.influencers.find_one({"username": username}, {"_id": 0})
    print(type(influencer))
    return {"data": influencer}


def search_website(domain):
    return db.websites.find_one({"domain": domain})


def list_websites():
    return db.websites.find()


def list_products(website_id):
    return db.products.find()


def get_website(_id):
    return db.websites.find_one({"_id": ObjectId(_id)})


def add_website(domain, frequency):
    """
    Given a name, email and password, inserts a document with those credentials
    to the `users` collection.
    """
    try:
        # : User Management
        # insert a user with the "name", "email", and "password" fields
        new_website = {
            "domain": domain,
            "frequency": frequency,
            "is_activated": False
        }

        db.websites.insert_one(new_website)
        return {"success": True}
    except DuplicateKeyError:
        return {"error": "A website with the given domain already exists."}


# get_all_influencers()