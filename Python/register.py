from py_uareu import u_are_u as freader
from pymongo import MongoClient
import bson

client = MongoClient()
db = client['fprint']
fingers = db['finger']

finger_id = raw_input("Insert the finger id: ");

ref = freader.getFinger(finger_id)
d = ref['fmd']
ref['fmd'] = ref['fmd'].encode('hex')
print fingers.insert_one(ref).inserted_id

f = fingers.find_one({"id":"10"})

if( d == f['fmd'].decode('hex')):
    print "Win"
else:
    print "Fail!"
