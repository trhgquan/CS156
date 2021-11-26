import joblib, getopt, sys
from underthesea import word_tokenize

# Tiền xử lý: loại bỏ các dấu , . ! ?,
# loại bỏ dấu cách thừa và chuyển string về dạng lowercase.
def preprocess(sentence):
    sentence = sentence.strip()
    sentence = sentence.replace(',', '')
    sentence = sentence.replace('.', '')
    sentence = sentence.replace('?', '')
    sentence = sentence.replace('!', '')
    sentence = sentence.replace('"', '')
    sentence = sentence.replace('  ', ' ')

    specials_ = {
        ':)' : 'colonsmile',
        ':(' : 'colonsad',
        '@@' : 'colonsurprise',
        '<3' : 'colonlove',
        ':d' : 'colonsmilesmile',
        ':3' : 'coloncontemn',
        ':v' : 'colonbigsmile',
        ':_' : 'coloncc',
        ':p' : 'colonsmallsmile',
        '>>' : 'coloncolon',
        ':">' : 'colonlovelove',
        '^^' : 'colonhihi',
        ':' : 'doubledot',
        ":'(" : 'colonsadcolon',
        ':’(' : 'colonsadcolon',
        ':@' : 'colondoublesurprise',
        'v.v' : 'vdotv',
        '...' : 'dotdotdot',
        '/' : 'fraction',
        'c#' : 'cshrap',
    }

    for key in specials_.keys():
        sentence = sentence.replace(key, specials_[key])
    return sentence.lower().strip()

def tokenize(sentence):
    return word_tokenize(sentence, format = 'word')

def main(argv):
    input, output_file = '', ''
    try:
        opts, args = getopt.getopt(argv, 'hi:o:', ['input=', 'result='])
    except getopt.GetoptError:
        print('Command line arguments invalid, try again.')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '--input':
            input = arg
        elif opt == '--result':
            output_file = arg

    if (input == '' or output_file == ''):
        print('Missing arguments, please try again.')
        sys.exit(2)

    stopwords = []
    with open('stopwords.txt', 'r+', encoding = 'utf-8') as f:
        for line in f:
            stopwords.append(line.strip())

    try:
        model_ = joblib.load('sentiment.joblib')
        vectorizer_ = joblib.load('vectorizer.joblib')

        with open(output_file, 'w+') as f:
            predict_ = model_.predict(vectorizer_.transform([preprocess(input)]))
            print(predict_[0], file = f)

        print('Successfully printed to {0}'.format(output_file))
    except:
        print('Model not found, have you tried running training inside danh_gia_mon_hoc_bayes.ipynb yet?')

if __name__ == '__main__':
    main(sys.argv[1:]);
