import pandas

major, minor, micro = pandas.version_info[:3]
print(print(f"Your Python version is {major}.{minor}.{micro}"))