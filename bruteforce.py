import zipfile

charlist = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' #ALPHANUMERICAL ONLY (CAN ADD MORE)
complete = []

for current in range(4): #MAX PASSWORD LENGTH = 4
    a = [i for i in charlist]
    for x in range(current):
        a = [y + i for i in charlist for y in a]
    complete = complete + a

z = zipfile.ZipFile('filename') #INPUT THE NAME OF YOUR ZIP FILE (MUST BE IN SAME DIRECTORY)

tries = 0

for password in complete:
    try:
        tries += 1
        print(f'Try number {tries}...')
        password = password.strip("\n")
        z.setpassword(password.encode('ascii'))
        z.extract('This is it.docx') #NAME OF FILE(S) INSIDE ZIP
        print(f'Password is -- {password} -- after {tries}!')
    except:
        pass