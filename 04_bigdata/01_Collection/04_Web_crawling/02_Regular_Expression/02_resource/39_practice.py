import re


def five_long(sub_str):
    p = re.compile(r' {2}', re.MULTILINE)
    s = p.sub('', sub_str)
    if s:
        return s
    return None


sample_string ='I  think  it  is  good  idea  to  go  there'
print(five_long(sample_string))
