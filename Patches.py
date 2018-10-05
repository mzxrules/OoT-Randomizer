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


def patch_rom(world, rom):

    return rom
