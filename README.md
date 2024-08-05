The task at hand with this cybersecurity job simulation was to write a Python
script to bruteforce the decryption key of the encrypted file, to avoid paying a ransom

    - This was accomplished by importing the zipfile and using the main function to open rockyou.txt,
    iterating through the passwords and calling 'attempt_extract(zf, password)' with each password

    - The code uses strip() and decode('utf-8') to handle and clean the passwords read from rockyou.txt

    - Prints the password if found and stops the brute force process, prints an attempt message if the password is incorrect
