# fritzbox-vanilla-soap-requests
Using vanilla python 3 to not get your hands dirty doing SOAP requests. As in no external libraries needed.

## The poor man's "SOAP" request
Regards to everyone else using plain vanilla python 3 and not further losing their minds. This works with UPnP in restricted rights setting. You don't need your FB's username nor password.

```
ran@odroidxu4:~$ chmod +x soapless-soap.py
ran@odroidxu4:~$ ./soapless-soap.py
['442.044', '58.469', '8', '0']
```
Values for total download, upload in GiB and current download and upload in Mbit/s. To be used with wireless displays or rrdtool scripts as in my other projects.

```
ran@odroidxu4:~ $ ./full-sid-authorization.py
Bearer a3cddb40a8fa1970
Basic ZnJpdHoxMjM0OmZveDc4OTA=
123.132.213.231
```

You can even do fully authorized SOAP requests now!

## Traffic monitor RRDtool example
```
rrdtool create traffic.rrd --step 60 DS:download:GAUGE:600:U:U DS:upload:GAUGE:600:U:U RRA:MAX:0.5:1:1080
```
![alt text](https://raw.githubusercontent.com/ran-sama/fritzbox-soapless-soap-requests/master/images/dl_example.png
)
![alt text](https://raw.githubusercontent.com/ran-sama/fritzbox-soapless-soap-requests/master/images/ul_example.png
)

## Docs  
https://avm.de/fileadmin/user_upload/Global/Service/Schnittstellen/IGD2.pdf  

## License
Licensed under the WTFPL license.
