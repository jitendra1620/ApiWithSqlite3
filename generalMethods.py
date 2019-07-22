from flask import Flask, jsonify, request, make_response


class GeneralMethods():
    @staticmethod
    def checkIfHederKeyunauthorized(headers):
	    headerKey = headers.get('X-API-Key')
	    try:
	        if headerKey is None:  # The variable
	            response = jsonify({"error": "unauthorized."})
	            response.status_code = 403
	            return response
	    except NameError:
	        response = jsonify({"error": "unauthorized."})
	        response.status_code = 403
	        return response
	    else:
	        return None
