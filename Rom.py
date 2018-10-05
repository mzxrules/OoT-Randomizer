import io
import logging
import os
import platform
import struct
import subprocess


class LocalRom(object):

    def __init__(self, file, patch=True):
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        #os.chdir(output_path(os.path.dirname(os.path.realpath(__file__))))
        with open(file, 'rb') as stream:
            self.buffer = read_rom(stream)
        file_name = os.path.splitext(file)
        if len(self.buffer) < 0x2000000 or len(self.buffer) > 0x4000000 or file_name[1] not in ['.z64', '.n64']:
            raise RuntimeError('ROM is not a valid OoT 1.0 ROM.')
        if len(self.buffer) == 0x2000000:
            if platform.system() == 'Windows':
                subprocess.call(["Decompress\Decompress.exe", file, output_path('ZOOTDEC.z64')])
                with open((output_path('ZOOTDEC.z64')), 'rb') as stream:
                    self.buffer = read_rom(stream)
            elif platform.system() == 'Linux':
                subprocess.call(["Decompress/Decompress", file])
                with open(("ZOOTDEC.z64"), 'rb') as stream:
                    self.buffer = read_rom(stream)
            elif platform.system() == 'Darwin':
                subprocess.call(["Decompress/Decompress.out", file])
                with open(("ZOOTDEC.z64"), 'rb') as stream:
                    self.buffer = read_rom(stream)
            else:
                raise RuntimeError('Unsupported operating system for decompression. Please supply an already decompressed ROM.')
        # extend to 64MB
        self.buffer.extend(bytearray([0x00] * (0x4000000 - len(self.buffer))))
            

    def write_byte(self, address, value):
        self.buffer[address] = value

    def write_bytes(self, startaddress, values):
        for i, value in enumerate(values):
            self.write_byte(startaddress + i, value)

    def write_int16_to_rom(self, address, value):
        self.write_bytes(address, int16_as_bytes(value))

    def write_int32_to_rom(self, address, value):
        self.write_bytes(address, int32_as_bytes(value))

    def write_to_file(self, file):
        with open(file, 'wb') as outfile:
            outfile.write(self.buffer)

def read_rom(stream):
    "Reads rom into bytearray"
    buffer = bytearray(stream.read())
    return buffer


def int16_as_bytes(value):
    value = value & 0xFFFF
    return [value & 0xFF, (value >> 8) & 0xFF]

def int32_as_bytes(value):
    value = value & 0xFFFFFFFF
    return [value & 0xFF, (value >> 8) & 0xFF, (value >> 16) & 0xFF, (value >> 24) & 0xFF]