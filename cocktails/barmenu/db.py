import sys
import requests
import logging

import datetime

import nacl.pwhash
import nacl.utils

from couchbase.cluster import Cluster, ClusterOptions
from couchbase_core.cluster import PasswordAuthenticator
import couchbase
from couchbase.bucket import Bucket

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
couchbase.enable_logging()

#function to create bucket using the api interface
def create_cb_bucket(bname):
        cb_url = {"http://localhost:8091/"}
        payload = ("","","","")
#function to fetch a bucket - takeS bucket name as the only argument
def get_cb_bucket(cdbname):
    pa = PasswordAuthenticator('python', 'passw0rd')
    try:
        cluster = Cluster('couchbase://127.0.0.1', ClusterOptions(pa))
        db = cluster.bucket(cdbname)
        return db
    except couchbase.exceptions.CouchbaseError as err:
        print(err)
        return "an error occurred"



c = get_cb_bucket("ssodb")
print(c)
