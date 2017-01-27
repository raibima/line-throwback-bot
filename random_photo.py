from os import listdir, environ
from random import choice

def random_photo():
  return environ[HOSTNAME] + 'static/img/' + choice(listdir('static/img'))
  
if __name__ == '__main__':
  print random_photo()
