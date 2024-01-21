f = open("python.txt")
print(f.read())
print(f.read(1))
print(f.read(-1))

def word_count(f):
    with open("python.txt", 'r') as file:
        data = file.read().replace('\n', '')
        words = data.split(' ')
        return len(words)

word_count = word_count(f)

if word_count is not None:
    print(f"The number of words in the file {f} is {word_count}.")

def read_last_n_lines(f, n):
    with open("python.txt", 'r') as file:
        lines = file.readlines()
    last_n_lines = lines[-n:]
    for line in last_n_lines:
        print(line, end='')
n = 5

read_last_n_lines(f, n)