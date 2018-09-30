import copy
from enum import Enum, unique
import logging
from collections import OrderedDict

"""
World object:
Creates the world we're gonna start with and which will be populated.
Contains the following:
  - All settings/flags set as options
  - The state to track what has been collected
  - Locations
  - Entrances
  - Regions
We might need a better name for Locations/Regions/Entrances,
because they're all words that mean "places" while describing very
different things.
"""
class World(object):

"""
`moon` -> variable on which the "beatable" settings is set,
          like Ganon's bridge in OoT being beatable 'vanilla',
          or 'all medallions' etc.
`open_*` -> flags as settings to be set as options in OoT
`place_dungeon_items` -> if False, wouldn't add dungeon items (map and compass)
`check_beatable_only` -> if True, would only require game to be beatable
                         if False, would require game to be completable.
`hints` -> option to set stones to give hints or not.
           (isn't used anywhere, but used for some `Location.access_rule`s in ZOoTR)
"""
    def __init__( self
                , moon
                , open_ocarina
                , shuffle_owls
                , place_dungeon_items
                , check_beatable_only
                , hints):
        self.shuffle = 'vanilla' # option for entrance shuffle
        self.moon = moon         # beatable requirement option
        self.dungeons = []       # contains dungeons for dungeon item pools
        self.regions = []        # contains all regions
        self.itempool = []       # items to be placed
        self.seed = None         # the random seed number
        self.state = CollectionState(self) # collection tracking state
        self._cached_locations = None # internally used by `get_locations`
        self._entrance_cache = {} # internally used by `get_entrance`
        self._region_cache = {}  # internally used by `get_region`
        self._location_cache = {} # internally used by `get_location`
        self.required_locations = [] # used for statistical analysis (`create_playthrough`)
        self.check_beatable_only = check_beatable_only
        self.place_dungeon_items = place_dungeon_items
        self.open_ocarina = open_ocarina
        self.shuffle_owls = shuffle_owls
        self.hints = hints
        self.keysanity = False   # option for keysanity
        self.can_take_damage = True # isn't actually used anywhere???
        self.spoiler = Spoiler(self) # object to create spoiler log

    # Makes the world fetchable from all regions
    def intialize_regions(self):
        for region in self.regions:
            region.world = self

    # Checks if `regionname` is actually a Region
    # If not, will try to find that name in `World.regions` if
    # you only gave the name of the Region and cache it to
    # be easily fetched later in `_regions_cache`
    def get_region(self, regionname):
        if isinstance(regionname, Region):
            return regionname
        try:
            return self._region_cache[regionname]
        except KeyError:
            for region in self.regions:
                if region.name == regionname:
                    self._region_cache[regionname] = region
                    return region
            raise RuntimeError('No such region %s' % regionname)

    # Similar to `get_region` but for Entrances
    def get_entrance(self, entrance):
        if isinstance(entrance, Entrance):
            return entrance
        try:
            return self._entrance_cache[entrance]
        except KeyError:
            for region in self.regions:
                for exit in region.exits:
                    if exit.name == entrance:
                        self._entrance_cache[entrance] = exit
                        return exit
            raise RuntimeError('No such entrance %s' % entrance)

    # Similar to `get_region` but for Locations
    def get_location(self, location):
        if isinstance(location, Location):
            return location
        try:
            return self._location_cache[location]
        except KeyError:
            for region in self.regions:
                for r_location in region.locations:
                    if r_location.name == location:
                        self._location_cache[location] = r_location
                        return r_location
        raise RuntimeError('No such location %s' % location)

    '''
    Create the CollectionState.
    Goes through all items and collects all advancement items
    and keys into `.prog_items` of the CollectionState.

    Also does `sweep_for_events`
    and `clear_cache_unreachable` before returning the CollectionState.
    '''
    def get_all_state(self, keys=False):
        ret = CollectionState(self)

        def soft_collect(item):
            if item.advancement or item.key:
                ret.prog_items.append(item.name)

        for item in self.itempool:
            soft_collect(item)
        from Items import ItemFactory
        if keys:
            for item in ItemFactory(['Small Key (Woodfall Temple)'] +
                                    ['Boss Key (Woodfall Temple)'
                                    ,'Boss Key (Snowhead Temple)'
                                    ,'Boss Key (Great Bay Temple)'
                                    ,'Boss Key (Stone Tower Temple)'
                                    ] +
                                    ['Small Key (Stone Tower Temple)'] * 3 +
                                    ['Small Key (Snowhead Temple)'] * 3 +
                                    ['Small Key (Great Bay Temple)']):
                soft_collect(item)
        ret.sweep_for_events()
        ret.clear_cached_unreachable()
        return ret

    # Returns all items already placed and the ones still to be placed.
    # so basically, all items.
    def get_items(self):
        return [loc.item for loc
                in self.get_filled_locations()] + self.itempool

    # Takes an item(name?) and gives the location(s) where
    # that item can be found.
    def find_items(self, item):
        return [location for location
                in self.get_locations()
                        if location.item is not None
                                        and location.item.name == item]


    # Takes a Location and an Item and tries to put the item in the
    # Location using `location.can_fill`.
    # If collect isn't set to False, also adds the location to
    # `CollectionState.locations_checked` and more
    # (see `CollectionState.collect`)
    def push_item(self, location, item, collect=True):
        if not isinstance(location, Location):
            location = self.get_location(location)

        if location.can_fill(self.state, item, False):
            location.item = item
            item.location = location
            if collect:
                self.state.collect(item, location.event, location)

            logging.getLogger('').debug('Placed %s at %s', item, location)
        else:
            raise RuntimeError('Cannot assign item %s to location %s.' % (item, location))

    # Initializes all locations found in the provided World.regions
    # into `_cached_locations` and returns all locations.
    def get_locations(self):
        if self._cached_locations is None:
            self._cached_locations = []
            for region in self.regions:
                self._cached_locations.extend(region.locations)
        return self._cached_locations

    # Like it says, returns all item locations that aren't filled yet
    def get_unfilled_locations(self):
        return [location for location
                in self.get_locations()
                        if location.item is None]

    # Like above, but returns the ones that ARE filled already.
    def get_filled_locations(self):
        return [location for location
                in self.get_locations()
                        if location.item is not None]

    # Returns all reachable locations from the provided state
    # OR if None give, from the World.state.
    def get_reachable_locations(self, state=None):
        if state is None:
            state = self.state
        return [location for location
                in self.get_locations()
                        if state.can_reach(location)]

    # Same as `get_reachable_locations`, but returns all
    # locations where there's no item and it's reachable.
    def get_placeable_locations(self, state=None):
        if state is None:
            state = self.state
        return [location for location
                in self.get_locations()
                        if location.item is None
                                        and state.can_reach(location)]

    # Checks to see if this item unlocks any new Location
    def unlocks_new_location(self, item):
        # Create hypothetical state
        temp_state = self.state.copy()
        # (Still not sure what this does)
        temp_state.clear_cached_unreachable()
        # Update hypothetical state as if we got the item.
        temp_state.collect(item, True)

        for location in self.get_unfilled_locations():
            # Check in all locations if we can reach it now (hypothetically)
            # and can't without the item (still the actual `.state`)
            if temp_state.can_reach(location) and not self.state.can_reach(location):
                return True

        return False

    # Checks if the win condition has been satisfied.
    # Used to ignore `location.can_reach` when `beatable_only` is set.
    def has_beaten_game(self, state):
        if state.has('Majora Mask'):
            return True
        return False

    # Uses the given state or a fresh `CollectionState` and checks if
    # the game is beatable by going through all reachable locations
    # and collecting items until Majora's Mask is reachable, or not.
    def can_beat_game(self, starting_state=None):
        if starting_state:
            state = starting_state.copy()
        else:
            state = CollectionState(self)

        if self.has_beaten_game(state):
            return True

        # Get all Locations where the item is filled
        # AND the item is an advancement or event item
        # AND this location isn't already in `.locations_checked`
        prog_locations = [location for location
                          in self.get_locations()
                                if location.item is not None
                                                and (location.item.advancement or location.event)
                                                and location not in state.locations_checked]

        # Go through all important but still unchecked locations
        while prog_locations:
            # Build up spheres of collection radius.
            # Everything in each sphere is independent from each other
            # in dependencies and only depends on lower spheres
            sphere = []

            # Check if any of the reachable locations contains Majora's Mask
            for location in prog_locations:
                if state.can_reach(location):
                    if location.item.name == 'Majora Mask':
                        return True
                    sphere.append(location)

            if not sphere:
                # ran out of places and did not find Majora's Mask yet, quit
                return False

            # Collect all items from the reachable locations and remove
            # them from `prog_locations` and try again.
            for location in sphere:
                prog_locations.remove(location)
                state.collect(location.item, True, location)

        return False

    # This isn't used anywhere... (???)
    @property
    def option_identifier(self):
        id_value = 0
        id_value_max = 1

        def markbool(value):
            nonlocal id_value, id_value_max
            id_value += id_value_max * bool(value)
            id_value_max *= 2
        def marksequence(options, value):
            nonlocal id_value, id_value_max
            id_value += id_value_max * options.index(value)
            id_value_max *= len(options)
        markbool(self.place_dungeon_items)
        marksequence(['ganon', 'pedestal', 'dungeons'], self.bridge)
        marksequence(['vanilla', 'simple'], self.shuffle)
        markbool(self.check_beatable_only)
        assert id_value_max <= 0xFFFFFFFF
        return id_value

