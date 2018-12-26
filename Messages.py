# text details: https://wiki.cloudmodding.com/mm/Text_Format

import random

TABLE_START = 0xC5D0D8
TEXT_START = 0xAD1000

TABLE_SIZE_LIMIT = 0x90D8
TEXT_SIZE_LIMIT = 0x6A000

# name of type, followed by number of additional bytes to read, follwed by a function that prints the code
CONTROL_CODES = {
    0x00: ('text-white', 0, lambda _: '<default text>' ),
    0x01: ('text-red', 0, lambda _: '<red text>' ),
    0x02: ('text-green', 0, lambda _: '<green text>' ),
    0x03: ('text-blue', 0, lambda _: '<blue text>' ),
    0x04: ('text-yellow', 0, lambda _: '<yellow text>' ),
    0x05: ('text-turquoise', 0, lambda _: '<turquoise text>' ),
    0x06: ('text-pink', 0, lambda _: '<pink text>' ),
    0x07: ('text-silver', 0, lambda _: '<silver text>' ),
    0x08: ('text-orange', 0, lambda _: '<orange text>' ),
    0x0A: ('spaces', 1, lambda d: '<' + "{:02x}".format(d) + ' spaces>'),
    0x0B: ('cruise-reward', 0, lambda _: '<cruise reward hit count>' ),
    0x0C: ('stray-fairy', 0, lambda _: '<stray fairy count>' ),
    0x0D: ('skulltula', 0, lambda _: '<skulltula count>' ),
    0x10: ('box-break', 0, lambda _: '\n▼ 4\n' ),
    0x11: ('line-break', 0, lambda _: '\n▼ 3\n' ),
    0x12: ('box-break2', 0, lambda _: '\n▼\n' ),
    0x13: ('cursor-reset', 0, lambda _: '<cursor reset>'),
    0x15: ('disable-skip', 0, lambda _: '<disable text skip>' ),
    0x16: ('name', 0, lambda _: '<name>' ),
    0x17: ('instant', 0, lambda _: '<allow instant text>' ),
    0x18: ('un-instant', 0, lambda _: '<disallow instant text>' ),
    0x19: ('disable-skip-finish', 0, lambda _: '<disable text skip finish>' ),
    0x1A: ('disable-close', 0, lambda _: '<disable textbox close>' ),
    0x1B: ('delay', 2, lambda d: '<wait ' + str(d) + ' frames>' ),
    0x1C: ('fade-out', 2, lambda d: '<fade after ' + str(d) + ' frames?>' ),
    0x1D: ('delay-end', 2, lambda d: '\n▼<end after ' + str(d) + ' frames>\n' ),
    0x1E: ('sound', 2, lambda d: '<play SFX ' + "{:04x}".format(d) + '>' ),
    0x1F: ('pause', 2, lambda d: '\n<wait ' + str(d) + ' frames>\n' ),
    0xBF: ('end', 0, lambda _: '' ),
    0xC1: ('ocarina-failed', 0, lambda _: '<ocarina song failed>'),
    0xC2: ('two-choice', 0, lambda _: '<start two choice>' ),
    0xC3: ('three-choice', 0, lambda _: '<start three choice>' ),
    0xCF: ('time', 0, lambda _: '<time remaining>' ),
    0xE0: ('end-conversation', 0, lambda _: '<end conversation>' ),
    0xE7: ('moon-fall', 0, lambda _: '<time to moon fall>' ),
    0xE8: ('morning', 0, lambda _: '<time to morning>' ),
}

ICONS = {
    0x96: 'é',
    0x9F: '[A]',
    0xA0: '[B]',
    0xA1: '[C]',
    0xA2: '[L]',
    0xA3: '[R]',
    0xA4: '[Z]',
    0xA5: '[C Up]',
    0xA6: '[C Down]',
    0xA7: '[C Left]',
    0xA8: '[C Right]',
    0xA9: '[Triangle]',
    0xAA: '[Control Stick]',
}

TEXT_BOX_TYPES = {
    0x0: ('standard', lambda _: 'Standard Textbox' ),
    0x1: ('sign', lambda _: 'Wooden Sign' ),
}

