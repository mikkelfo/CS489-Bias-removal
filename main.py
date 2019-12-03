from PDF import Reader


file = 'test/bias.pdf'
reader = Reader.ReadFile()
x = reader.read(file)
print(x)



