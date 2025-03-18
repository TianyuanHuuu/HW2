import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	# Pin JSON data to IPFS via Pinata API (no ipfs client required)
        url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    
        headers = {
            "Content-Type": "application/json"
        # If Pinata gave you API keys, add: "Authorization": f"Bearer {PINATA_JWT}"
        }
    
        payload = {
            "pinataContent": data
        }
    
	response = requests.post(url, headers=headers, json=payload)
	response.raise_for_status()
	    
	cid = response.json()['IpfsHash']  # <-- that's the returned CID
	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
	url = f"https://gateway.pinata.cloud/ipfs/{cid}"
	response = requests.get(url)
    	response.raise_for_status()
	data = response.json()
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
