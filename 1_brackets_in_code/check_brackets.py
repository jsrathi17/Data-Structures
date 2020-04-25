
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opstack = []
    for i, next in enumerate(text):
        if next in "([{":
            opstack.append(Bracket(next,i))
            pass

        elif next in ")]}":
            if not opstack:
                return i+1
            else:
                top = opstack.pop()
                if not are_matching(top.char,next):
                    return i+1

    if opstack:
        top = opstack.pop()
        return top.position+1
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
