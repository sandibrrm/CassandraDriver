# test_cassandradriver.py
"""
Tests for CassandraDriver module.
"""

import unittest
from cassandradriver import CassandraDriver

class TestCassandraDriver(unittest.TestCase):
    """Test cases for CassandraDriver class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CassandraDriver()
        self.assertIsInstance(instance, CassandraDriver)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CassandraDriver()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