'''
CollectionState object:
Keeps track of all Items/Regions/Entrances/Locations/Events/etc.
while filling in the items in the Locations in the World.
'''
class CollectionState(object):

    def __init__(self, parent):
        self.prog_items = []        # Item progression: items collected so far
        self.world = parent         # World object
        self.region_cache = {}      # Cache used when `CollectionState.can_reach` is called
        self.location_cache = {}    # Cache used when `CollectionState.can_reach` is called
        self.entrance_cache = {}    # Cache used when `CollectionState.can_reach` is called
        self.recursion_count = 0    # Used to stop infinite loops when calling `can_reach`
        self.events = []            # Event progression: events done/collected so far
        self.path = {}              # Regions/Entrances/Locations accessible so far
        self.locations_checked = set() # Set of all checked Locations


    def clear_cached_unreachable(self):
        # we only need to invalidate results which were False, places we could reach before we can still reach after adding more items
        self.region_cache = {k: v for k, v in self.region_cache.items() if v}
        self.location_cache = {k: v for k, v in self.location_cache.items() if v}
        self.entrance_cache = {k: v for k, v in self.entrance_cache.items() if v}

    # Make a copy of the current state
    def copy(self):
        ret = CollectionState(self.world)
        ret.prog_items = copy.copy(self.prog_items)
        ret.region_cache = copy.copy(self.region_cache)
        ret.location_cache = copy.copy(self.location_cache)
        ret.entrance_cache = copy.copy(self.entrance_cache)
        ret.events = copy.copy(self.events)
        ret.path = copy.copy(self.path)
        ret.locations_checked = copy.copy(self.locations_checked)
        return ret

    '''
    Takes a Region/Entrance/Location
    (Or a name of a R/E/L, and default to Region. If the name is of
    an Entrance or Location, `resolution_hint` should be set to either
    'Entrance' or 'Location')

    Does the following:
    - Checks if we tried to reach this spot already
        (R/E/L's implementation of `can_reach` also uses the `CollectionState.can_reach`
    - If the spot is already in the cache for that spot, return that (will be False if present)
    - Check the `can_reach` of that spot (while increasing the `recursion_count`)
        - If it's reachable, done.
        - If not, put it in the cache as unreachable
            (unless we're still in a recursion, because that means we were checking
             the accessability of a different spot:
                - Regions check Entrances
                - Entrances and Locations check Regions
            )
    '''
    def can_reach(self, spot, resolution_hint=None):
        try:
            spot_type = spot.spot_type
            if spot_type == 'Location':
                correct_cache = self.location_cache
            elif spot_type == 'Region':
                correct_cache = self.region_cache
            elif spot_type == 'Entrance':
                correct_cache = self.entrance_cache
            else:
                raise AttributeError
        except AttributeError:
            # try to resolve a name
            if resolution_hint == 'Location':
                spot = self.world.get_location(spot)
                correct_cache = self.location_cache
            elif resolution_hint == 'Entrance':
                spot = self.world.get_entrance(spot)
                correct_cache = self.entrance_cache
            else:
                # default to Region
                spot = self.world.get_region(spot)
                correct_cache = self.region_cache

        if spot.recursion_count > 0:
            return False

        if spot not in correct_cache:
            # for the purpose of evaluating results, recursion is resolved by always denying recursive access (as that ia what we are trying to figure out right now in the first place
            spot.recursion_count += 1
            self.recursion_count += 1
            can_reach = spot.can_reach(self)
            spot.recursion_count -= 1
            self.recursion_count -= 1

            # we only store qualified false results (i.e. ones not inside a hypothetical)
            if not can_reach:
                if self.recursion_count == 0:
                    correct_cache[spot] = can_reach
            else:
                correct_cache[spot] = can_reach
            return can_reach
        return correct_cache[spot]

    # Checks to see if any of the event Locations that have an item
    # are reachable, and considers them done/collected.
    def sweep_for_events(self, key_only=False):
        # this may need improvement
        new_locations = True
        checked_locations = 0
        while new_locations:
            reachable_events = [location for location
                                in self.world.get_filled_locations()
                                        if location.event
                                            and (not key_only or location.item.key)
                                            and self.can_reach(location)]
            for event in reachable_events:
                if event.name not in self.events:
                    self.events.append(event.name)
                    self.collect(event.item, True, event)
            new_locations = len(reachable_events) > checked_locations
            checked_locations = len(reachable_events)

    # Check if the given (number of) item(s) is in `.prog_items`
    def has(self, item, count=1):
        if count == 1:
            return item in self.prog_items
        return self.item_count(item) >= count

    # Count how many duplicates of an item are in `.prog_items`
    # (Used in `heart_count` and `has`)
    def item_count(self, item):
        return len([pritem for pritem
                    in self.prog_items
                            if pritem == item]
                  )

    # Checks if explosions are possible given the current state.
    def can_blast(self):
        return self.form('Human') and (self.has('Bomb Bag') or self.has('Blast Mask'))

    # Checks if bottles have been obtained
    def has_bottle(self):
        return self.bottle_count > 0

    # Counts the number of bottles in `.prog_items`
    def bottle_count(self):
        return len([pritem for pritem
                    in self.prog_items
                            if pritem.startswith('Bottle')]
                  )

    # Checks if the current heart count is equal or higher than the given `count` number
    def has_hearts(self, count):
        # Warning: This only considers items that are marked as advancement items
        # (Vlix' comment: I don't know what this comment above means, but I'll keep it in)
        return self.heart_count() >= count

    # Checks if paper has been obtained.
    def has_paper(self):
        paper_list = [ 'Town Title Deed'
                     , 'Swamp Title Deed'
                     , 'Mountain Title Deed'
                     , 'Ocean Title Deed'
                     , 'Letter to Mama'
                     , 'Letter to Anju']  # TODO: needs more?
        for p in paper_list:
            if self.has(p):
                return True
        return False

    # TODO: consider can_wear(mask_name), rather than just using has(item)
    # would do a check to see if you have the mask and can do human form

    # Checks to see if balloons are poppable.
    def can_pop_balloon(self):
        # TODO: test for other ways of popping balloons (in the air)
        return self.form('Zora')
            or (self.form('Deku') and self.has('Magic Meter'))
            or (self.form('Human') and (self.has('Bow') or self.has('Hookshot')))

    # Gives the number of current full hearts
    def heart_count(self):
        # Warning: This only considers items that are marked as advancement items
        return (
            self.item_count('Heart Container')
            + self.item_count('Piece of Heart') // 4
            + 3 # starting hearts
        )

    # Checks if the given form is accessable.
    def form(self, form):
        if form == 'Deku':
            return self.has('Deku Mask')
        if form == 'Goron':
            return self.has('Goron Mask')
        if form == 'Zora':
            return self.has('Zora Mask')
        # TODO: This probably needs to change to something like:
        # `starting_form('Human') or has('Song of Healing')`
        # (or instead of Song of Healing, just Ocarina, or 'Cured by HMS' or something)
        if form == 'Human':
            return self.has('Fierce Deity Mask')

    # Checks to see if fire can be generated autonomously
    def has_fire_source(self):
        return self.has('Bow') and self.has('Fire Arrows') and self.has('Magic Meter')

    # Not used anywhere, but used in ZOoTR in `Location.access_rule`s as a requirement?
    def guarantee_hint(self):
        return(self.has('Mask of Truth') or not self.world.hints)

    '''
    Considers given Item as collected.
    - If given a Location, adds the location to `.locations_checked`
    - If `event` is set to True or Item is an advancement item,
        will add the item to `.prog_items`
    - If added to `.prog_items` gets rid of all cached unreachable
        Locations and, if not from an event, checks for newly accessable
        events and again clears the unreachable caches.
    '''
    def collect(self, item, event=False, location=None):
        if location:
            self.locations_checked.add(location)
        changed = False
        if item.name.startswith('Bottle'):
            if self.bottle_count() < 6:
                self.prog_items.append(item.name)
                changed = True
        elif event or item.advancement:
            self.prog_items.append(item.name)
            changed = True

        if changed:
            self.clear_cached_unreachable()
            if not event:
                self.sweep_for_events()
                self.clear_cached_unreachable()

    # Removes the item from `.prog_items` and cleares all caches.
    # (Only used in Main.py in `create_playthrough`)
    def remove(self, item):
        if item.advancement:
            to_remove = item.name

            if to_remove is not None:
                try:
                    self.prog_items.remove(to_remove)
                except ValueError:
                    return

                # invalidate caches, nothing can be trusted anymore now
                self.region_cache = {}
                self.location_cache = {}
                self.entrance_cache = {}
                self.recursion_count = 0

    # Shortcut to call `can_reach_{location}` or `has_{item}`
    def __getattr__(self, item):
        if item.startswith('can_reach_'):
            return self.can_reach(item[10])
        elif item.startswith('has_'):
            return self.has(item[4])

        raise RuntimeError('Cannot parse %s.' % item)

