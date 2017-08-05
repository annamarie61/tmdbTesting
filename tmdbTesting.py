#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
tmdbTesting.py

tmbdTesting is test application, written in Python, for The Movie Database (TMDb) API version 3.

If you want more info on The Movie Database API, check out http://www.themoviedb.org/documentation/api

To run tests: pytest -v --apikey="<api_key>" tmdbTesting.py
"""

import json
import requests
import pytest

class apiKeyError(Exception):
	pass

paramsDict = {}
baseURL = 'https://api.themoviedb.org'
apiVersion = '3'

	# # def ___init___():
	# # 	.paramsDict['api_key'] = api_key()
	# # 	print(.paramsDict['api_key'])
	# # 	if not .paramsDict['api_key']:
	# # 		raise apiKeyError

'''
getURL return the full url path for a request

index refers to tv, movies, ect.
vid is the id for what you want

examples:
	___getURL('tv','550') returns https://api.themoviedb.org/3/tv/550
'''
def ___getURL(index,vid):
	return baseURL + '/' + apiVersion + '/' + str(index) + '/' + str(vid)

# runs the actual api request
def ___request(apikey,method,index,vid,payload=None):
	headers={'Content-Type': 'application/json','Accept': 'application/json','Connection': 'close'}
	url=___getURL(index,vid)
	if len(apikey):
		paramsDict['api_key'] = apikey
	else:
		raise apiKeyError

	response = requests.request(method,url,params=paramsDict,data=json.dumps(payload) if payload else payload,headers=headers)
	response.encoding = 'utf-8'
	return response

@pytest.mark.parametrize("test_input,expected_return_code", [
	("1",200),
	("-1",404),
	("a",404),
	("5555555555",404),
	("0",404),
])

# '''
# Verifying I can get tv info back when given a valid id or a 404 error when given an invalid id.
# Pass in a tv id to the url https://api.themoviedb.org/3/tv/.

# Expected results:
# If a valid id: 200 code returned
# If an invalid id: 404 code returned
# '''
def test_tv_info(apikey,test_input,expected_return_code):
	response = ___request(apikey,'GET','tv',test_input)
	# response.raise_for_status()
	assert len(response.json()) and response.status_code == expected_return_code

'''
Verifying I can get tv info back when given a valid id.
Pass in a valid tv id (in this case I used 550) to the url https://api.themoviedb.org/3/tv/550.

Verifying that some of the data values I got back match expected values

Expected results:
No error and actual info returned
first_air_date = "1965-07-22"
last_air_date = "1975-12-17"
original_name = "Till Death Us Do Part"
'''
def test_valid_tv_info_returned(apikey):
	response = ___request(apikey,'GET','tv','550')
	response.raise_for_status()
	assert len(response.json())
	assert response.json()['first_air_date'] == "1965-07-22"
	assert response.json()['last_air_date'] == "1975-12-17"
	assert response.json()['original_name']	== "Till Death Us Do Part"

'''
Verifying I can get tv info back when given a valid id.
Pass in a valid tv id (in this case I used 550) to the url https://api.themoviedb.org/3/tv/550.

Verifying that some of the data values do not match expected values

Expected results:
No error and actual info returned
first_air_date != "1965-07-23"
last_air_date != "1975-12-18"
original_name != "Till Death Us Do Part 2"
'''
def test_valid_tv_info_returned(apikey):
	pass
	# call the api to get data back
	# raise an error if a 404 error or similar is returned
	# verify the first air date does not equal "1965-07-23"
	# verify the last air date does not equal "1975-12-18"
	# verify the original name does not equal "Till Death Us Do Part 2"

'''
Verifying I can get tv info back when given a list of ids.
Pass in a comma separated list of tv ids (in this case I used 1,2,3) to the url https://api.themoviedb.org/3/tv/1,2,3.

Expected results:
No error and actual info returned
Multiple tv shows returned in the json
'''
def test_valid_tv_info_returned(apikey):
	pass
	# call the api to get data back
	# raise an error if a 404 error or similar is returned
	# verify I have the same number of tv shows and the number of ids passed in

'''
Verifying I do not get tv info back when given an id inside brackets.
Pass in a tv id in brackets (in this case I used [1]) to the url https://api.themoviedb.org/3/tv/[1].

Expected results:
A 404 error and status code 34 returned from application
'''
def test_valid_tv_info_returned(apikey):
	pass
	# call the api to get data back
	# verify I got a 404 error back and not a tv listing

'''
Verifying I can get movie info back when given a valid id.
Pass in a valid movie id (in this case I used 500) to the url https://api.themoviedb.org/3/movie/500.

Expected results:
No error and actual info returned
'''
def test_valid_id_movie_info(apikey):
	response = ___request(apikey,'GET','movie','500')
	response.raise_for_status()
	assert len(response.json())

'''
Verifying I do not get movie info back when given a negative movie id.
Pass in a negative movie id (in this case I used -1) to the url https://api.themoviedb.org/3/movie/-1.

Expected results:
A 404 error and status code 34 returned from application
'''
def test_negative_id_movie_info(apikey):
	response = ___request(apikey,'GET','movie','-1')
	assert len(response.json()) and response.status_code == 404

'''
Verifying I do not get movie info back when given an invalid movie id.
Pass in an invalid movie id (in this case I used a) to the url https://api.themoviedb.org/3/movie/a.

Expected results:
A 404 error and status code 34 returned from application
'''
def test_invalid_id_movie_info(apikey):
	response = ___request(apikey,'GET','movie','a')
	assert len(response.json()) and response.status_code == 404