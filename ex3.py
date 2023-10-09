from functools import wraps
import logging
from datetime import datetime


def logger(path):
  
  def __logger(old_function):
    @wraps(old_function)

    def new_function(*args, **kwargs):
      date_time = datetime.now()
      name = old_function.__name__
      result = old_function(*args, **kwargs)
      logging.basicConfig(filename = path,
                          # filemode='w',
                          level = logging.DEBUG,
                          force=True)
      logging.info(f'{date_time}, {name}, {args}, {kwargs}, {result}')
      # return result
    
    return new_function

  return __logger


class FlatIterator:

  def __init__(self, list_of_list):
    self.list_of_list = list_of_list

  def __iter__(self):
    self.count = 0
    self.count_l = -1
    self.list_of_list[self.count]
    return self

  def __next__(self):
    if self.count_l < (len(self.list_of_list[self.count])-1):
      self.count_l += 1
    else:
      self.count_l = 0
      if self.count == (len(self.list_of_list)-1):
        raise StopIteration
      else:
        self.count += 1
    return self.list_of_list[self.count][self.count_l]


@logger('log_4.log')
def test_3():

  list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
  ]

  return [item for item in FlatIterator(list_of_lists_1)]
