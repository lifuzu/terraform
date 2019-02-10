''' example for practising terraform external data source configuration '''
import json
import sys


class MyCustomizedException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
    def __str__(self):
        return repr(str(self.code) + ": " + self.message)


def main(opts= None):
# def main(opts: dict = None) -> dict:
    '''The main routine'''

    retval = {}
    retval.update(opts)
    retval.update({"abc": "123abc"})

    # when there is an exception
    raise MyCustomizedException(10, "STDERR on something")

    return retval


if __name__ == "__main__":
    args = json.load(sys.stdin)

    try:
        retval = main(args)
    except MyCustomizedException as e:
        print(e)
    else:
        print(json.dumps(retval))
    finally:
        sys.exit(e.code if e else 0)
