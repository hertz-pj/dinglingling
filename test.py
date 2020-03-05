from dinglingling import wx_reminder

SCKEY = "" # the sckey you get from http://sc.ftqq.com/3.version
proxy = "" # if you needn't proxy, ignore it.

@wx_reminder(SCKEY=SCKEY, proxy=proxy, remind_started=True)
def test_correct_func():
    print("hello world")

@wx_reminder(SCKEY=SCKEY, proxy=proxy)
def test_error():
    raise Exception("test error")


if __name__ == "__main__":
    test_correct_func()
    # test_error()
    pass