# Introduction

**Note:** I'm continuing to update these docs. Keep checking back.

## What is EZIoT.link?

The `eziot.link` website and application is an online location that IoT developers and hobbyist can use to post data from their IoT devices. The posted data can then be downloaded and used by other IoT devices or desktop applications. 

The Python file `eziot.py` is a script that can be run with both **Python3** and **MicroPython**. It functions as a Software Development Kit or **SDK** that allows the user to easily interact with the Application Programming Interface or **API** on the `eziot.link` website.

By adding the SDK to MicroPython-based projects and devices, users can easily swap data between devices and desktop applications. The `eziot.link` website is basically a cloud data platform where you can drop off your data package so that it can be picked up later by your other devices. 

![EZIoT.link Illustration](https://eziot.link/images/eziot_illustration_1.png)

## What Can I Do?

The `eziot.py` SDK in combination with the `eziot.link` API will allow you to upload data from anywhere with an internet connection and use it anywhere else with an internet connection. Here are some of the specific things you can do:

1. **Upload Data** - You can upload up to **1024** rows of data. For each row of data you can include **6** items or values: `[group,device,data1,data2,data3,data4]`. The first 5 values can be strings (i.e. text), integers, or floats. If the value is a string, it can be up to **32** characters long. The `data4` value is the same, except that if it is a string, it can be **256** characters long. If you load more than 1024 rows, the oldest row will be dropped from the data and the new row will be added. Also, the `eziot.link` API will add a time stamp, an id number, and an IP address to the row, so you don't need to worry about those.

1. **Download Data** - Once you have some data, you can easily get it back. You can request 1 to 1024 rows, and you can select on `group` and `device`. So it you want to get the most recent row for the `command` group and the `FunBoard1` device, no problem. If you need to do something fancy, just grab all your rows and do what you need.

1. **Delete Data** - It's your data. You can delete any row, or any row older than a given row, or all of it. Whatever you need. I don't care. I don't want it.

1. **Pass Data Between Devices** - You can easily send commands to devices and pass data between devices by using the `group` and `device` values. Just post data using a specific group and device, and then the target device can get that data using the same group and device. Easy.

## What Can't I Do?

The `eziot.link` API is designed to simply meet a primary need of developers and hobbyists: an interim place to post and get data. 
It will probably handle 90% of IoT applications. But just to be clear, here are some of the things you shouldn't expect from `eziot.link`:

1. **Unlimited Data** - Nope. This is a place to post data so you can get it and use it some other place, not save it forever. You get 1024 rows to work with. If you need to save all data forever, then periodically download it to your desktop.

1. **Huge Data** - Nope. You only get 6 fields to post data, and only one allows a long string. So, you can post temperature, humidity, readings, counts, status, et cetera, and if you need you can put some JSON into the `data4` field. That's mainly what IoT needs to do. And don't forget that the `eziot.link` API will add those extras items (timestamps, ip address, id numbers).

1. **User Support** - Not really. It's a super-simple, basically-free, service. It's also tested and known to work if used as intended. It's being used everyday by people all over the place. If you're having trouble, the best thing is to read the docs again. Or you can check my [Patreon](https://www.patreon.com/claytondarwin) account and send me a message. 

## What About Privacy and Security?

1. The `eziot.link` website and API is not interested in collecting your data. Your data is intended to be transient and exists in only one location, and when you delete it, or if it gets dropped off the bottom of the stack, then it's gone forever. Don't ask about recovering it because it can't be done. There are no backups. Anything that needs to be maintained should be downloaded to your desktop soon after it is posted.

1. The `eziot.link` website and API DOES collect data necessary to maintain a web server. Access logs (which include IP addresses) are maintained for about a week. We also, of course, keep the email address you used to create an account for the period that the account exists (until you delete it).

1. The `eziot.link` website and API **SHOULD NOT** be used to host any data that is critical to commercial, medical, government, or military systems or infrastructure. This is an experimental site/application designed for developers and hobbyists. There is no guarantee of permanence for data or application. Both may be removed at any time.

1. The `eziot.link` website and API **SHOULD NOT** be used to host any data that is personal or private in nature. We use encryption on the front end, but not on the back end. That is, your data is encrypted when transmitted over the internet (if you are using HTTPS), but it is not stored in an encrypted format. Please keep this in mind.

# EZIoT SDK Documentation

## A Video to Get Started

To be added soon.

## No Installation

### Python Versions

**Python:** Developed on 3.8. Should work on 3.5+.

**MicroPython:** Developed on 1.13. Should work on 1.10+.

### Setup Requirements

The EZIoT.link SDK script itself does not need installation. Simply copy/load it to a location in your Python or MicroPython `import` path list (see `sys.path`).

The SDK uses the `requests` or `urequests` module to send and receive data. This is included with most current versions of Python and Micropython.

## Test Run

The EZIoT.link API has a default user account that everyone can use for testing. 
The SDK comes set up to use the default account.
Here are some simple examples you can try using your desktop or the MicroPython REPL:

```python
# assuming you have Python open and eziot.py on the import path
>>> import eziot # import module

>>> eziot.post_data('my_group','my_device','hello from me') # post data group, device, and data1
2 # this is the rowid of the post

>>> for x in range(3):
... eziot.post_data('my_group','my_device','hello from me',x) # also posting to x to data2
... 
3 # rowid
4 # rowid
5 # rowid

>>> for x in eziot.get_data(10): # ask for last 10 rows (only 5 exist)
... print(x)
... 
[5, 1615761740, '2021-03-14 22:42:20', '67.140.214.0', 'my_group', 'my_device', 'hello from me', 2, None, None]
[4, 1615761740, '2021-03-14 22:42:20', '67.140.214.0', 'my_group', 'my_device', 'hello from me', 1, None, None]
[3, 1615761739, '2021-03-14 22:42:19', '67.140.214.0', 'my_group', 'my_device', 'hello from me', 0, None, None]
[2, 1615761700, '2021-03-14 22:41:40', '67.140.214.0', 'my_group', 'my_device', 'hello from me', None, None, None]
[1, 1615761087, '2021-03-14 22:31:27', '67.140.214.0', 'clayton', 'example', 'hello', 'this is rowid 1', 1, 'you cannot delete this']

>>> eziot.stats() # get stats for data
{'size': 8192, 'rows': 5, 'min_rowid': 1, 'max_rowid': 5, 'max_rows': 1024, 'max_rate': 2.0, 'email': 'example@eziot.link'}

>>> eziot.delete_data(rowids=[4,2]) # delete rows 4 and 2
2

>>> for x in eziot.get_data(10): # ask for last 10 rows (now only 3 exist)
... print(x)
... 
[5, 1615761740, '2021-03-14 22:42:20', '67.140.214.0', 'my_group', 'my_device', 'hello from me', 2, None, None]
[3, 1615761739, '2021-03-14 22:42:19', '67.140.214.0', 'my_group', 'my_device', 'hello from me', 0, None, None]
[1, 1615761087, '2021-03-14 22:31:27', '67.140.214.0', 'clayton', 'example', 'hello', 'this is rowid 1', 1, 'you cannot delete this']

>>> 
```
## Getting an Account

The example account is good for testing, but it mixes the data from everyone that may be using it. So you will probably want get an account of your own. This is done using the SDK.

Start by opening a Python or MicroPython REPL prompt, then do the following:
```python
# assuming you have Python open and eziot.py on the import path
>>> import eziot
>>> eziot.get_creds()
What is your email address?> 
```
At this point just do what you are asked. You have to agree with some stuff, and then a validation code will be sent to your email. Once you enter your validation code (copy and paste), your new user credentials will be sent to your email. This will give you a `key`, a `secret`, and a `version`. They should be in a format that lets you copy and paste them straight into your start script.

**IMPORTANT:** Keep your key and secret a secret. If anybody else knows them, they can manipulate your account just as you can. They can even delete it and all your data.

Once you have your credentials, add them to your start script like this:
```python
import eziot

eziot.api_key = MYKEY123456789AB
eziot.api_secret = MYSECRET12345678
eziot.api_version = 1.0

# now you're ready
# connect to wifi
# post some data or whatever

```

## Functions
The SDK only has a few common commands, plus a few odd extras for convenience.

### Rate Limits

It is important to remember that the EZIoT.link API rate limits each account. Basically, you want to try and keep your posts and gets to about **1 request per second**. 
There are so-called "burst" limits in case you have several devices trying to post data at one time, but the target for your account should be less than is 1 per second. For devices like an ESP32, this isn't a problem because a request will take more than a second, but you can easily exceed this on a desktop or IoT device with a fast processor.

There are also rate limits on account options, like resetting or resending your credentials.

If you exceed your limit, the API won't complete your request and the SDK will raise an error.

### ROWIDs

Every data row has an associated `rowid` which can be used to select the row for return or deletion. The rowids start at 1 and are augmented such that a new rowid will be 1 higher than the highest rowid in the data. Rowids can recycle in two cases: 1) if any number of most-recent rows are deleted, and 2) if all rows are deleted (starts again with 1).

