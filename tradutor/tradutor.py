from translate import translate

s = translate.Translator(to_lang='en', from_lang='pt')
while True:
    res = s.translate(input('>>>: '))
    print(res)