#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib, requests, base64
import xml.etree.ElementTree as ET

def main():
    # define your IP and credentials
    url = "http://10.0.0.1/login_sid.lua?version=2"
    username = "fritz1234"
    password = "fox7890"

    # start the SID request for modern authentication
    r = requests.get(url)
    xml = ET.fromstring(r.content)
    challenge = xml.find("Challenge").text
    challenge_parts = challenge.split("$")
    iter1 = int(challenge_parts[1])
    salt1 = bytes.fromhex(challenge_parts[2])
    iter2 = int(challenge_parts[3])
    salt2 = bytes.fromhex(challenge_parts[4])
    hash1 = hashlib.pbkdf2_hmac("sha256", password.encode(), salt1, iter1)
    hash2 = hashlib.pbkdf2_hmac("sha256", hash1, salt2, iter2)
    challenge_response = "{}${}".format(challenge_parts[4], hash2.hex())
    post_data = {"username": username, "response": challenge_response}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(url, headers=headers, data=post_data)
    xml = ET.fromstring(r.content)
    sid = xml.find("SID").text

    # there is also legacy auth but it might get deprecated
    method_modern = 'Bearer %s' % sid
    bytes_login = (username + ':' + password).encode("utf-8")
    bytes_b64 = base64.b64encode(bytes_login)
    method_old = 'Basic ' + bytes_b64.decode("utf-8")
    print(method_modern)
    print(method_old)

    # let us continue with the modern SID way
    url = "http://10.0.0.1:49000/igdupnp/control/WANIPConn1"
    headers = {'soapaction': 'urn:schemas-upnp-org:service:WANIPConnection:1#ForceTermination', 'Authorization': method_modern, 'content-type': 'text/xml','charset': 'utf-8'}
    body = """<?xml version='1.0' encoding='utf-8'?><s:Envelope s:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/' xmlns:s='http://schemas.xmlsoap.org/soap/envelope/'><s:Body><u:ForceTermination xmlns:u='urn:schemas-upnp-org:service:WANIPConnection:1' /></s:Body></s:Envelope>"""
    boxdata = requests.post(url,data=body,headers=headers).content.decode('utf-8')
    print(boxdata)

main()
