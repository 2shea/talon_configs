from talon.engine import engine


def listener(topic, m):
    if topic == "cmd" and m["cmd"]["cmd"] == "g.load" and m["success"] == True:
        print("[grammar reloaded]")
    else:
        try:
            if m["cmd"]["list"] == "homophones.all":
                m["cmd"]["items"] = len(m["cmd"]["items"])
                print(topic, m)
        except:
            print(topic, m)


engine.register("", listener)