GOSSIP_STONE_MESSAGES = list( range(0x0401, 0x0421) ) # ids of the actual hints
GOSSIP_STONE_MESSAGES += [0x2053, 0x2054] # shared initial stone messages
TEMPLE_HINTS_MESSAGES = [0x7057, 0x707A] # dungeon reward hints from the temple of time pedestal
LIGHT_ARROW_HINT = [0x70CC] # ganondorf's light arrow hint line
GS_TOKEN_MESSAGES = [0x00B4, 0x00B5] # Get Gold Skulltula Token messages

# messages for shorter item messages
ITEM_MESSAGES = {
}


# messages for keysanity item pickup
# ids are in the space freed up by move_shop_item_messages()
KEYSANITY_MESSAGES = {
    0x06: '\x13\x74\x08You got the \x05\x41Boss Key\x05\x40\x01for the \x05\x42Forest Temple\x05\x40!\x09',
    0x1c: '\x13\x74\x08You got the \x05\x41Boss Key\x05\x40\x01for the \x05\x41Fire Temple\x05\x40!\x09',
    0x1d: '\x13\x74\x08You got the \x05\x41Boss Key\x05\x40\x01for the \x05\x43Water Temple\x05\x40!\x09',
    0x1e: '\x13\x74\x08You got the \x05\x41Boss Key\x05\x40\x01for the \x05\x46Spirit Temple\x05\x40!\x09',
    0x65: '\x13\x75\x08You found the \x05\x41Compass\x05\x40\x01for the \x05\x42Forest Temple\x05\x40!\x09',
    0x7c: '\x13\x75\x08You found the \x05\x41Compass\x05\x40\x01for the \x05\x41Fire Temple\x05\x40!\x09',
    0x7d: '\x13\x75\x08You found the \x05\x41Compass\x05\x40\x01for the \x05\x43Water Temple\x05\x40!\x09',
    0x7e: '\x13\x75\x08You found the \x05\x41Compass\x05\x40\x01for the \x05\x46Spirit Temple\x05\x40!\x09',
    0x8b: '\x13\x76\x08You found the \x05\x41Dungeon Map\x05\x40\x01for the \x05\x42Forest Temple\x05\x40!\x09',
    0x8c: '\x13\x76\x08You found the \x05\x41Dungeon Map\x05\x40\x01for the \x05\x41Fire Temple\x05\x40!\x09',
    0x8e: '\x13\x76\x08You found the \x05\x41Dungeon Map\x05\x40\x01for the \x05\x43Water Temple\x05\x40!\x09',
    0x8f: '\x13\x76\x08You found the \x05\x41Dungeon Map\x05\x40\x01for the \x05\x46Spirit Temple\x05\x40!\x09',
    0x93: '\x13\x77\x08You found a \x05\x41Small Key\x05\x40\x01for the \x05\x42Forest Temple\x05\x40!\x09',
    0x94: '\x13\x77\x08You found a \x05\x41Small Key\x05\x40\x01for the \x05\x41Fire Temple\x05\x40!\x09',
    0x95: '\x13\x77\x08You found a \x05\x41Small Key\x05\x40\x01for the \x05\x43Water Temple\x05\x40!\x09',
    0xa6: '\x13\x77\x08You found a \x05\x41Small Key\x05\x40\x01for the \x05\x46Spirit Temple\x05\x40!\x09',
}


# messages for song items
SONG_MESSAGES = {
    0x00B0: "\x08\x06\x28You have learned the\x01\x06\x2F\x05\x42Minuet of Forest\x05\x40!",
    0x00B1: "\x08\x06\x28You have learned the\x01\x06\x37\x05\x41Bolero of Fire\x05\x40!",
    0x00B2: "\x08\x06\x28You have learned the\x01\x06\x29\x05\x43Serenade of Water\x05\x40!",
    0x00B3: "\x08\x06\x28You have learned the\x01\x06\x2D\x05\x46Requiem of Spirit\x05\x40!",
    0x00B6: "\x08\x06\x28You have learned the\x01\x06\x28\x05\x45Nocturne of Shadow\x05\x40!",
    0x00B7: "\x08\x06\x28You have learned the\x01\x06\x32\x05\x44Prelude of Light\x05\x40!",
    0x00B8: "\x08\x06\x15You've learned \x05\x43Zelda's Lullaby\x05\x40!",
    0x00B9: "\x08\x06\x11You've learned \x05\x41Epona's Song\x05\x40!",
    0x00BA: "\x08\x06\x14You've learned \x05\x42Saria's Song\x05\x40!",
    0x00BB: "\x08\x06\x0BYou've learned the \x05\x46Sun's Song\x05\x40!",
    0x00BC: "\x08\x06\x05You've learned the \x05\x44Song of Time\x05\x40!",
    0x00BD: "\x08You've learned the \x05\x45Song of Storms\x05\x40!",
}