# RegionType used for ordering Regions
# (not actually used for anything, afaik)
@unique
class RegionType(Enum):
    Overworld = 1
    Interior = 2
    Dungeon = 3
    Grotto = 4

    # !!! NEVER USED
    @property
    def is_indoors(self):
        """Shorthand for checking if Interior or Dungeon"""
        return self in (RegionType.Interior, RegionType.Dungeon, RegionType.Grotto)


'''
Region object:
Information about a region (e.g. South Clock Town, Termina Field, Stock Pot Inn)

Contains entrances and exits to other Regions, and item Locations.
'''
class Region(object):

    def __init__(self, name, type):
        self.name = name    # Name of the Region
        self.type = type    # RegionType set by `create_{type}_region` in Regions.py
        self.entrances = [] # Entrances that go to this Region
        self.exits = []     # Entrances found in this Region that connect to other Regions
        self.locations = [] # Item Locations found in this Region
        self.dungeon = None # True if this Region is (in) a Dungeon
        self.world = None   # World object
        self.spot_type = 'Region'
        self.recursion_count = 0 # Used to stop infinite loops when calling `can_reach`

    # Checks if this Region is reachable
    # - Checks if any of the entrances are reachable
    # - Adds itself to the `CollectionState.path` if not already in there
    def can_reach(self, state):
        for entrance in self.entrances:
            if state.can_reach(entrance):
                if not self in state.path:
                    state.path[self] = (self.name, state.path.get(entrance, None))
                return True
        return False

    # Checks to see if the item give can be filled in this Region.
    # Used to check that, if the item is a dungeon item, that this
    # Region is (in) a dungeon for it to be fillable here.
    def can_fill(self, item):
        is_dungeon_item = item.key or item.map or item.compass
        if is_dungeon_item:
            return self.dungeon and self.dungeon.is_dungeon_item(item)
        return True

    def __str__(self):
        return str(self.__unicode__())

    def __unicode__(self):
        return '%s' % self.name