### Posting Data

**Best Practice:** Only post what is needed. Don't hog bandwidth and server space posting useless information.

`eziot.post_data(group=None,device=None,data1=None,data2=None,data3=None,data4=None)`

Post the given data to your data as a row. Return the rowid of the newly-created row. You can include all or none of the variables. If no variables are given, the API will add a row with with a current timestamp and IP from the device making the post.

- group: should be a STRING with a max length of 32 characters. if an INTEGER or FLOAT is given, it will be coerced to a string.
- device: should be a STRING with a max length of 32 characters. if an INTEGER or FLOAT is given, it will be coerced to a string.
- data1-3: can be an INTEGER, a FLOAT, or a STRING with a max length of 32 characters.
- data4: can be an INTEGER, a FLOAT, or a STRING with a max length of 256 characters. use this for JSON-type data.

### Getting Data

**Best Practice:** Only download the rows your need. Use rowids to limit your downloads and not re-download.

`eziot.get_data(count=1,after=None,group=None,device=None)`

Return a list of data rows (also lists). The default is to return the last row added.

**IMPORTANT:** The API will easily return all 1024 rows, even if they have the maximum allotted data in each row. However, an **ESP32** or similar device cannot handle that much data. It will exceed the memory capacity. Use count, after, group, and device to limit the returns to a size your device can handle. Also see the `watch()` function below.

