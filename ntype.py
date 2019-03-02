import struct
class uint16:
    _struct = struct.Struct('>H')
    def w(b,a,v): struct.pack_into('>H', b,a,v)
    def r(b,a = 0): return uint16._struct.unpack_from(b,a)[0]
    def bytes(value):
        value = value & 0xFFFF
        return [(value >> 8) & 0xFF, value & 0xFF]
    def value(values):
        return (values[0] << 24) | (values[1] << 16) | (values[2] << 8) | values[3]
    
class uint32:
    _struct = struct.Struct('>I')
    def w(b,a,v): struct.pack_into('>I', b,a,v)
    def r(b,a = 0): return uint32._struct.unpack_from(b,a)[0]
    def bytes(value):
        value = value & 0xFFFFFFFF
        return [(value >> 24) & 0xFF, (value >> 16) & 0xFF, (value >> 8) & 0xFF, value & 0xFF]
    def value(values):
        return (values[0] << 8) | values[1]
        
class int32:
    _struct = struct.Struct('>i')
    def w(b,a,v): struct.pack_into('>i', b,a,v)
    def r(b,a = 0): return int32._struct.unpack_from(b,a)[0]
    def bytes(value):
        value = value & 0xFFFFFFFF
        return [(value >> 24) & 0xFF, (value >> 16) & 0xFF, (value >> 8) & 0xFF, value & 0xFF]
    def value(values):
        return (values[0] << 8) | values[1]
        
class uint24:
    def bytes(value):
        value = value & 0xFFFFFF
        return [(value >> 16) & 0xFF, (value >> 8) & 0xFF, value & 0xFF]
    def value(values):
        return (values[0] << 16) | (values[1] << 8) | values[2]
    def __write_to_array(b, a, v):
        byte_arr = bytes(v)
        b[a:a + 3] = byte_arr[0:3]
    def __read_from_array(b, a = 0):
        return (b[a+0] << 16) | (b[a+1] << 8) | b[a+2]
    w = __write_to_array
    r = __read_from_array


class BigStream(object):
    def __init__(self, buffer:bytearray):
        self.__last_address = 0
        self.buffer = buffer

    def seek_address(self, address):
        self.last_address = address

    def read_byte(self, address):
        self.last_address = address + 1
        return self.buffer[address]

    def read_bytes(self, address, len):
        self.last_address = address + len
        return self.buffer[address : address + len]

    def read_int16(self, address):
        return uint16.r(self.read_bytes(address, 2))

    def read_int24(self, address):
        return uint24.r(self.read_bytes(address, 3))

    def read_int32(self, address):
        return uint32.r(self.read_bytes(address, 4))

    def write_byte(self, address, value):
        if address == None:
            address = self.last_address
        self.buffer[address] = value
        self.last_address = address + 1

    def write_sbyte(self, address, value):
        if address == None:
            address = self.last_address
        self.write_bytes(address, struct.pack('b', value))

    def write_int16(self, address, value):
        if address == None:
            address = self.last_address
        self.write_bytes(address, uint16.bytes(value))

    def write_int24(self, address, value):
        if address == None:
            address = self.last_address
        self.write_bytes(address, uint24.bytes(value))

    def write_int32(self, address, value):
        if address == None:
            address = self.last_address
        self.write_bytes(address, uint32.bytes(value))

    def write_f32(self, address, value:float):
        if address == None:
            address = self.last_address
        self.write_bytes(address, struct.pack('>f', value))

    def write_bytes(self, startaddress, values):
        if startaddress == None:
            startaddress = self.last_address
        for i, value in enumerate(values):
            self.write_byte(startaddress + i, value)

    def write_int16s(self, startaddress, values):
        if startaddress == None:
            startaddress = self.last_address
        for i, value in enumerate(values):
            self.write_int16(startaddress + (i * 2), value)

    def write_int24s(self, startaddress, values):
        if startaddress == None:
            startaddress = self.last_address
        for i, value in enumerate(values):
            self.write_int24(startaddress + (i * 3), value)

    def write_int32s(self, startaddress, values):
        if startaddress == None:
            startaddress = self.last_address
        for i, value in enumerate(values):
            self.write_int32(startaddress + (i * 4), value)