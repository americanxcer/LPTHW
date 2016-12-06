from nose.tools import *
import re

# A useful function for asserting conditions in an HTTP response
def assert_response(resp, contains=None, matches=None, headers=None, status=200, mime=None):
    assert_equal(status, resp.status_code)

    if status == 200:
        assert resp.data, "Resonse data is empty!"
    if contains:
        assert contains in resp.data, "Response does not contain %r!" % matches
    if headers:
        assert_equal(resp.headers, headers)
    if mime:
        assert_equal(resp.mimetype, mime)
