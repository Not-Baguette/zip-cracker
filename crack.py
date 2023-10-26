import pyzipper
import itertools
from string import ascii_letters, digits, punctuation

def brute_force_zip(zip_file_path, min_password_length, max_password_length, extraction_path):
    with pyzipper.AESZipFile(zip_file_path) as zf:
        for password_length in range(min_password_length, max_password_length + 1):
            for password in itertools.product(ascii_letters + digits, repeat=password_length): # "+ punctuation" after digits to include punctuation
                password_str = ''.join(password)
                try:
                    zf.pwd = password_str.encode('utf-8')
                    zf.extractall(path=extraction_path)
                    print(f"Password found: {password_str}")
                    return password_str
                except RuntimeError:
                    print(f"Attempt Fail: {password_str}")
                    continue
                except Exception as e:
                    print(f"Error for: {password_str}, Error: {e}")
                    continue

    print("Password not found")

zip_file_path = ""
extraction_path = ""
brute_force_zip(zip_file_path, min_password_length=5 , max_password_length=8)