# convert byte array to an integer
def bytes_to_int(bytes, signed=False):
    return int.from_bytes(bytes, byteorder='big', signed=signed)

# convert int to an array of bytes of the given width
def int_to_bytes(num, width, signed=False):
    return int.to_bytes(num, width, byteorder='big', signed=signed)

def display_code_list(codes):
    message = ""
    for code in codes:
        message += str(code)
    return message

def check_message_header( rom, offset):
        check_header = rom.read_bytes( TEXT_START + offset, 11 )
        end_header = bytes_to_int( check_header[7:] )
        return check_header[0] & 0xF0 == 0x00 and end_header == 0xFFFFFFFF

def find_message_byte(rom, start, limit, find_byte = 0xBF):
        if start >= limit:
            return 0
        offset = start
        # skip the header if it exists
        if check_message_header( rom, offset ):
            offset += 11
        while offset < limit:
            next_char = rom.read_byte(offset)
            if next_char == find_byte: # message end code
                return offset - start
            offset += 1
        return limit - offset

# holds a single character or control code of a string
class Text_Code():

    def display(self):
        if self.code in CONTROL_CODES:
            return CONTROL_CODES[self.code][2](self.data)
        elif self.code in ICONS:
            return ICONS[self.code]
        elif self.code >= 0x7F:
            return '?'
        else:
            return chr(self.code)

    def get_python_string(self):
        if self.code in CONTROL_CODES:
            ret = ''
            subdata = self.data
            for _ in range(0, CONTROL_CODES[self.code][1]):
                ret = ('\\x%02X' % (subdata & 0xFF)) + ret
                subdata = subdata >> 8
            ret = '\\x%02X' % self.code + ret
            return ret
        elif self.code in ICONS:
            return '\\x%02X' % self.code
        # elif self.code >= 0x7F:
            # return '?'
        else:
            return chr(self.code)

    # writes the code to the given offset, and returns the offset of the next byte
    def write(self, rom, offset):
        rom.write_byte(TEXT_START + offset, self.code)

        extra_bytes = 0
        if self.code in CONTROL_CODES:
            extra_bytes = CONTROL_CODES[self.code][1]
            bytes_to_write = int_to_bytes(self.data, extra_bytes)
            rom.write_bytes(TEXT_START + offset + 1, bytes_to_write)

        return offset + 1 + extra_bytes

    def __init__(self, code, data):
        self.code = code
        if code in CONTROL_CODES:
            self.type = CONTROL_CODES[code][0]
        else:
            self.type = 'character'
        self.data = data

    __str__ = __repr__ = display

