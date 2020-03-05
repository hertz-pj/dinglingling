from dinglingling import wx_reminder

SCKEY = "SCU88001Tf72ede214b2df11a6bde4c3a68c0f26c5e60b2b6f3f5e"
proxy = "http://10.249.148.139:7890"

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