# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 09:29:13 2021

@author: Usuario
"""
import http.client

conn = http.client.HTTPSConnection("data.mongodb-api.com")
payload = "{\r\n    \"collection\":\"revista\",\r\n    \"database\":\"biblioteca\",\r\n    \"dataSource\":\"Cluster0\",\r\n    \"document\": {\"nombre_revista\": \"vamos con todo\",\r\n    \"fecha_publicacion\":\"2005-05-12\",\r\n    \"precio\":\"2.75\",\r\n    }\r\n}"
headers = {
  'api-key': 'GCfkaESwRJfO2UN9Vmzcsn0zRuMkMgmTIBdF7JKWIaEhWtExSG7649OjNSVfwOf6',
  'Content-Type': 'text/plain'
}
conn.request("POST", "/app/data-gsakb/endpoint/data/beta/action/insertOne", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))