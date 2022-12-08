### Update: I did this program when I was still not very experienced on computer security ( even now I’m not an expert ) , it was created only as a leisure and I do not recommend using it for projects where you need serious security system.

# JUC
JUC is a simple Unicode based text crypter

### **NOTE: This project was *not* created to be used in other projects, but only to be able to read the code and understand its operation, it is strongly discouraged to use JUC in important security systems**


note: *You can find all the examples in the folder `examples`*


# Installation
You can find the project on [PyPi](https://pypi.org/project/JUC/).
To install it execute this command in the cmd
```yaml
pip install JUC
```

# Preview
> ### File Encrypter
> ![Gif Video](./assets/ImageCrypter.gif)
> ### Original and decrypted file differences
> ![Differences](./assets/fileSize.PNG)
> The quality of the original file and the decrypted file is equal :)
> 
> ### Text Crypter
> ![TextCrypter](./assets/TextCrypter.png)

# Examples

> ### Encrypting a text
> ```py
> from JUC import *
> worker = Juc('YourSecretKey')
> print(worker.crypt(b'ehy, hello there'))
> ```
> ### Decrypting a text
> ```py
> from JUC import *
> worker = Juc('YourSecretKey')
> print(worker.decrypt(text).decode())
> ```


> ### Encrypting a file
> ```py
> from JUC import *
> 
> worker = Juc('YourSecretKey')
> 
> filePath = 'image.png'
> 
> with open(f'result.png', 'wb') as f:
>     with open(filePath, 'rb') as file:
>         content = file.read()
>         crypted = worker.crypt(content)
>         f.write(crypted.encode())
> ```
> ### Decrypting a file
> ```py
> from JUC import *
> 
> worker = Juc('YourSecretKey')
> 
> filePath = 'result.png'
> fileType = filePath.split('.')[-1]
> 
> with open(filePath, 'r') as file:
>     content = file.read()
>     with open(f'result-decrypted.{fileType}', 'wb') as f:
>         decrypted = worker.decrypt(content, False)
>         f.write(decrypted)
> ```
