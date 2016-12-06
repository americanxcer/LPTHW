from nose.tools import *
from app import app
from tests.tools import assert_response

client = app.test_client() # create a testing client (like a fake web browser)
client.testing = True # enable this so that errors in your web app bubble up to the testing client

def test_index():
    global client # let python know you want to use the global client variable in this function
    resp = client.get('/') # with this client you can do all kinds of stuff
    assert_response(resp, status=302) # the root url should give back a redirect

    # test to make sure a GET request to /hello works (return a 200 status code)
    resp = client.get('/game')
    assert_response(resp) # just make sure we got a valid response

    # make sure the default values work when POST has no data
    resp = client.post('/game') # use POST, but provide no data
    assert_response(resp, contains="You Died!")

    # Go to another scene in the game
    testdata = {'userinput': 'tella joke'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Laser Weapon Armory")

    # From there, go to yet another scene
    testdata = {'userinput': '132'}
    resp = client.post('/game', data = testdata)
    assert_response(resp, containts="The Bridge")

    # my code
    testdata = {'userinput': 'slowly place the bomb'}
    resp = client.post('/game', data = testdata)
    assert_response(resp, contains="Escape Pod")

    testdata = {'userinput': '2'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="You Made It!")
