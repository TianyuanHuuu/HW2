import requests
import json


def pin_to_ipfs(data):
    assert isinstance(data, dict), "Error pin_to_ipfs expects a dictionary"
    
    url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

    headers = {
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJhMmVkNTQyNC1kYTRlLTQ3MzktYTViYS1jOWRiYmJiYTBlZjkiLCJlbWFpbCI6InR5aHVAc2Vhcy51cGVubi5lZHUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJGUkExIn0seyJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MSwiaWQiOiJOWUMxIn1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiYWVkNzYxMDE2ODdjM2M3ZjBlYjkiLCJzY29wZWRLZXlTZWNyZXQiOiI3MTVmNjJmNGRhY2U1OTgxNTE0ZTNkYjE0NDA3NTAwMjBiOTdiMDhmOWRkNDNmNTRiOWZhZmVkMDU2ZDlmNDE4IiwiZXhwIjoxNzczNzk3NDg0fQ.6cjBFsCWImyuZXwwhWETG51mCoLDZXqzb4zfUxm1QtA",
        "Content-Type": "application/json"
    }

    payload = {
        "pinataContent": data
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    
    cid = response.json()['IpfsHash']
    return cid





def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), f"get_from_ipfs accepts a cid in the form of a string"
    
    url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    assert isinstance(data, dict), f"get_from_ipfs should return a dict"
    return data
