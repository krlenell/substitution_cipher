import sys
import argparse
import random

class Cipher():
    def __init__(self, input=None, key=None):
        self.alpha = list('abcdefghijklmnopqrstuvwxyz')
        self.input = input
        self.key = key

    def encode(self):
        if not self.input:
            raise ValueError("Cannot encode without a set input")
        res = {"original": self.input, "key": self.key}
        s = ''
        for char in self.input:
            if char.lower() in self.key:
                s += self.key[char.lower()]
            else:
                s += char
        res["encoded"] = s
        return res

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, input):
        self._input = input

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        if key:
            # add more checks for key
            self._key = key
        cipher_key = {}
        shuffled_alpha = list(self.alpha)
        random.shuffle(shuffled_alpha)
        for i in range(len(self.alpha) - 1):
            cipher_key[self.alpha[i]] = shuffled_alpha[i]
        self._key = cipher_key

    def decode(self):
        pass

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--decode", help="decode the input using a key", action="store_true")
    parser.add_argument("--encode", help="cipher the input text and create a key", action="store_true")
    parser.add_argument("--input", help="a raw string to be decoded or encoded", action="store")
    parser.add_argument("--key", help="decryption key used to decode input", action="store")
    parser.add_argument("--keygen", help="simply generate a key object", action="store_true")
    args = parser.parse_args()
    return args


def main():
    args = init_args()
    print(args)
    if args.keygen:
        c = Cipher()
        print(c.key)
    if args.encode:
        c = Cipher(input=args.input)
        print(c.encode())

if __name__ == "__main__":
    main()
