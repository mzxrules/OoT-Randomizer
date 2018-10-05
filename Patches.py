import io
import logging
import os
import platform
import struct
import subprocess
import random

from Hints import buildGossipHints, buildBossRewardHints
from Utils import local_path, output_path
from Items import ItemFactory, item_data
from TextArray import text_array


def patch_rom(world, rom):

    return rom
