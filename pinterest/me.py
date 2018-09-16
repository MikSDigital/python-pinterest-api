from typing import Any, Dict, List

from . import config
from .util import do_request


class Me:

    def __init__(self, token):
        self.token = token

    def boards(self, fields: List[str] = None):
        """
        The default response returns an ordered list of the authenticated user’s public boards,
        including the URL, ID and name. The boards are sorted first by user order, then by creation date,
        with the most recently created boards being first.

        fields: counts, created_at, creator, description, id, image, name, privacy, reason, url

        GET /v1/me/boards/
        """
        if fields is None:
            fields = ['url', 'id', 'name']
        url = config.api_url + '/v1/me/boards/'
        params = {'access_token': self.token, 'fields': ','.join(fields)}
        return do_request('get', url, params=params).json()

    def suggest_boards(self, pin_id):
        """
        Returns the boards that Pinterest would suggest to the authenticated user if they were
        to save the specified Pin. The default response returns the ID, URL and name of the boards.

        GET /v1/me/boards/suggested/
        """
        url = config.api_url + '/v1/me/boards/suggested/'
        params = {'access_token': self.token, 'pin': pin_id}
        return do_request('get', url, params=params)

    def pins(self, cursor=None):
        """
        The default response returns the ID, link, URL and descriptions of the authenticated user’s Pins.

        GET /v1/me/pins/
        """
        url = config.api_url + '/v1/me/pins/'
        params = {'access_token': self.token}
        if cursor is not None:
            params['cursor'] = cursor
        return do_request('get', url, params=params)

    def search_boards(self, query, cursor=None):
        """
        Searches the authenticated user’s board names (but not Pins on boards).
        An empty response indicates that nothing was found that matched your search terms.
        The default response returns the ID, name and URL of boards matching your query.

        GET /v1/me/search/boards/
        """
        url = config.api_url + '/v1/me/search/boards/'
        params = {'access_token': self.token, 'query': query}
        if cursor is not None:
            params['cursor'] = cursor
        return do_request('get', url, params=params)

    def search_pins(self, query, cursor=None):
        """
        Searches the authenticated user’s Pin descriptions.
        An empty response indicates that nothing was found that matched your search terms.
        The default response returns the ID, link, URL and description of Pins matching your query.

        GET /v1/me/search/pins/
        """
        url = config.api_url + '/v1/me/search/pins/'
        params = {'access_token': self.token, 'query': query}
        if cursor is not None:
            params['cursor'] = cursor
        return do_request('get', url, params=params)

    def follow_board(self, board):
        """
        Makes the authenticated user follow the specified board.
        A empty response (or lack of error code) indicates success.

        POST /v1/me/following/boards/
        """
        url = config.api_url + '/v1/me/following/boards/'
        data = {'access_token': self.token, 'board': board}
        return do_request('post', url, data=data)

    def follow_user(self, user):
        """
        Makes the authenticated user follow the specified user.
        A empty response (or lack of error code) indicates success.

        POST /v1/me/following/users/
        """
        url = config.api_url + '/v1/me/following/users/'
        data = {'access_token': self.token, 'user': user}
        return do_request('post', url, data=data)

    def followers(self, cursor=None):
        """
        Returns the users who follow the authenticated user.
        The default response returns the first and last name, ID and URL of the users.

        GET /v1/me/followers/
        """
        url = config.api_url + '/v1/me/followers/'
        params = {'access_token': self.token}
        if cursor is not None:
            params['cursor'] = cursor
        return do_request('get', url, params=params)

    def following_boards(self, cursor=None):
        """
        Returns the boards that the authenticated user follows.
        The default response returns the ID, name and URL of the board.

        GET /v1/me/following/boards/
        """
        url = config.api_url + '/v1/me/following/boards/'
        params = {'access_token': self.token}
        if cursor is not None:
            params['cursor'] = cursor
        return do_request('get', url, params=params)

    def following_interests(self, cursor: str = None, fields: List[str] = None) -> Dict[str, Any]:
        """
        Returns the topics (e.g, modern architecture, Sherlock) that the authenticated user follows.
        The default response returns the ID and name of the topic.

        fields: id, name

        GET /v1/me/following/interests/
        """
        url = config.api_url + '/v1/me/following/interests/'
        params = {'access_token': self.token}
        if cursor is not None:
            params['cursor'] = cursor
        if fields is None:
            fields = ['id', 'name']
        params['fields'] = ','.join(fields)
        return do_request('get', url, params=params).json()

    def following_users(self, cursor: str = None, fields: List[str] = None) -> Dict[str, Any]:
        """
        Returns the users that the authenticated user follows.
        The default response returns the first and last name, ID and URL of the users.

        fields: account_type, bio, counts, created_at, first_name, id, image, last_name, url, username

        GET /v1/me/following/users/
        """
        url = config.api_url + '/v1/me/following/users/'
        params = {'access_token': self.token}
        if cursor is not None:
            params['cursor'] = cursor
        if fields is None:
            fields = ['first_name', 'id', 'last_name', 'url']
        params['fields'] = ','.join(fields)
        return do_request('get', url, params=params).json()

    def unfollow_board(self, board: str):
        """
        Makes the authenticated user unfollow the specified board.
        A empty response (or lack of error code) indicates success.

        DELETE /v1/me/following/boards/<board>/
        """
        url = config.api_url + '/v1/me/following/boards/{board}/'.format(board=board)
        data = {'access_token': self.token}
        return do_request('delete', url, data=data)

    def unfollow_user(self, user):
        """
        Makes the authenticated user unfollow the specified user.
        A empty response (or lack of error code) indicates success.

        DELETE /v1/me/following/users/<user>/
        """
        url = config.api_url + '/v1/me/following/users/{user}/'.format(user=user)
        params = {'access_token': self.token}
        return do_request('delete', url, params=params)

    def __call__(self, fields: List[str] = None):
        """
        The default response returns the first and last name, ID and URL of the authenticated user.

        fields: account_type, bio, counts, created_at, first_name, id, image, last_name, url, username

        GET /v1/me/
        """
        url = config.api_url + '/v1/me/'
        params = {'access_token': self.token}
        if fields is None:
            fields = ['first_name', 'last_name', 'id', 'url']
        params['fields'] = ','.join(fields)
        return do_request('get', url, params=params).json()
