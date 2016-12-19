from nose.tools import *
from map import *

def test_room():
    gold = Scene("GoldScene", "goldroom", "normal",
     """
    This room has gold in it you can grab. There's a door
    to the north.
    """)
    assert_equal(gold.title, "GoldScene")
    assert_equal(gold.urlname, "goldroom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Scene("Center", "center", "normal", "Test room in the center.")
    north = Scene("North", "north", "normal", "Test room in the north.")
    south = Scene("South", "south", "normal", "Test room in the south.")

    center.add_paths({'north':north, 'south': south}) #no space?
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Scene("Start", "start", "begin", "You can go west and down a hole.")
    west = Scene("Trees", "trees", "normal", "There are trees here, you can go east.")
    down = Scene("Dungeon","dungeon", "normal", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east':start}) #no space?
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_drinking_game_map():
    assert_equal(intro.go('out'), outside)
    assert_equal(intro.go('go out'), outside)
    assert_equal(intro.go('stay home'), inside_sober)
    assert_equal(intro.go('home'), inside_sober)
    assert_equal(intro.go('help'), help_out_in)

    assert_equal(outside.go('rewe'), rewe)
    assert_equal(outside.go('Rewe'), rewe)
    assert_equal(outside.go('to rewe'), rewe)
    assert_equal(outside.go('to Rewe'), rewe)
    assert_equal(outside.go('the bar'), bar_sober)
    assert_equal(outside.go('the soccer bar'), bar_sober)
    assert_equal(outside.go('bar'), bar_sober)
    assert_equal(outside.go('soccer bar'), bar_sober)
    assert_equal(outside.go('help'), help_rewe_bar)

    assert_equal(rewe.go('the bar'), way_bar)
    assert_equal(rewe.go('the soccer bar'), way_bar)
    assert_equal(rewe.go('bar'), way_bar)
    assert_equal(rewe.go('soccer bar'), way_bar)
    assert_equal(rewe.go('go home'), way_inside)
    assert_equal(rewe.go('just go home'), way_inside)
    assert_equal(rewe.go('home'), way_inside)
    assert_equal(rewe.go('help'), help_home_bar)

    assert_equal(way_bar.go('0'), bar_sober)
    assert_equal(way_bar.go('1'), bar_sober)
    assert_equal(way_bar.go('2'), bar_sober)
    assert_equal(way_bar.go('3'), bar_buzzed)
    assert_equal(way_bar.go('4'), bar_buzzed)
    assert_equal(way_bar.go('5'), bar_buzzed)
    assert_equal(way_bar.go('6'), bar_buzzed)
    assert_equal(way_bar.go('7'), bar_buzzed)
    assert_equal(way_bar.go('8'), way_drunk)
    assert_equal(way_bar.go('9'), way_drunk)
    assert_equal(way_bar.go('10'), way_drunk)
    assert_equal(way_bar.go('11'), way_drunk)
    assert_equal(way_bar.go('12'), way_drunk)
    assert_equal(way_bar.go('help'), help_way_bar)

    assert_equal(way_inside.go('0'), inside_sober)
    assert_equal(way_inside.go('1'), inside_sober)
    assert_equal(way_inside.go('2'), inside_sober)
    assert_equal(way_inside.go('3'), inside_buzzed)
    assert_equal(way_inside.go('4'), inside_buzzed)
    assert_equal(way_inside.go('5'), inside_buzzed)
    assert_equal(way_inside.go('6'), inside_buzzed)
    assert_equal(way_inside.go('7'), inside_buzzed)
    assert_equal(way_inside.go('8'), way_drunk)
    assert_equal(way_inside.go('9'), way_drunk)
    assert_equal(way_inside.go('10'), way_drunk)
    assert_equal(way_inside.go('11'), way_drunk)
    assert_equal(way_inside.go('12'), way_drunk)
    assert_equal(way_inside.go('help'), help_way_inside)

    assert_equal(inside_buzzed.go('yes'), inside_buzzed_invite)
    assert_equal(inside_buzzed.go('Yes'), inside_buzzed_invite)
    assert_equal(inside_buzzed.go('no'), inside_buzzed_alone)
    assert_equal(inside_buzzed.go('No'), inside_buzzed_alone)
    assert_equal(inside_buzzed.go('help'), help_invite_buzzed)

    assert_equal(inside_sober.go('yes'), inside_sober_invite)
    assert_equal(inside_sober.go('Yes'), inside_sober_invite)
    assert_equal(inside_sober.go('no'), inside_sober_alone)
    assert_equal(inside_sober.go('No'), inside_sober_alone)
    assert_equal(inside_sober.go('help'), help_invite_sober)
