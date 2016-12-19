from nose.tools import *
from gothonweb import lexicon


def test_directions():
    assert_equal(lexicon.scan("slowly"), [('direction', 'slowly')])
    result = lexicon.scan("slowly south east")
    assert_equal(result, [('direction', 'slowly'),
                        ('direction', 'south'),
                        ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("throw"), [('verb', 'throw')])
    result = lexicon.scan("shoot dodge place")
    assert_equal(result, [('verb', 'shoot'),
                        ('verb', 'dodge'),
                        ('verb', 'place')])


def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the a of")
    assert_equal(result, [('stop', 'the'),
                        ('stop','a'),
                        ('stop', 'of')])


def test_nouns():
    assert_equal(lexicon.scan("bomb"), [('noun', 'bomb')])
    result = lexicon.scan("bomb joke")
    assert_equal(result, [('noun', 'bomb'),
                        ('noun', 'joke')])

def test_numbers():
    assert_equal(lexicon.scan("132"), [('number', 132)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                        ('number', 91234)])


def test_errors():
    assert_equal(lexicon.scan("ASDFSDFASDF"), [('error', 'ASDFSDFASDF')])
    result = lexicon.scan("bomb IAS joke")
    assert_equal(result, [('noun', 'bomb'),
                        ('error', 'IAS'),
                        ('noun', 'joke')])
