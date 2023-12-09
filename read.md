# Password Generator and Strength Checker
The program will create and password and check it's strength.
You can also enter your own password and check it's strength.

Strength will be determined using password entropy, using the following guide:


Password strength is determined with this chart:
* < 28 bits = Very Weak; might keep out family members
* 28 - 35 bits = Weak; should keep out most people, often good for desktop login passwords
* 36 - 59 bits = Reasonable; fairly secure passwords for network and company passwords
* 60 - 127 bits = Strong; can be good for guarding financial information
* 128+ bits = Very Strong; often overkill

Password entropy will be calculated using the following reference: [Password Entropy Reference](https://www.pleacher.com/mp/mlessons/algebra/entropy.html)

For password generation, you can select the number of characters and a password will be generated.
