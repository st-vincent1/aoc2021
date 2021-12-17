import sys
import math

def h2b(s):
    h2b = {"0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111" }
    return ''.join(h2b[c] for c in s)


class Bits:
    def __init__(self, v, t, value, internal_bits):
        self.v = v
        self.t = t
        self.value = value
        self.internal_bits = internal_bits

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.v = } || {self.t = } || {self.value = } \n {self.internal_bits = }"

    @classmethod
    def from_binary(cls, bin_, leave_residue=False):
        v = int(bin_[:3], 2)
        t = int(bin_[3:6], 2)

        if t == 4:
            literal_value, residue = Bits.read_literal_value(bin_[6:])
            internal_bits = []
        else:
            internal_bits, residue = Bits.construct_bits(bin_[6:])
            literal_value = None

        if leave_residue:
            return cls(v, t, literal_value,  internal_bits), residue
        return cls(v, t, literal_value, internal_bits)

    @staticmethod
    def read_literal_value(bin_):
        total_value = ''
        for k in range(0, len(bin_), 5):
            total_value = total_value + bin_[k + 1:k + 5]
            if bin_[k] == '0':
                residue_ = k + 5
                break
        return int(total_value, 2), bin_[residue_:]

    @staticmethod
    def construct_bits(bin_):
        if bin_[0] == '0':
            length_in_bits = int(bin_[1:16], 2)
            bits_ = Bits.collect_from_length(bin_[16:16 + length_in_bits])
            residue = bin_[16+length_in_bits:]
        else:
            number_of_subpackets = int(bin_[1:12], 2)
            bits_, residue = Bits.collect_by_number(bin_[12:], number_of_subpackets)
        return bits_, residue

    @classmethod
    def collect_from_length(cls, bin_):
        """
        bin_ contains a number of subpackets. Unpack them and return as a list of Bits
        :param bin_:
        :param length_:
        :param residue:
        :return:
        """
        bits_ = []
        while bin_:
            bit_, bin_ = Bits.from_binary(bin_, leave_residue=True)
            bits_.append(bit_)
        return bits_

    @classmethod
    def collect_by_number(cls, bin_, num):
        bits_ = []
        while num:
            bit_, bin_ = Bits.from_binary(bin_, leave_residue=True)
            bits_.append(bit_)
            num -= 1
        return bits_, bin_

    def retrieve_version_sum(self):
        return self.v + sum([k.retrieve_version_sum() for k in self.internal_bits])


    def eval(self):
        for k in range(len(self.internal_bits)):
            if self.internal_bits[k].value is None:
                self.internal_bits[k].value = self.internal_bits[k].eval()

        vals = [i.value for i in self.internal_bits]
        if self.t == 0: self.value = sum(vals)
        if self.t == 1: self.value = math.prod(vals)
        if self.t == 2: self.value = min(vals)
        if self.t == 3: self.value = max(vals)
        if self.t in [5,6,7]:
            assert len(vals) == 2
            if self.t == 5:
                self.value = vals[0] > vals[1]
            if self.t == 6:
                self.value = vals[0] < vals[1]
            if self.t == 7:
                self.value = vals[0] == vals[1]
        return self.value


if __name__ == '__main__':
    examples_b = [
        ("620080001611562C8802118E34", 46),
        ("C0015000016115A2E0802F182340", 45),
        # ("C200B40A82", 3),
        # ("04005AC33890", 54),
        # ("880086C3E88112", 7),
        # ("CE00C43D881120", 9),
        # ("D8005AC2A8F0", 1),
        # ("F600BC2D8F", 0),
        # ("9C005AC2F8F0", 0),
        # ("9C0141080250320F1802104A08", 1)
    ]

    all_tests_passed = True
    for sample, answer in examples_b:
        bin_ = h2b(sample)
        print(bin_)
        k = Bits.from_binary(bin_)
        prediction = k.eval()
        print(k)
        try:
            assert prediction == answer
        except AssertionError:
            print(f"Test {sample} failed. Expected: {answer}, got {prediction}.")
            all_tests_passed = False
            pass
    if all_tests_passed:
        print("Congratulations, all tests passed. Running main puzzle. . .")
        with open('input_file', 'r') as f:
            sample = f.read().splitlines()[0]
        bin_ = h2b(sample)
        k = Bits.from_binary(bin_)
        prediction = k.eval()
        print("16A: ", k.retrieve_version_sum())
        print("16B: ", prediction)



