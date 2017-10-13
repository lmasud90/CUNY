# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:56:43 2017

@author: latif
"""

import requests

endpoint = "https://api.test.sabre.com/v2/shop/flights/fares"

params = {
        "origin": "JFK",
        "destination": "LAX",
        "lengthofstay": "5",
        "pointofsalecountry": "US"
        }

headers = {"Authorization":"Bearer T1RLAQIDSStlpKs2hHIu4zBicNT7z69vbRDbq7wQrvk2m0NTjbV7vlI+AADAyc/MiHaSYoo3GqSnigD2y++SWbiolECubaAoSp3xxfDjus0fKRf20RJOIQMKwFwE8c+E3r5/5moBSh/zOO7WTIZBUxqN5rlnwDFUx6xk7VY/oeQ0SVEUfNC/hxXy3Er5bMgl2awBp7W8hkNwnRcEwMedzRJrcro72l4VGApULInEf5rL02Dxy1ZNLMyiU2h5BV7L1+3QDifVUfqPZGlXo7SPugTlMMByBtO1o0+fXLs7k8EF+j1HSukH8SVLkGgX"}

print requests.get(endpoint,params=params,headers=headers).json()