# fritzbox-soapless-soap-requests
Using vanilla python 3 to not get your hands dirty doing SOAP requests. As in no external libraries needed.

## Are you a sane person?
Use this instead and thank me later:  
https://github.com/kbr/fritzconnection  

## Using the poor man's "SOAP" request
Regards to everyone else using plain vanilla python 3 and not further losing their minds. This works with UPnP in restricted rights setting. You don't need your FB's username nor password.

```
ran@odroidxu4:~$ chmod +x soapless-soap.py
ran@odroidxu4:~$ ./soapless-soap.py
['442.044', '58.469', '8', '0']
```
Values for total download, upload in GiB and current download and upload in Mbit/s. To be used with wireless displays or rrdtool scripts as in my other projects.

## Traffic monitor RRDtool example

![alt text](https://raw.githubusercontent.com/ran-sama/fritzbox-soapless-soap-requests/master/images/dl_example.png
)
![alt text](https://raw.githubusercontent.com/ran-sama/fritzbox-soapless-soap-requests/master/images/ul_example.png
)

## License
Licensed under the WTFPL license.
