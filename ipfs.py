import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_data = json.dumps(data)
	cid = ipfs.add_bytes(json_data.encode('utf-8'))['Hash']
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	data = ipfs.cat(cid).decode('utf-8')
	data = json.loads(data)
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
