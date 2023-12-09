## README.md

**Password Generator and Strength Checker**

This Python script provides two functionalities: generating a random password and checking the strength of a user-defined password.

### Features:

* Generates random passwords with varying lengths and character sets (letters, numbers, symbols).
* Computes the password's entropy, which is a measure of its security against brute-force attacks.
* Provides a user-friendly interface for input and feedback.

### Usage:

1. Run the `password_strength.py` script.
2. Select your preferred option:
    * Enter `1` to generate a random password and receive its strength analysis.
    * Enter `2` to input your own password and obtain its strength score.
3. Follow the on-screen prompts for password length (for option 1) or password entry (for option 2).
4. The script will output the generated password (if applicable) and its strength rating.

### Password Strength Rating:
Follows the following reference: [Password Entropy Reference](https://www.pleacher.com/mp/mlessons/algebra/entropy.html)


* **Very Weak:** Entropy less than 28 bits. Suitable for family-level security.
* **Weak:** Entropy between 28 and 35 bits. Good for desktop login passwords.
* **Reasonable:** Entropy between 35 and 59 bits. Fair security for network and company passwords.
* **Strong:** Entropy between 60 and 127 bits. Suitable for guarding financial information.
* **Very Strong:** Entropy exceeding 127 bits. Often considered overkill.

### Dependencies:

* Python 3
* No additional libraries required

### Example Output:

**Option 1:**


Welcome to the password generator and strength checker, would you like to create a password or strength the check of your password?
Enter 1 to generate and 2 to enter your own password
1
Ok!
How long would you like the password to be?
12
Here's your password
tP9#x5y3u8sG
Password is Strong; can be good for guarding financial information
Thank you for using the password generator and strength checker


**Option 2:**


Welcome to the password generator and strength checker, would you like to create a password or strength the check of your password?
Enter 1 to generate and 2 to enter your own password
2
Ok!
Please enter your password
MySuperSecretPassword123!
Password is Very Strong; often overkill
Thank you for using the password generator and strength checker


### Contributing:

This script is open-source and welcomes contributions for further improvement. Feel free to fork the repository and submit pull requests with your suggestions and enhancements.
