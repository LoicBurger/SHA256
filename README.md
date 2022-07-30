# SHA-256
Implementation of SHA-256 algorithm

The following repository aims at implementing the SHA-256 algorithm, which hashes an arbitrary message. The algorithm is in python. This implementation allows for choosing the initial hash table for the algorithm, if one does not wish to use the values that are usually used in the regular version of the SHA-256 algorithm. 

## How to use

The sha256 function requires two inputs. The first input corresponds to the message that you wish to hash as a charcater string, and takes the form of a character string. The second entry consists in a table containing 8 hexadecimal values, and is labelled as init_hash_table in the following example
```python
sha256(message, init_hash_table)
```

If no init_hash_table is mentioned, the sha256 function will use default values that are normally used in the standard form of the SHA-256 algorithm. For instance, you can hash the message 'Hello World'`according to the classical SHA-256 algorithm with the following command
```python
sha256('Hello World')
```

## Installation

Create your virtual environement with the following command
```bash
python3 -m venv venv
source venv/bin/activate
pip install pytest
```

## Tests

You can run the tests associated to the sha256 function by typing the following command
```bash
pytest
```

## How it works

This sections aims at explaining the main steps that are executed in the SHA-256 algorithm in a coarse way. For more details, the reader is invited to refer to the code or to the wikipedia description of the SHA-256 [wikipedia](https://en.wikipedia.org/wiki/SHA-2).

### 1. Encoding the message as a binary string

The message is first converted into a binary string which size is a multiple of 512. To this aim, one matches each character of the message to the binary representation of its ascii classification. Let denote the size of this string by l. 

Most of the time, l is not a multiple of 512, as required. To overcome this issue, the binary strring is completed with a single '1' followed by a serie of k '0'. k is chosen in such a way that k = 448-l-1 (mod 512). 

With such an approach, 64 binary characters are missing so that the total number of characters is a multiple of 512. These characters are chose in such a way to correspond to the binary representation of l over 64 bits. 

### 2. Dividing the message into blocks

Thereafter, the binary-encoded message will be divided in blocks of 512 binary characters. Each of these blocks is then subdivided in 16 groups of 32 bits. Such a decomposition will help for the upcoming step, implementing the hash function. 

### 3. Hashing the different blocks

First, a table of 64 bit strings, which will be called "words", is created. The first 16 words correspond to the 16 32-bit subdivisions of the current investigated block. The residual words are then obtained by rearranging the bits composing the previously obtained words according to specific rules. 

Then, a table of 8 values, that will be called variables, is created. The 8 variables are first initialized with the 8 values of the init_hash_table. This variables is then updated according to mathematical operations involving bit manipulation and modular additions. 

The scheme described in the previous paragraph is repeated 64, each iteration involving a given word at a time. At the end of the each of these iterations, the hash values that are used to table of variables is also updated. 

The previous operations must be repeated for each block of 512 binary characters that compose the binary string extracted from the initial message.

Note that by modifying the init_hash_table, you will influence the result of these, and therefore the final expression of the hash of your message. 

### 4. Final encrypted message

The final message corresponds to the concatenation of the 8 final hashes that are obtained, each of these hashes being expressed in hexadecimal notation. The final message is therefore composed of 8*16 = 128 characters.  



