from nose.tools import *
from app import app
from tests.tools import assert_response

client = app.test_client() # create a testing client (like a fake web browser)
client.testing = True # enable this so that errors in your web app bubble up to the testing client

def test_index():
    global client # let python know you want to use the global client variable in this function
    resp = client.get('/') # with this client you can do all kinds of stuff
    assert_response(resp, status=302) # the root url should give back a redirect,needs to be redirected, see app.py 44- 47

    # test to make sure a GET request to /hello works (return a 200 status code)
    resp = client.get('/game')
    assert_response(resp) # just make sure we got a valid response

    # make sure the default values work when POST has no data
    resp = client.post('/game') # use POST, but provide no data
    assert_response(resp, contains="Come On!")

    # Go to another scene in the game, testing that we're landing on the right scene
    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Laser Weapon Armory")

    # From there, go to yet another scene
    testdata = {'userinput': '132'}
    resp = client.post('/game', data = testdata)
    assert_response(resp, contains="The Bridge")

    # my code
    testdata = {'userinput': 'slowly place the bomb'}
    resp = client.post('/game', data = testdata)
    assert_response(resp, contains="Escape Pod")

    testdata = {'userinput': '2'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="You Made It!")

    testdata = {'userinput': 'blah blah'}  #if userinput doesnt translate in the game
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Try Again!")


    #testdata = {'userinput': 'throw the bomb'}
    #resp = client.post('/game', data=testdata)
    #assert_response(resp, contains="Throw Death")

    # testdata = {'userinput': 'dodge!'}
    # resp = client.post('/game', data=testdata)
    # assert_response(resp, contains="Dodge Death")
    #
    # testdata = {'userinput': '*'}
    # resp = client.post('/game', data=testdata)
    # assert_response(resp, contains="Code Fail Death")
    #
    # testdata = {'userinput': 'throw the bomb'}
    # resp = client.post('/game', data=testdata)
    # assert_response(resp, contains="Throw Death")
