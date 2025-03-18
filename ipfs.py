import requests
import json

import ipfshttpclient

def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error pin_to_ipfs expects a dictionary"
    
    # Convert the dictionary to a JSON string
    json_data = json.dumps(data)
    
    # Connect to the local IPFS node (default address)
    with ipfshttpclient.connect() as client:
        # Add the JSON data to IPFS
        res = client.add_json(json_data)
        
    # The CID is returned after adding
    cid = res
    return cid



def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), f"get_from_ipfs accepts a cid in the form of a string"
    
    url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    assert isinstance(data, dict), f"get_from_ipfs should return a dict"
    return data
