Hi Rahul, I got the encryption methods working for both a data input
and data file. Data file reads an inputFile.txt that I made 
and converts whatever is inside to an external file called 
encryptedFile.txt. Decryption also works, and I got the encryptedFile.txt
to be able to decrypt it back to a decryptedFile.txt.  

Unfortunately, I don't think I implemented the chain of responsibility 
properly this lab. I will probably be needing to see you during office hours
before the final to understand it more in depth for this lab. 

Anyways, here's what I did to test the lab: 

Test data input string: 

python3 crypto abcd1234 -s "Test Data to be encrypted" -m en 

Test input file: 

crypto.py abcd1234 -f "inputFile.txt" -m en

Test decrypt input string: 

python3 crypto abcd1234 -s "Test Data to be encrypted" -m de

Test decrypt file: 

python3 crypto.py abcd1234 -f "encryptedFile.txt" -m de

Thanks for reading, 
Ringo 