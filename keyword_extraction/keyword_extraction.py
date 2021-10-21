# Sinh vien thuc hien: Tran Hoang Quan (19120338)
# Tai lieu tham khao:
#    - Command line arguments on Python:
#       - https://www.tutorialspoint.com/python/python_command_line_arguments.htm
#    - Bo stopwords tieng Viet:
#       - https://github.com/stopwords/vietnamese-stopwords
#    - Code mau LSA tham khao cua thay Luong An Vinh
#    - Bai bao goc:
#       - https://tuoitre.vn/bo-y-te-du-kien-thang-10-bat-dau-tiem-vac-xin-cho-tre-tu-12-17-tuoi-20211009094118891.htm

import sys, getopt
from vi_LSA import LSA

def main(argv):
    input_file, output_file = '', ''
    try:
        opts, args = getopt.getopt(argv, 'hi:o:', ['input_file=', 'result='])
    except getopt.GetoptError:
        print('Command line arguments invalid, try again.')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '--input_file':
            input_file = arg
        elif opt == '--result':
            output_file = arg

    if (input_file == '' or output_file == ''):
        print('Missing arguments, please try again.')
        sys.exit(2)

    try:
        with open(input_file, mode = 'r+', encoding = 'utf8') as f:
            texts = f.read()

        extracted = LSA(texts).extract()
        terms, components = extracted[0], extracted[1]

        with open(output_file, mode = 'w+', encoding = 'utf8') as f:
            for i, comp in enumerate(components):
                terms_comp = zip(terms, comp)

                sorted_terms = sorted(terms_comp, key = lambda x:x[1], reverse = True)[:7]

                f.write('Topic {0}:\n'.format(i))
                for term in sorted_terms:
                    f.write(term[0] + ' ')
                f.write('\n')

        print('Results are printed to', output_file)
    except FileNotFoundError:
        print('Input file does not exist.')
        sys.exit(2)


if __name__ == '__main__':
    main(sys.argv[1:])
