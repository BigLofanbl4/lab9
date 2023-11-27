# !/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "bob"
    }

    new = {val: key for key, val in a.items()}
    print(new)