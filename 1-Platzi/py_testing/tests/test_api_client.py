import unittest
import requests
from src.api_client import get_location
from unittest.mock import patch, Mock


class ApliClientTest(unittest.TestCase):
    
    @patch("src.api_client.requests.get")
    def test_get_location_returns_correct_data(self,mock_get):
        # Mock the response from the API
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI"
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")
        

    @patch("src.api_client.requests.get")
    def test_get_location_returns_correct_data_side_effect(self,mock_get):

        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200, 
                json=lambda: {
                    "countryName": "USA",
                    "regionName": "FLORIDA",
                    "cityName": "MIAMI"
            })
        ]


        with self.assertRaises(requests.exceptions.RequestException):
            get_location("8.8.8.8")

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

    @patch("src.api_client.requests.get")
    def test_get_location_with_invalid_ip(self, mock_get):
        # Mock response for invalid IP
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("400 Client Error: Bad Request")
        mock_get.return_value = mock_response
        
        # Test that HTTPError is raised for invalid IP
        with self.assertRaises(requests.exceptions.HTTPError):
            get_location("invalid.ip.address")
        
        mock_get.assert_called_once_with("https://freeipapi.com/api/json/invalid.ip.address")

    @patch("src.api_client.requests.get")
    def test_get_location_with_empty_ip(self, mock_get):
        # Mock response for empty IP
        mock_response = Mock()
        mock_response.status_code = 400
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("400 Client Error: Bad Request")
        mock_get.return_value = mock_response
        
        # Test that HTTPError is raised for empty IP
        with self.assertRaises(requests.exceptions.HTTPError):
            get_location("")
        
        mock_get.assert_called_once_with("https://freeipapi.com/api/json/")

    @patch("src.api_client.requests.get")
    def test_get_location_with_malformed_ip(self, mock_get):
        # Mock response for malformed IP
        mock_response = Mock()
        mock_response.status_code = 422
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("422 Unprocessable Entity")
        mock_get.return_value = mock_response
        
        # Test that HTTPError is raised for malformed IP
        with self.assertRaises(requests.exceptions.HTTPError):
            get_location("999.999.999.999")
        
        mock_get.assert_called_once_with("https://freeipapi.com/api/json/999.999.999.999")