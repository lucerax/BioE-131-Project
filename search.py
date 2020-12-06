import sys

infile = sys.argv[1]
ref = sys.argv[2]
if len(sys.argv) == 4:
    outfile = sys.argv[3]


def find_str(s, char):
    result = []
    index = 0
    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    result.append(index)

            index += 1

    return result

with open(infile, 'r') as input:
    line = input.read().replace("\n", " ")
    print(find_str(line, ref))
