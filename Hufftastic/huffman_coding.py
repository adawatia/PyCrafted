import heapq
import os
from collections import Counter

class HuffmanCoding:
    def __init__(self, path):
        self.path = path
        self.heap = []
        self.codes = {}
        self.reverse_mapping = {}

    class HeapNode:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            if not other:
                return False
            if not isinstance(other, type(self)):
                return False
            return self.freq == other.freq

    def make_frequency_dict(self, data):
        return Counter(data)

    def make_heap(self, frequency):
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self, root, current_code):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char

        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        if len(self.heap) == 0:
            return
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_encoded_data(self, data):
        encoded_data = "".join([self.codes[byte] for byte in data])
        return encoded_data

    def pad_encoded_data(self, encoded_data):
        extra_padding = 8 - len(encoded_data) % 8
        for i in range(extra_padding):
            encoded_data += "0"
        padded_info = "{0:08b}".format(extra_padding)
        encoded_data = padded_info + encoded_data
        return encoded_data

    def get_byte_array(self, padded_encoded_data):
        if len(padded_encoded_data) % 8 != 0:
            print("Encoded data not padded properly")
            exit(0)

        b = bytearray()
        for i in range(0, len(padded_encoded_data), 8):
            byte = padded_encoded_data[i:i+8]
            b.append(int(byte, 2))
        return b

    def compress(self):
        filename, file_extension = os.path.splitext(self.path)
        output_path = filename + ".bin"

        # Change to read in binary mode
        with open(self.path, 'rb') as file, open(output_path, 'wb') as output:
            data = file.read()
            frequency = self.make_frequency_dict(data)
            self.make_heap(frequency)
            self.merge_nodes()
            self.make_codes()

            encoded_data = self.get_encoded_data(data)
            padded_encoded_data = self.pad_encoded_data(encoded_data)

            b = self.get_byte_array(padded_encoded_data)
            output.write(bytes(b))

        print("Compressed")
        return output_path

    def remove_padding(self, padded_encoded_data):
        padded_info = padded_encoded_data[:8]
        extra_padding = int(padded_info, 2)

        padded_encoded_data = padded_encoded_data[8:]
        encoded_data = padded_encoded_data[:-1 * extra_padding]

        return encoded_data

    def decode_data(self, encoded_data):
        current_code = ""
        decoded_data = bytearray()

        for bit in encoded_data:
            current_code += bit
            if current_code in self.reverse_mapping:
                byte = self.reverse_mapping[current_code]
                decoded_data.append(byte)
                current_code = ""

        return decoded_data

    def decompress(self, input_path):
        filename, file_extension = os.path.splitext(input_path)
        output_path = filename + "_decompressed" + file_extension  # Keep original extension

        with open(input_path, 'rb') as file, open(output_path, 'wb') as output:
            bit_string = ""

            byte = file.read(1)
            while len(byte) > 0:
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = file.read(1)

            encoded_data = self.remove_padding(bit_string)
            decompressed_data = self.decode_data(encoded_data)
            output.write(bytes(decompressed_data))

        print("Decompressed")
        return output_path