- count: an INTEGER number of rows to return (if available). set to 0 for no limit.
- after: a INTEGER rowid, return all rows posted after this rowid (not including it). ~~takes precedence over count.~~
- group: a STRING. limit returned rows to those where the group field exactly matches this string.
- device: a STRING. limit returned rows to those where the device field exactly matches this string.
- NOTs: the `group` and `device` string values can be preceded by `"not:"` to match all values except the string that follows.
- WILDs: the `group` and `device` string values can contain the wildcard `"%"` to match any series of characters.
- examples: `group="funboard1"`, `group="funboard2"`, `group="funboard%"`, `group="not:funboard%"`

return = `[[rowid,epoch,gmt,ip,group,device,data1,data2,data3,data4],...]`

The returned list of rows is ordered most-recent-first (descending by rowid + epoch).

- rowid: the data row id number (can be used to select or delete)
- epoch: an integer representing the epoch time when the row was created
- gmt: a GMT timestamp based on the epoch time
- ip: the IP address of the device that posted the data
- group,device,data1-4: see the description above in `eziot.post_data`

`eziot.watch(startrows=10,update=10,group=None,device=None)`

This meta function uses `get_data` and the `after` variable to efficiently watch for new rows added to the data. Once called it will loop indefinitely and print new rows to the screen.

- startrows: an INTEGER number of rows to start the printout. default is 10.
- update: an INTEGER or FLOAT number of seconds between `get_data` requests. default is 10.
- group|device: see the description above in `eziot.post_data`