# holds a single message, and all its data
class Message():

    def display(self):
        meta_data = ["#" + str(self.index),
         "ID: 0x" + "{:04x}".format(self.id),
         "Offset: 0x" + "{:06x}".format(self.offset),
         "Length: 0x" + "{:04x}".format(self.length),
         "Box Type: " + str(self.box_type),
         "Position: " + str(self.position)]
        return ', '.join(meta_data) + '\n' + self.text

    def get_python_string(self):
        ret = ''
        for code in self.text_codes:
            ret = ret + code.get_python_string()
        return ret

    # check if this is an unused message that just contains it's own id as text
    def is_id_message(self):
        if self.length == 5:
            for i in range(4):
                code = self.text_codes[i].code
                if not (code in range(ord('0'),ord('9')+1) or code in range(ord('A'),ord('F')+1) or code in range(ord('a'),ord('f')+1) ):
                    return False
            return True
        return False

    # DOOT: actually parse the headers so they don't disappear
    def parse_text(self):
        self.text_codes = []

        index = 0
        next_char = 0x00
        while index < len(self.raw_text) and next_char != 0xBF:
            next_char = self.raw_text[index]
            data = 0
            index += 1
            if next_char in CONTROL_CODES:
                extra_bytes = CONTROL_CODES[next_char][1]
                if extra_bytes > 0:
                    data = bytes_to_int(self.raw_text[index : index + extra_bytes])
                    index += extra_bytes
            text_code = Text_Code(next_char, data)
            self.text_codes.append(text_code)
            if next_char == 0xBF: # message end code
                break
            if next_char == 0x1C: # keep-open
                self.has_keep_open = True
                self.ending = text_code
            if next_char == 0x1D: # fade out
                self.has_fade = True
                self.ending = text_code
            if next_char == 0xC2: # two choice
                self.has_two_choice = True
            if next_char == 0xC3: # three choice
                self.has_three_choice = True
            if next_char == 0xE0:
                self.endNPC = True
        self.text = display_code_list(self.text_codes)
        # print( 'Original: ', str(self.raw_text) )
        self.raw_text = self.raw_text[:index]
        # print( 'Fixed: ', str(self.raw_text) )
        self.length = index

    def is_basic(self):
        return not (self.has_keep_open or self.has_fade or self.has_two_choice or self.has_three_choice or self.has_parent)

    # writes a Message back into the rom, using the given index and offset to update the table
    # returns the offset of the next message
    def write(self, rom, index, offset, replace_ending=False, ending=None, always_allow_skip=True, speed_up_text=True):

        # construct the table entry
        id_bytes = int_to_bytes(self.id, 2)
        offset_bytes = int_to_bytes(offset, 3)
        entry = id_bytes + bytes([0x00, 0x00, 0x08]) + offset_bytes
        # write it back
        entry_offset = TABLE_START + 8 * index
        rom.write_bytes(entry_offset, entry)

        ending_codes = [0x1C, 0x1D]
        box_breaks = [0x10, 0x12]
        slows_text = [0x15, 0x18, 0x19, 0x1A]

        # # speed the text
        if speed_up_text:
            offset = Text_Code(0x17, 0).write(rom, offset) # allow instant

        # write the message
        for code in self.text_codes:
            # ignore ending codes if it's going to be replaced
            if replace_ending and code.code in ending_codes:
                pass
            # ignore the "make unskippable flag"
            elif always_allow_skip and (code.code in [0x15, 0x19, 0x1A]):
                pass
            # ignore anything that slows down text
            elif speed_up_text and code.code in slows_text:
                pass
            elif speed_up_text and code.code in box_breaks:
                offset = Text_Code(0x17, 0).write(rom, offset) # allow instant
            else:
                offset = code.write(rom, offset)

        if replace_ending:
            if ending:
                offset = ending.write(rom, offset) # write special ending
            offset = Text_Code(0xBF, 0).write(rom, offset) # write end code

        while offset % 4 > 0:
            offset = Text_Code(0x00, 0).write(rom, offset) # pad to 4 byte align

        return offset

    def __init__(self, header, raw_text, index, id, offset):

        if header != 0:
            # DOOT: there will be errors wherever these properties are checked
            self.header = header
            self.box_type = (self.header[0] & 0x0F)
            self.position = self.header[1]
            self.icon = self.header[2]
            self.next_message = bytes_to_int(self.header[3:5])
            self.rupees = bytes_to_int(self.header[5:7])
        self.raw_text = raw_text
        if hasattr( self, "header" ):
            pass
        self.index = index
        self.id = id
        self.offset = offset

        self.has_keep_open = False
        self.has_fade = False
        self.has_two_choice = False
        self.has_three_choice = False
        self.ending = None

        self.parse_text()

    # read a single message from rom
    @classmethod
    def from_rom(cls, rom, index):

        entry_offset = TABLE_START + 8 * index
        entry = rom.read_bytes(entry_offset, 8)
        next = rom.read_bytes(entry_offset + 8, 8)
        # print( hex(bytes_to_int(entry[5:8])), ' : ', hex(bytes_to_int(next[5:8])) )

        id = bytes_to_int(entry[0:2])
        offset = bytes_to_int(entry[5:8])
        length = find_message_byte(rom, TEXT_START + offset, TEXT_START + bytes_to_int(next[5:8]), 0xBF)

        if check_message_header( rom, offset ):
            header = rom.read_bytes(TEXT_START + offset, 11)
            raw_text = rom.read_bytes(TEXT_START + offset + 11, length - 11 )
        else:
            header = 0
            raw_text = rom.read_bytes(TEXT_START + offset, length )

        return cls(header, raw_text, index, id, offset)

    @classmethod
    def from_string(cls, header, text, id=0):
        bytes = list(text.encode('utf-8'))

        return cls(bytes, 0, id, 0, len(bytes))

    __str__ = __repr__ = display

