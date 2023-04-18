import sys
import json
import argparse
import random

class Cipher():
    def __init__(self, text=None, key=None):
        self.alpha = 'abcdefghijklmnopqrstuvwxyz'
        self.text = text
        self.key = key

    def encode(self):
        print(f"self.text{self.text}")
        if not self.text:
            raise ValueError("Cannot encode without a set input")
        res = {"original": self.text, "key": self.key}
        s = ''
        for char in self.text:
            key = json.loads(self.key)
            if char.lower() in key:
                s += key[char.lower()]
            else:
                s += char
        res["encoded"] = s
        return res

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        if key:
            self.__validate_key(key)
            self._key = key
            return
        cipher_key = {}
        random.shuffle(shuffled_alpha := list(self.alpha))
        for i in range(len(self.alpha)):
            cipher_key[self.alpha[i]] = shuffled_alpha[i]
        self._key = json.dumps(cipher_key)

    def __validate_key(self, key):
        if not key:
            return None
        try:
            key = json.loads(key)
        except json.decoder.JSONDecodeError:
            sys.exit("Input for key is not JSON")
        alpha_len = len(self.alpha)
        keys_set = set(key.keys())
        values_set = set(key.values())
        if not len(keys_set) == alpha_len: 
            sys.exit("Repeated or missing key character")
        if not len(values_set) == alpha_len: 
            sys.exit("Repeated or missing value character")
        kv_set = keys_set.union(values_set)
        if not len(kv_set) == alpha_len:
            sys.exit("Invalid characters in key")
        for char in self.alpha:
            if char not in kv_set:
                sys.exit("Invalid characters in key")
        return

    def decode(self):
        key = json.loads(self.key)
        key = {v: k for k, v in key.items()}
        s = ''
        for char in self.text:
            if char.lower() in key:
                s += key[char]
            else:
                s += char
        return s


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--decode", help="decode the input using a key", action="store_true")
    parser.add_argument("--encode", help="cipher the input text and create a key", action="store_true")
    parser.add_argument("--input", help="a raw string to be decoded or encoded", action="store")
    parser.add_argument("--key", help="decryption key used to decode input. JSON", action="store")
    parser.add_argument("--keygen", help="simply generate a key object", action="store_true")
    #parser.add_argument("--input_path", help="relative path to file to be used as input text", action="store")
    #parser.add_argument("--key_path", help="relative path to file to be used as input", action="store")
    #parser.add_argument("--output", help="name of output file. will be used as name_key.txt and name.txt", action="store")
    parser.add_argument("-t", "--test", help="does whatever testing thing I want", action="store_true")
    args = parser.parse_args()
    return args


def main():
    args = init_args()
    print(args)
    if args.test:
        c = Cipher(key= args.key)
        print(c.key)
    if args.keygen:
        c = Cipher()
        print(c.key)
    if args.encode:
        c = Cipher(text=args.input)
        print(c.encode())
    if args.decode:
        c = Cipher(text=args.input, key= args.key)
        print(c.decode())

if __name__ == "__main__":
    main()
