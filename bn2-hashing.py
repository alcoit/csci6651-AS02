import hashlib

d = {}
# d['208f1a0c208342372b75d914b6c098d626becf07'] = "??"
# d['61fc7fbf6b24ff258633dad73f13f9bd66a2477f'] = "??"
# d['8a57a79d7a9921cd2344e7295dc72359780e9f9d'] = "??"
# d['bba1db3a9d5ba9f72b91312e730a9612dfdea053'] = "??"
# d['350d5bf1074e5557367a24ae9e07ab65aacfc031'] = "??"

#here is an example on how to use hashlib
value = "0x5FA"
print(value)
value = value.encode("utf-8")
print(value)
print(hashlib.sha1(value).hexdigest())

# def bruteforce():
  #here goes your code but this function should be never called on the 
  #system here
#  return []