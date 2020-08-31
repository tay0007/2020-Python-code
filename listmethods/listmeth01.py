#!/usr/bin/env python
proto = ["ssh", "http", "https"]
print(proto)
print(proto[1])
proto.extend("dns") # this line will add d, n, and s
print(proto)
