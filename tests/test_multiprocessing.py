import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestMain(unittest.TestCase):
    def test_valid_request(self):
        payload = {
            "batchid": "id0101",
            "payload": [[1, 2], [3, 4]]
        }
        response = client.post("/addition/", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("batchid", data)
        self.assertIn("response", data)
        self.assertIn("status", data)
        self.assertIn("started_at", data)
        self.assertIn("completed_at", data)

    def test_empty_list(self):
        payload = {
            "batchid": "id0102",
            "payload": [[]]
        }
        response = client.post("/addition/", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["response"], [0])

    def test_single_list(self):
        payload = {
            "batchid": "id0103",
            "payload": [[5]]
        }
        response = client.post("/addition/", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["response"], [5])

    def test_negative_numbers(self):
        payload = {
            "batchid": "id0104",
            "payload": [[-1, -2], [-3, -4]]
        }
        response = client.post("/addition/", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["response"], [-3, -7])

    def test_float_numbers(self):
        payload = {
            "batchid": "id0105",
            "payload": [[1.5, 2.5], [3.5, 4.5]]
        }
        response = client.post("/addition/", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["response"], [4, 8])

    def test_invalid_request(self):
        payload = {
            "payload": [[1, 2], [3, 4]]
        }
        response = client.post("/addition/", json=payload)
        self.assertEqual(response.status_code, 422)

    def test_empty_payload(self):
        payload = {
            "batchid": "id0106",
            "payload": []
        }
        response = client.post("/addition/", json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["response"], [])

if __name__ == "__main__":
    unittest.main()
