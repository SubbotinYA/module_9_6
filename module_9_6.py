def  all_variants(text:str)->str:
    for x in range(0,len(text)):
        yield text[x]
    for y in range(1, len(text)):
        yield text[y-1] + text[y]
    yield text

a = all_variants("abc")
for i in a:
    print(i)