### Deleting Data

**IMPORTANT:** Deletions are permanent. There is no recovery.

`eziot.delete_data(rowids=[],before=None,xall=False)`

Delete rows and return the number of rows deleted.

- rowids: a single INTEGER or a list of INTEGERs. the rowids to delete (if they exist).
- before: an INTEGER rowid. delete all rows before this row (not including it). takes precedence over rowids.
- xall: boolean. if not `False`, delete all rows.

### Getting Stats

`eziot.stats()`

Return a dictionary of stats related to the data.

return = `{'rows':5,
'min_rowid':1,
'max_rowid':5,
'max_rows':1024,
'max_rate':1.0,
'email':'example@eziot.link',
'size':8192
}`

- rows: an INTEGER. current number of rows in the data.
- min/max_rowid: INTEGER. the current lowest/highest rowid in the data. 
- max_rows: an INTEGER. the maximum rows a user can add before the oldest rows begin to be removed from the stack.
- max_rate: an INTEGER. the target maximum request rate per second for the given user.
- email: a STRING. the email address associated with the data account.
- size: an INTEGER. the size-on-disk of the data in bytes (this may be removed in the future)

### Wifi Connections

The SDK includes several MicroPython WiFi functions as a convenience:

`eziot.wifi_scan()`

Scan for available WiFi access points. Print a list of APs.

print = `Network AP: [ssid,bssid,channel,RSSI,authmode,hidden]` per AP

`eziot.wifi_connect(essid,essid_password)`

Connect to the given AP using the `essid` and `essid_password`. The `essid_password` can be `None` if no password is required.

`eziot.wifi_disconnect()`

Self explanatory.

### Getting Credentials

See "Getting an Account" above.

### Deleting Credentials/Account

**IMPORTANT:** If you delete your credentials, everything on the server will be lost. All data, all knowledge that you ever had an account.

`eziot.delete_creds()`

You will be prompted. If you indicate yes, say bye-bye to everything.

## Tips and Tricks

### Get All Rows

The `after` variable takes precedence over the `count` variable. Set `after=0` to get all rows after rowid 0 (which doesn't exist). This will get all rows.

`eziot.get_data(1,0)` == `eziot.get_data(count=1,after=0,xall=False)`

### JSON for Data Objects

The `json` module, which supports the JSON (JavaScript Object Notation) data format, allows you to take Python objects like `list` and `dict` and convert them to a string format that you can store in `data4` (or another field if it is short). You can then use the module to convert the string back into a Python object. 

```python
# assuming your are already connected

import json

data = {'cat':'aloof','dog':'dirty','frog':'wet'} # make some data

jdata = json.dumps(data) # convert or "dump" the object to a json-formatted string

rowid = eziot.post('testing','funboard1',data4=jdata) # post to data4

for row in eziot.get_data(after=rowid-1,group='testing',device='funboard1'):
    if row[0] == rowid: # match rowid
        jdata = row[-1] # get data4 (last item in row)
        data = json.loads(jdata) # convert or "load" the json string back to a python object
        print(data)
        break

```

### Sending Commands

Because the EZIoT.link SDK is a simple way to post and get data, it can easily be used to pass data between devices. This can be used to send commands to devices.

For example, if you have a FunBoard and you want it to turn its neopixels red, from your desktop you can create a post similar to this:

`rowid = eziot.post_data('command','FunBoard_1','neopixels','red')`

The FunBoard needs to be running a loop that has a requests to get commands directed at it.
When it sees the command come through, it should set the neopixels and then delete the command.

```python
# this is rudimentary, you need wait periods and try-except catches etc.

rows = eziot.get_data(1024,group='command',device='FunBoard_1')

for rowid,epoch,gmt,group,device,data1,data2,data3 in rows:
do_command(data1,data2)
eziot.delete_data(rowid)
```

If you wanted, you could have it send back a response that indicating it did as it was told:

`rowid = eziot.post_data('response','FunBoard_1','neopixels','red','okay')`

You could read this from your desktop.