'''
Entrance object:
Information about exits of Regions (being Entrances to someplace else)
'''
class Entrance(object):

    def __init__(self, name='', parent=None):
        self.name = name            # Name of the Entrance
        self.parent_region = parent # Region this Entrance is in
        self.connected_region = None # Region this Entrance connects to
        self.target = None          # Only used in Rom.py (???)
        self.addresses = None       # Only used in Rom.py (???)
        self.spot_type = 'Entrance'
        self.recursion_count = 0    # Used to stop infinite loops when calling `can_reach`
        self.vanilla = None         # !!! NEVER USED
        # Function that takes a state and determines if the Entrance is reachable
        self.access_rule = lambda state: True

    # Checks if the Entrance is reachable
    # - Checks `self.access_rule` and if the region this Entrance is in is reachable
    # - Then, if not already in `CollectionState.path`, inserts itself into the path
    def can_reach(self, state):
        if self.access_rule(state)
                and state.can_reach(self.parent_region):
            if not self in state.path:
                state.path[self] = ( self.name
                                   , state.path.get( self.parent_region
                                                   , (self.parent_region.name, None)
                                                   )
                                   )
            return True

        return False

    # Connect this Entrance to the given Region. Also adds this Entrance
    # to the `.entrances` of the given Region.
    # (optional overriding of addresses/target/vanilla)
    def connect(self, region, addresses=None, target=None, vanilla=None):
        self.connected_region = region
        self.target = target
        self.addresses = addresses
        self.vanilla = vanilla
        region.entrances.append(self)

    def __str__(self):
        return str(self.__unicode__())

    def __unicode__(self):
        return '%s' % self.name

