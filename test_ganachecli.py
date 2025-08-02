# test_ganachecli.py
"""
Tests for GanacheCLI module.
"""

import unittest
from ganachecli import GanacheCLI

class TestGanacheCLI(unittest.TestCase):
    """Test cases for GanacheCLI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GanacheCLI()
        self.assertIsInstance(instance, GanacheCLI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GanacheCLI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
