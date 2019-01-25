import hashlib


def generator(path):
    with open(path, encoding='utf8') as file:
        for line in file:
            yield hashlib.md5(line.rstrip().encode('utf-8'))


my_generator = generator('result.txt')
for i in my_generator:
    print(i.hexdigest())


