# zip-cracker
no-nonsense zip bruteforcer, made this because I can't find a working one that is exactly as I wanted. This will not be actively maintained nor checked, But feel free to put an issue if you have a problem with it, cheers!

## Known issues
- "kCe" will generate an error `zlib.error: Error -3 while decompressing data: invalid distance too far back`

## How to use
This script is basically a working core of a zip extractor, But incase any complete beginners or people that are not used to python are here, 

- you basically just install `python`, and run this on cmd
```pip install pyzipper```

- Open the script, You will see something like this:
![image](https://github.com/Not-Baguette/zip-cracker/assets/94969176/9146b93e-a4c4-43b6-a82b-f314ca09532e)

- Just add the path to your file location on to `zip_file_path`, i.e. `"D:\\Test\\something.zip"`

- Add the extraction path to `extraction_path`, this is the path where you want to see the decrypted files at, so I reccomend putting it on close proximity with your file location, like `"D:\\Test\\"`

- Save the file and run the code, it'll show you every attempt and what password will work

## Prerequisites
- pyzipper
