import unittest
from simulation import simulate_ddos_attack, hide_source_ip

class TestSimulation(unittest.TestCase):
    def test_simulate_ddos_attack(self):
        self.assertIsNone(simulate_ddos_attack("192.168.0.1", 1))

    def test_hide_source_ip(self):
        spoofed_ip = hide_source_ip()
        self.assertTrue(spoofed_ip.count('.') == 3)
        self.assertTrue(all(0 < int(octet) <= 255 for octet in spoofed_ip.split('.')))

if __name__ == "__main__":
    unittest.main()