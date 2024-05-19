# fritzbox-soap-python-json
Using python 3 to send SOAP requests and get JSON formatted replies.

## The poor man's "SOAP" request
Regards to everyone else using plain vanilla python 3 and not further losing their minds. This works with UPnP in restricted rights setting. You don't need your FB's username nor password.

```
ran@odroidxu4:~$ chmod +x soapless-soap.py
ran@odroidxu4:~$ ./traffic-soap.py
['442.044', '58.469', '8', '0']
```
Values for total download, upload in GiB and current download and upload in Mbit/s. To be used with wireless displays or rrdtool scripts as in my other projects.

```
ran@odroidxu4:~ $ ./soap-ip.py
123.132.213.231
```

You can even do fully authorized SOAP requests now! This example prints your external IP.

## Traffic monitor RRDtool example
```
rrdtool create traffic.rrd --step 60 DS:download:GAUGE:600:U:U DS:upload:GAUGE:600:U:U RRA:MAX:0.5:1:1080
```
![alt text](https://raw.githubusercontent.com/ran-sama/fritzbox-soapless-soap-requests/master/images/dl_example.png
)
![alt text](https://raw.githubusercontent.com/ran-sama/fritzbox-soapless-soap-requests/master/images/ul_example.png
)

## Docs  
https://avm.de/service/schnittstellen/  
https://avm.de/fileadmin/user_upload/Global/Service/Schnittstellen/IGD2.pdf  
https://avm.de/fileadmin/user_upload/Global/Service/Schnittstellen/AVM_TR-064_first_steps.pdf  

## License
Licensed under the WTFPL license.
