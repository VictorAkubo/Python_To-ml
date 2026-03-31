def my_decorator(func):
  def wrapper():
    print("hi before deco")
    func()
    print("hi after deco")
  return wrapper

@my_decorator
def hello():
  print("hello")

hello()