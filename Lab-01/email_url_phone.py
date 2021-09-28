import re

class Tokeniser:
  def __init__(self, data):
    self.data = data
    self.email_regex = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    self.url_regex = '(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    self.phone_regex = '(\+\d{1,3}\s?)?((\(\d{3}\)\s?)|(\d{3})(\s|-?))(\d{3}(\s|-?))(\d{4})(\s?(([E|e]xt[:|.|]?)|x|X)(\s?\d+))?'

    self.tokens = []

    self.extract_email()
    self.extract_url()
    self.extract_phone()

  def extract_email(self):
    matches = re.finditer(self.email_regex, self.data)

    for match in matches:
      self.tokens.append((match.start(), match.end() - match.start(), match.group()))

  def extract_url(self):
    matches = re.finditer(self.url_regex, self.data)

    for match in matches:
      self.tokens.append((match.start(), match.end() - match.start(), match.group()))

  def extract_phone(self):
    matches = re.finditer(self.phone_regex, self.data)

    for match in matches:
      self.tokens.append((match.start(), match.end() - match.start(), match.group()))

def main():
  with open('dummy.txt', 'r') as f:
    data = f.read()

    tokens = Tokeniser(data)

    for token in tokens.tokens:
      print(token)

if __name__ == '__main__':
  main()