'''
Dungeon object:
Information about a dungeon.

Used to check what kind of items need to be limited to Dungeons
'''
class Dungeon(object):

    def __init__(self, name, regions, boss_key, small_keys, dungeon_items):
        self.name = name                # Name of the Dungeon
        self.regions = regions          # Regions inside the Dungeon
        self.boss_key = boss_key        # 'Boss Key' item (if applicable)
        self.small_keys = small_keys    # All 'Small Key's of the Dungeon
        self.dungeon_items = dungeon_items # Other items in this Dungeon (e.g. Map/Compass)

    # Returns all Small and Boss keys of this Dungeon
    @property
    def keys(self):
        return self.small_keys + ([self.boss_key] if self.boss_key else [])

    # Returns all items in this Dungeon (Keys and others)
    @property
    def all_items(self):
        return self.dungeon_items + self.keys

    # Returns the name of the item, if the item is found in `self.all_items`
    def is_dungeon_item(self, item):
        return item.name in [dungeon_item.name for dungeon_item in self.all_items]

    def __str__(self):
        return str(self.__unicode__())

    def __unicode__(self):
        return '%s' % self.name


'''
Location object:
Information about the location where an item can be or is placed.

!!! Type of Location is only used in Rom.py to differentiate
between handling of certain Locations.

* `.default` is only used at the bottom of Rom.py. unclear
'''
class Location(object):

    def __init__( self
                , name=''       # Name of the Location
                , address=None  # Hex address of Location
                , address2=None # Secondary hex address of Location
                , default=None  # Default hex code (???)
                , type='Chest'  # Type of Location
                , parent=None): # Region this Location is in
        self.name = name
        self.parent_region = parent
        self.item = None        # Item filled in this Location
        self.address = address
        self.address2 = address2
        self.default = default
        self.type = type
        self.spot_type = 'Location'
        self.recursion_count = 0 # Used to stop infinite loops when calling `can_reach`
        self.staleness_count = 0 # !!! NEVER USED
        self.event = False      # Is this Location an event
        # Function that takes an item and a state and determines
        # if the item can (always) be filled into this Location.
        self.always_allow = lambda item, state: False
        # Function that takes a state and determines if the Location is reachable
        self.access_rule = lambda state: True
        # Function that takes an item and determines if the item
        # can be filled into this Location
        self.item_rule = lambda item: True

    '''
    Takes a state and item and checks if the item can be filled into this Location.
    - Checks if it is always allowed (`self.always_allow`) or
    - Checks if the item is a dungeon item
        - if so, checks if the Location is in a dungeon
        - if not, uses `self.item_rule` and `self.can_reach` to determine
          whether it's fillable.

    * Check_access can be set to False to ignore the `self.can_reach` rule
      This is done when `has_beaten_game` is True and `beatable_only` is set.
    '''
    def can_fill(self, state, item, check_access=True):
        return self.always_allow(item, self)
                or (self.parent_region.can_fill(item)
                    and self.item_rule(item)
                    and (not check_access or self.can_reach(state))
                   )

    # Like `can_fill`, but only checks `self.item_rule`
    def can_fill_fast(self, item):
        return self.item_rule(item)

    # Checks to see if the Location is reachable.
    # Uses `self.access_rule` and checks if the Region this Location
    # is in is also reachable.
    def can_reach(self, state):
        if self.access_rule(state)
                and state.can_reach(self.parent_region):
            return True
        return False

    def __str__(self):
        return str(self.__unicode__())

    def __unicode__(self):
        return '%s' % self.name

