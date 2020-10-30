import regex
import argparse
import csv


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_file', help='input file')
    parser.add_argument('-r', '--ruby_list_file', help='ruby list file')
    return parser.parse_args()


def find_ruby_from_line(line):
    p = regex.compile(r'(\p{Script=Han}+)(\(|（)(.*?)(\)|）)')
    result = p.findall(line)
    ruby_list = []
    for tup in result:
        ruby_list.append([tup[0], tup[2]])
    print(ruby_list)
    return ruby_list


if __name__ == "__main__":
    args = parse()
    rblist = []
    with open(args.input_file, 'r') as f:
        lines_list = f.readlines()
    for line in lines_list:
        rb = find_ruby_from_line(line)
        if rb:
            rblist.extend(rb)
    rblist = sorted(rblist, key=lambda t: t[0])
    print(rblist)

    with open(args.ruby_list_file, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(rblist)
