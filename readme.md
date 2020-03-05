# dinglingling
dinglingling, your program is over!
The code references https://github.com/light8lee/dingdong. The web weChat now is not work, so I refact the code by the [Server Chan](http://sc.ftqq.com/3.version).

## Requirements
- python >= 3.6

## Installation
```bash
git clone git@github.com:light8lee/dingdong.git
python setup.py install
```

## Usage
Just like the examples in test.py, you need to add the decorator ahead of your function:
```python
from dinglingling import wx_reminder

SCKEY = "" # the sckey you get from http://sc.ftqq.com/3.version
proxy = "" # if you needn't proxy, ignore it.

# remind_started: if you need remind you when the function 
# stated, make remind_started = True

@wx_reminder(SCKEY=SCKEY, proxy=proxy, remind_started=False)
def test_correct_func():
    print("hello world")
```

## Thanks
- [ServerChan](http://sc.ftqq.com/3.version)
- [light8lee](https://github.com/light8lee)