'''
Item Object:
Information about an item.
Examples of these can be found in Items.py (`item_table`)
(`code` and `index` are used in Rom.py for "fix"es
and changing values at `location.address`es)
'''
class Item(object):

    def __init__( self
                , name=''           # Name of the item
                , advancement=False # Is the item needed to progress
                , priority=False    # Does the item have priority (???)
                , type=None         # Type of the item ('SmallKey', 'BossKey', 'Map', 'Compass')
                                    # - Only really used in Main.py and Dungeons.py
                                    # - Also used to label Hints.
                , code=None         # Hex code (???) of the item
                , index=None):      # Index (???) of the item
        self.name = name
        self.advancement = advancement
        self.priority = priority
        self.type = type
        self.code = code
        self.index = index
        self.location = None        # Location of the item (set when filled)

    # Returns True if the item is either a 'SmallKey' or 'BossKey'
    @property
    def key(self):
        return self.type == 'SmallKey' or self.type == 'BossKey'

    # DEPRECATED DEPRECATED DEPRECATED DEPRECATED
    # `crystal` not used anywhere. I opt for removing this function
    # DEPRECATED DEPRECATED DEPRECATED DEPRECATED
    @property
    def crystal(self):
        return self.type == 'Crystal'

    # Returns True is item is a 'Map'
    @property
    def map(self):
        return self.type == 'Map'

    # Returns True is item is a 'Compass'
    @property
    def compass(self):
        return self.type == 'Compass'

    def __str__(self):
        return str(self.__unicode__())

    def __unicode__(self):
        return '%s' % self.name

