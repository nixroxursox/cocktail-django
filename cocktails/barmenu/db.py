import sys
import requests
import logging
import json
import datetime

import nacl.pwhash
import nacl.utils

from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator
import couchbase
from couchbase.bucket import Bucket

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
couchbase.enable_logging()
cb_su = 'python'
cb_pass = 'passw0rd'

#function to create bucket using the api interface
def create_cb_bucket(bname,cbramnum):
    cb_url = ('http://localhost:8091/pools/default/buckets')
    cb_payload = {"name": bname,'ramQuotaMB': cbramnum, 'threadsNumber': "8", 'evictionPolicy': "fullEviction"}
    print(cb_url, cb_payload)
    cb_pa = (cb_su,cb_pass)
    r = requests.post(cb_url, auth=cb_pa, data=cb_payload)
    return r.json


#function to fetch a bucket - takeS bucket name as the only argument
def get_cb_bucket(cdbname):
    pa = PasswordAuthenticator(cb_su,cb_pass)
    try:
        cluster = Cluster('couchbase://127.0.0.1', ClusterOptions(pa))
        db = cluster.bucket(cdbname)
        return db
    except couchbase.exceptions.CouchbaseError as err:
        print(err)
        return "an error occurred"


def upsert_cb():
    create_cb_bucket(cbname)
    get_cb_bucket(cbname)
    
cbname = input("Enter bucket name: ")
create_cb_bucket(cbname,"256")
