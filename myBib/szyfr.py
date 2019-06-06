def znajdz (text):
    s= list(text)
    p=text.find('a')
    s[p]= 'z'
    print(s)

znajdz('asdr')