'''
Spoiler object:

'''
class Spoiler(object):

    def __init__(self, world):
        self.world = world      # World object
        self.entrances = []     # Entrances for "Entrance Shuffle"
        self.playthrough = {}   # Playthrough of accessable areas/spheres and the items in them
        self.locations = {}     # Locations of all items
        self.paths = {}         # Paths through all regions and exits
        self.metadata = {}      # Settings of this spoiler/randomization

    # USED IN ENTRANCE SHUFFLE
    # Adds a Entrance/Exit/Direction combination to `self.entrances`
    def set_entrance(self, entrance, exit, direction):
        self.entrances.append(OrderedDict([ ('entrance', entrance)
                                          , ('exit', exit)
                                          , ('direction', direction)]
                                         )
                             )

    # Sets `self.locations` to a combination of (Location name, Item name)
    # for all items not in the list seen in the for loop.
    # Also sets the metadata to reflect the initial options.
    def parse_data(self):
        spoiler_locations = []
        for location in self.world.get_locations():
            # TODO: Needs to be updated for MM
            # All item Locations that AREN'T to be added to the spoiler log
            if location.item.name not in [ 'Gold Skulltulla Token'
                                         , 'Epona'
                                         , 'Majora Mask'
                                         , 'Fairy Ocarina'
                                         , 'Ocarina of Time'
                                         , 'Zeldas Letter'
                                         , 'Master Sword'
                                         , 'Magic Bean'
                                         , 'Gerudo Membership Card'
                                         , 'Forest Trial Clear'
                                         , 'Fire Trial Clear'
                                         , 'Water Trial Clear'
                                         , 'Shadow Trial Clear'
                                         , 'Spirit Trial Clear'
                                         , 'Light Trial Clear']:
                spoiler_locations.append(location)
        sort_order = {"Song": 0, "Boss": -1}
        # Sort all items first, then songs, then bosses
        spoiler_locations.sort(key=lambda item: sort_order.get(item.type, 1))
        self.locations = {'other locations': OrderedDict(
                                [(str(location), str(location.item) if location.item is not None else 'Nothing')
                                    for location in spoiler_locations]
                                                        )
                         }
        from Main import __version__ as MMRVersion
        self.metadata = {'version': MMRVersion,
                         'seed': self.world.seed,
                         'moon': self.world.moon,
                         # TODO: needs to be updated for MM
                         'forest': self.world.open_forest,
                         'door': self.world.open_door_of_time,
                         'completeable': not self.world.check_beatable_only,
                         'dungeonitems': self.world.place_dungeon_items}

    # Prints the spoiler log to a file.
    def to_file(self, filename):
        self.parse_data()
        with open(filename, 'w') as outfile:
            outfile.write('MM Randomizer Version %s  -  Seed: %s\n\n' % (self.metadata['version'], self.metadata['seed']))
            # TODO: needs to be updated for MM
            outfile.write('Rainbow Bridge Requirement:      %s\n' % self.metadata['bridge'])
            outfile.write('Open Forest:                     %s\n' % ('Yes' if self.metadata['forest'] else 'No'))
            outfile.write('Open Door of Time:               %s\n' % ('Yes' if self.metadata['door'] else 'No'))
            outfile.write('All Locations Accessible:        %s\n' % ('Yes' if self.metadata['completeable'] else 'No, some locations may be unreachable'))
            outfile.write('Maps and Compasses in Dungeons:  %s\n' % ('Yes' if self.metadata['dungeonitems'] else 'No'))
            outfile.write('\n\nEntrances:\n\n')
            outfile.write('\n'.join(['%s %s %s' % (entry['entrance'], '<=>' if entry['direction'] == 'both' else '<=' if entry['direction'] == 'exit' else '=>', entry['exit']) for entry in self.entrances]))
            outfile.write('\n\nLocations:\n\n')
            outfile.write('\n'.join(['%s: %s' % (location, item) for (location, item) in self.locations['other locations'].items()]))
            outfile.write('\n\nPlaythrough:\n\n')
            outfile.write('\n'.join(['%s: {\n%s\n}' % (sphere_nr, '\n'.join(['  %s: %s' % (location, item) for (location, item) in sphere.items()])) for (sphere_nr, sphere) in self.playthrough.items()]))
            outfile.write('\n\nPaths:\n\n')

            path_listings = []
            for location, path in sorted(self.paths.items()):
                path_lines = []
                for region, exit in path:
                    if exit is not None:
                        path_lines.append("{} -> {}".format(region, exit))
                    else:
                        path_lines.append(region)
                path_listings.append("{}\n        {}".format(location, "\n   =>   ".join(path_lines)))

            outfile.write('\n'.join(path_listings))
