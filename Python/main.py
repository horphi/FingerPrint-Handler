from py_uareu import u_are_u as freader
from pymongo import MongoClient
# import bson
# import bson.binary

client = MongoClient()
db = client['fprint']
fingers = db['finger']

# fingers = []
#
# for i in xrange(10):
#     fingers.append(freader.getFinger("finger#{}".format(i)))

ref = freader.getFinger("1128264989")
ref['fmd'] = ref['fmd'].decode('base64_codec')
finger_id = fingers.insert_one(ref).inserted_id

print finger_id

# print "id: {} \tsize: {}\t len: {}\n".format(result['id'], result['size'], len(result['fmd']))
# reference = freader.getFinger("ref")
# print "id: {}\tsize: {}\t len: {}\n".format(reference['id'], reference['size'], len(reference['fmd']))
# print freader.compareFinger(result['fmd'], result['size'], reference['fmd'], reference['size'])

# print freader.identifyFinger(
# (result['fmd'], result['size'],
# reference['fmd'], reference['size'])
# )

# Make the Input

# def makeCompareInput(finger, fingers):
#     out = []
#     out.append(finger['fmd'])
#     out.append(finger['size'])
#     for f in fingers:
#         out.append(f['fmd'])
#         out.append(f['size'])
#
#     return tuple(out)
#
# comp = makeCompareInput(ref, fingers)
#
# print freader.identifyFinger(comp)