import pikepdf
import os

# load password list
passwords = "june2022"
list_of_files = filter(os.path.isfile, os.listdir(os.curdir))
print("Here is your current files contained in current directory: ")
count = 1
for files in list(list_of_files):

    print(f'{count}. {files}')
    count += 1
file_name = input("Please write the file name? ")
# iterate over passwords

# open PDF file
with pikepdf.open(f"{file_name}", passwords) as pdf:
    # Password decrypted successfully, break out of the loop
    print("[+] Password found:", passwords)
    pdf.save("hello.pdf")