# wrapper for updating the text of a message, given its message id
# if the id does not exist in the list, then it will add it
def update_message_by_id(messages, id, header, text):
    # get the message index
    index = next( (m.index for m in messages if m.id == id), -1)
    # update if it was found
    if index >= 0:
        update_message_by_index(messages, index, header, text)
    else:
        add_message(messages, header, text, id)

# Gets the message by its ID. Returns None if the index does not exist
def get_message_by_id(messages, id):
    # get the message index
    index = next( (m.index for m in messages if m.id == id), -1)
    if index >= 0:
        return messages[index]
    else:
        return None

# wrapper for updating the text of a message, given its index in the list
def update_message_by_index(messages, index, text):
    messages[index] = Message.from_string(messages[index].header, text, messages[index].id)
    messages[index].index = index

# wrapper for adding a string message to a list of messages
def add_message(messages, header, text, id=0):
    messages.append( Message.from_string(header, text, id) )
    messages[-1].index = len(messages) - 1

# holds a row in the shop item table (which contains pointers to the description and purchase messages)
class Shop_Item():

    def display(self):
        meta_data = ["#" + str(self.index),
         "Item: 0x" + "{:04x}".format(self.get_item_id),
         "Price: " + str(self.price),
         "Amount: " + str(self.pieces),
         "Object: 0x" + "{:04x}".format(self.object),
         "Model: 0x" + "{:04x}".format(self.model),
         "Description: 0x" + "{:04x}".format(self.description_message),
         "Purchase: 0x" + "{:04x}".format(self.purchase_message),]
        func_data = [
         "func1: 0x" + "{:08x}".format(self.func1),
         "func2: 0x" + "{:08x}".format(self.func2),
         "func3: 0x" + "{:08x}".format(self.func3),
         "func4: 0x" + "{:08x}".format(self.func4),]
        return ', '.join(meta_data) + '\n' + ', '.join(func_data)

    # write the shop item back
    def write(self, rom, shop_table_address, index):

        entry_offset = shop_table_address + 0x20 * index

        bytes = []
        bytes += int_to_bytes(self.object, 2)
        bytes += int_to_bytes(self.model, 2)
        bytes += int_to_bytes(self.func1, 4)
        bytes += int_to_bytes(self.price, 2)
        bytes += int_to_bytes(self.pieces, 2)
        bytes += int_to_bytes(self.description_message, 2)
        bytes += int_to_bytes(self.purchase_message, 2)
        bytes += [0x00, 0x00]
        bytes += int_to_bytes(self.get_item_id, 2)
        bytes += int_to_bytes(self.func2, 4)
        bytes += int_to_bytes(self.func3, 4)
        bytes += int_to_bytes(self.func4, 4)

        rom.write_bytes(entry_offset, bytes)

    # read a single message
    def __init__(self, rom, shop_table_address, index):

        entry_offset = shop_table_address + 0x20 * index
        entry = rom.read_bytes(entry_offset, 0x20)

        self.index = index
        self.object = bytes_to_int(entry[0x00:0x02])
        self.model = bytes_to_int(entry[0x02:0x04])
        self.func1 = bytes_to_int(entry[0x04:0x08])
        self.price = bytes_to_int(entry[0x08:0x0A])
        self.pieces = bytes_to_int(entry[0x0A:0x0C])
        self.description_message = bytes_to_int(entry[0x0C:0x0E])
        self.purchase_message = bytes_to_int(entry[0x0E:0x10])
        # 0x10-0x11 is always 0000 padded apparently
        self.get_item_id = bytes_to_int(entry[0x12:0x14])
        self.func2 = bytes_to_int(entry[0x14:0x18])
        self.func3 = bytes_to_int(entry[0x18:0x1C])
        self.func4 = bytes_to_int(entry[0x1C:0x20])

    __str__ = __repr__ = display

