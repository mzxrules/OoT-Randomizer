class InitialSave(object):
    def __init__(self, log = True):
        self.table = []
        self.log = log
        

    # will set the bits of value to the offset in the save (or'ing them with what is already there)
    def set_bits(self, offset, value, filter=None):

        if filter and not filter(value):
            return
        if self.log:
            print("| {:08x} {:04x} {:02x}".format(0x801EF670 + offset, offset, value))
        self.table += [(offset & 0xFF00) >> 8, offset & 0xFF, 0x00, value]

        
    # will overwrite the byte at offset with the given value
    def set_byte(self, offset, value, filter=None):

        if filter and not filter(value):
            return
        
        if self.log:
            print("W {:08x} {:04x} {:02x}".format(0x801EF670 + offset, offset, value))
        self.table += [(offset & 0xFF00) >> 8, offset & 0xFF, 0x01, value]

        
    # will overwrite the byte at offset with the given value
    def set_bytes(self, offset, bytes, filter=None):
        for i, value in enumerate(bytes):
            write_byte_to_save(offset + i, value, filter)


    def set_switch_flag(self, scene, flag, filter=None):
        offset = 0xF8 + (scene * 0x1C) + 4 + flag_to_offset(flag)
        bit = flag & 0x7
        value = 1 << bit
        self.set_bits(offset, value, filter)

        
    # will overwrite the byte at offset with the given value
    def write_table_to_rom(self, rom):
        self.table += [0, 0, 0, 0] #terminator
        table_len = len(self.table)

        start = rom.sym("INITIAL_SAVE_DATA")
        end = rom.sym("INITIAL_SAVE_DATA_END")
        size = end - start
        if self.log:
            print("Initial save table capacity: 0x{:03X}/0x{:03X}".format(table_len, size))
        if table_len > size:
            raise Exception("The initial save table has exceeded it's maximum capacity: 0x{:03X}/0x{:03X}".format(table_len, size))
        rom.write_bytes(start, self.table)
        

def flag_to_offset(flag):
    offset = (flag // 0x20) * 4
    w = (flag & 0x18) >> 3
    return offset + 3 - w