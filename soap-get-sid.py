#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib, requests, base64, re
import xml.etree.ElementTree as ET

def main():
    # define your credentials
    username = "fritz1234"
    password = "fox7890"

    # legacy basicauth
    bytes_login = (username + ':' + password).encode("utf-8")
    bytes_b64 = base64.b64encode(bytes_login)
    method_old = 'Basic ' + bytes_b64.decode("utf-8")
    print(method_old)

    # send SOAP packet
    url = "http://10.0.0.1:49000/igdupnp/control/deviceconfig"
    headers = {'soapaction': 'urn:dslforum-org:service:DeviceConfig:1#X_AVM-DE_CreateUrlSID', 'Authorization': method_old, 'content-type': 'text/xml','charset': 'utf-8'}
    body = """<?xml version='1.0' encoding='utf-8'?><s:Envelope s:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/' xmlns:s='http://schemas.xmlsoap.org/soap/envelope/'><s:Body><u:X_AVM-DE_CreateUrlSID xmlns:u='urn:dslforum-org:service:DeviceConfig:1' /></s:Body></s:Envelope>"""
    boxdata = requests.post(url,data=body,headers=headers).content.decode('utf-8')
    print(boxdata)

main()