# reads each of the shop items
def read_shop_items(rom, shop_table_address):
    shop_items = []

    for index in range(0, 100):
        shop_items.append( Shop_Item(rom, shop_table_address, index) )

    return shop_items

# writes each of the shop item back into rom
def write_shop_items(rom, shop_table_address, shop_items):
    for s in shop_items:
        s.write(rom, shop_table_address, s.index)

# these are unused shop items, and contain text ids that are used elsewhere, and should not be moved
SHOP_ITEM_EXCEPTIONS = [0x0A, 0x0B, 0x11, 0x12, 0x13, 0x14, 0x29]

# returns a set of all message ids used for shop items
def get_shop_message_id_set(shop_items):
    ids = set()
    for shop in shop_items:
        if shop.index not in SHOP_ITEM_EXCEPTIONS:
            ids.add(shop.description_message)
            ids.add(shop.purchase_message)
    return ids

# remove all messages that easy to tell are unused to create space in the message index table
def remove_unused_messages(messages):
    messages[:] = [m for m in messages if not m.is_id_message()]
    for index, m in enumerate(messages):
        m.index = index

# takes all messages used for shop items, and moves messages from the 00xx range into the unused 80xx range
def move_shop_item_messages(messages, shop_items):
    # checks if a message id is in the item message range
    def is_in_item_range(id):
        bytes = int_to_bytes(id, 2)
        return bytes[0] == 0x00
    # get the ids we want to move
    ids = set( id for id in get_shop_message_id_set(shop_items) if is_in_item_range(id) )
    # update them in the message list
    for id in ids:
        # should be a singleton list, but in case something funky is going on, handle it as a list regardless
        relevant_messages = [message for message in messages if message.id == id]
        for message in relevant_messages:
            message.id |= 0x8000
    # update them in the shop item list
    for shop in shop_items:
        if is_in_item_range(shop.description_message):
            shop.description_message |= 0x8000
        if is_in_item_range(shop.purchase_message):
            shop.purchase_message |= 0x8000

def make_player_message(text):
    player_text_U = '\x05\x42\x0F\x05\x40'
    player_text_L = '\x05\x42\x0F\x05\x40'
    pronoun_mapping = {
        'You have ': player_text_U + ' ',
        'You\'ve ':  player_text_U + ' ',
        'Your ':     player_text_U + '\'s ',
        'You ':      player_text_U + ' ',

        'you have ': player_text_L + ' ',
        'you\'ve ':  player_text_L + ' ',
        'your ':     player_text_L + '\'s ',
        'you ':      player_text_L + ' ',
    }

    verb_mapping = {
        'obtained ': 'got ',
        'received ': 'got ',
        'learned ': 'got ',
        'borrowed ': 'got ',
        'found ': 'got ',
    }

    new_text = text
    for find_text, replace_text in pronoun_mapping.items():
        if find_text in text:
            new_text = new_text.replace(find_text, replace_text, 1)
            break
    for find_text, replace_text in verb_mapping.items():
        new_text = new_text.replace(find_text, replace_text)
    return new_text




# add the keysanity messages
# make sure to call this AFTER move_shop_item_messages()
def add_keysanity_messages(messages, world):
    for id, text in KEYSANITY_MESSAGES.items():
        if world.world_count > 1:
            update_message_by_id(messages, id, header, make_player_message(text))
        else:
            update_message_by_id(messages, id, header, text)

# add the song messages
# make sure to call this AFTER move_shop_item_messages()
def add_song_messages(messages, world):
    for id, header, text in SONG_MESSAGES.items():
        if world.world_count > 1:
            update_message_by_id(messages, id, header, make_player_message(text))
        else:
            update_message_by_id(messages, id, header, text)

# reduce item message sizes
def update_item_messages(messages, world):
    for id, text in ITEM_MESSAGES.items():
        if world.world_count > 1:
            update_message_by_id(messages, id, header, make_player_message(text))

        else:
            update_message_by_id(messages, id, header, text)

