#!/usr/local/bin/python3

import argparse
import random

class GenerationConfig:
    count = 0
    maximum = 0
    minimum = 0

    def __init__(self, count = 100, maximum = 100, minimum = 0):
        if count <= 0:
            raise Exception("Count must be positive!")

        if minimum >= maximum:
            raise Exception("Maximum must be greater than minimum!")

        self.count = count
        self.maximum = maximum
        self.minimum = minimum

    def generate(self):
        result = []

        for i in range(self.count):
            result.append(random.randint(self.minimum, self.maximum))

        return result
            

def process_args():
    parser = argparse.ArgumentParser() 

    parser.add_argument("--count", help="number of items to generate", default = 100, required = False)
    parser.add_argument("--max", help="maximum value of generated items", default = 100, required = False)
    parser.add_argument("--min", help="maximum value of generated items", default = 0, required = False)

    args = parser.parse_args()
    return GenerationConfig(int(args.count), int(args.max), int(args.min))    

def generate(generationConfig):
    return generationConfig.generate()

def main():
    generationConfig = process_args()
    data = generate(generationConfig)

    for item in data:
        print(item)

if __name__ == '__main__':
    main()
