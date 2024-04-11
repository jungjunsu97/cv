import itertools
import zipfile

def crack_zip_password(zipfilename, digits=True, letters=True, max_length=9):

   chars = ""
   if digits:
      chars += "0123456789"
   if letters:
      chars += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
   passwords = itertools.chain.from_iterable(
      itertools.product(chars, repeat=i) for i in range(1, max_length + 1)
   )

   with zipfile.ZipFile(zipfilename) as zf:
      for password in passwords:
          password = "".join(password)
          print(password)
          try:
             zf.extractall(pwd=password.encode())
             return password
          except:
             pass
          
   return None
password = crack_zip_password(r"폴더명\암호.zip", digits=True, letters=True, max_length=9)
print("비밀번호는:",password)       