# run all keysanity related patching to add messages for dungeon specific items
def message_patch_for_dungeon_items(messages, shop_items, world):
    move_shop_item_messages(messages, shop_items)
    add_keysanity_messages(messages, world)

# reads each of the game's messages into a list of Message objects
def read_messages(rom):

    table_offset = TABLE_START
    index = 0
    messages = []
    while True:
        entry = rom.read_bytes(table_offset, 8)
        id = bytes_to_int(entry[0:2])

        if id == 0xFFFD:
            pass

        if id == 0xFFFF:
            break # this marks the end of the table

        messages.append( Message.from_rom(rom, index) )

        index += 1
        table_offset += 8

    check_multi_textbox(messages)
    return messages

# wrtie the messages back
def repack_messages(rom, messages, permutation=None, always_allow_skip=True, speed_up_text=True):

    if permutation is None:
        permutation = range(len(messages))

    # repack messages
    offset = 0
    for old_index, new_index in enumerate(permutation):
        old_message = messages[old_index]
        new_message = messages[new_index]
        remember_id = new_message.id
        new_message.id = old_message.id
        offset = new_message.write(rom, old_index, offset, True, old_message.ending, always_allow_skip, speed_up_text)
        new_message.id = remember_id

    if offset > TEXT_SIZE_LIMIT:
        raise(TypeError("Message Text table is too large: 0x" + "{:x}".format(offset) + " written / 0x" + "{:x}".format(TEXT_SIZE_LIMIT) + " allowed."))

    # end the table
    table_index = len(messages)
    entry = bytes([0xFF, 0xFD, 0x00, 0x00, 0x08]) + int_to_bytes(offset, 3)
    entry_offset = TABLE_START + 8 * table_index
    rom.write_bytes(entry_offset, entry)
    table_index += 1
    entry_offset = TABLE_START + 8 * table_index
    if 8 * (table_index + 1) > TABLE_SIZE_LIMIT:
        raise(TypeError("Message ID table is too large: 0x" + "{:x}".format(8 * (table_index + 1)) + " written / 0x" + "{:x}".format(TABLE_SIZE_LIMIT) + " allowed."))
    rom.write_bytes(entry_offset, [0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

def check_multi_textbox(messages):
    for m in messages:
        if hasattr( m, "header" ):
            next = get_message_by_id(messages, m.next_message)
            if next:
                next.has_parent = True
# shuffles the messages in the game, making sure to keep various message types in their own group
def shuffle_messages(rom, except_hints=True, always_allow_skip=True):

    messages = read_messages(rom)

    permutation = [i for i, _ in enumerate(messages)]

    def is_not_exempt(m):
        exempt_as_id = m.is_id_message()
        exempt_as_hint = ( except_hints and m.id in (GOSSIP_STONE_MESSAGES + TEMPLE_HINTS_MESSAGES + LIGHT_ARROW_HINT + list(KEYSANITY_MESSAGES.keys()) + shuffle_messages.shop_item_messages ) )
        return hasattr( m, "parent" )

    textboxes = list( filter( lambda m: hasattr( m, "header"), messages ) )
    have_keep_open =    list( filter( lambda m: is_not_exempt(m) and m.has_keep_open, textboxes) )
    have_fade =         list( filter( lambda m: is_not_exempt(m) and m.has_fade, textboxes) )
    have_two_choice =   list( filter( lambda m: is_not_exempt(m) and m.has_two_choice, textboxes) )
    have_three_choice = list( filter( lambda m: is_not_exempt(m) and m.has_three_choice, textboxes) )
    basic_textboxes =    list( filter( lambda m: is_not_exempt(m) and m.is_basic(), textboxes) )
    textbox_group = []
    for code, _ in enumerate(TEXT_BOX_TYPES):
        textbox_group.append( list( filter( lambda m: m.box_type == code, textboxes ) ) )

    def shuffle_group(group):
        group_permutation = [i for i, _ in enumerate(group)]
        random.shuffle(group_permutation)

        for index_from, index_to in enumerate(group_permutation):
            permutation[group[index_to].index] = group[index_from].index

    # need to use 'list' to force 'map' to actually run through
    list( map( shuffle_group, textbox_group))

    # write the messages back
    repack_messages(rom, messages, permutation, always_allow_skip, False)
