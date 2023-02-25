import pymongo
from Classes import DATA, Dataprocess, DbMongo


def main():

    client, db = DbMongo.getDB()

    pipeline = Dataprocess(DATA)
    
    pipeline.create_careers()
    pipeline.create_students()
    pipeline.create_enrollments()

    return True

if __name__ == "__main__":
    main()