class CustomError(Exception):
  def __init__(self,message,code):
    super().__init__(message,code)
    self.code = code


try:
  if 4<5:
    raise CustomError("the condition is false",200)
  else:
    print("4 isnt")
  
except CustomError as e:
  print(f"caught an exception: {e}")