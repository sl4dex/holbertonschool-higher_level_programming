#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    s = dir(hidden_4)
    for i in range(len(dir(hidden_4))):
        if s[i][:2] != "__":
            print(s[i])
