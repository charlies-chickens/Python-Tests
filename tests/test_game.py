import unittest
from models import KeyCoin, ComputingArchitect, NanoEngineer, CyberneticOperative, BioIntegrator, QuantumTrader
from main import City

class TestKeyCoin(unittest.TestCase):
    def test_initial_state(self):
        kc = KeyCoin()
        self.assertEqual(kc.evolution_level, 1)
        self.assertEqual(kc.experience, 0)
        self.assertIn("Basic Access", kc.powers)

    def test_gain_experience(self):
        kc = KeyCoin()
        kc.gain_experience(50)
        self.assertEqual(kc.experience, 50)
        self.assertEqual(kc.evolution_level, 1)

    def test_evolution(self):
        kc = KeyCoin()
        kc.gain_experience(100)
        self.assertEqual(kc.evolution_level, 2)
        self.assertEqual(kc.experience, 0)
        self.assertIn("Enhanced Tier 2", kc.powers)

class TestRoles(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def test_computing_architect(self):
        ca = ComputingArchitect("Alice")
        self.assertEqual(ca.name, "Alice")
        self.assertEqual(ca.role, "Computing Architect")

        self.assertEqual(ca.quantum_hack(self.city), "City systems overridden.")
        self.assertEqual(ca.keycoin_sync(self.city), "KeyCoin linked to AI entities.")
        self.assertEqual(ca.data_construct(self.city), "Temporary AI minion created.")
        self.assertEqual(ca.keycoin.experience, 75)
        self.assertEqual(self.city.sectors["AI Core"], 15)

    def test_nano_engineer(self):
        ne = NanoEngineer("Bob")
        self.assertEqual(ne.nano_swarm(self.city), "Nanobots deployed for repair/damage.")
        self.assertEqual(ne.key_infusion(self.city), "KeyCoin embedded into tech.")
        self.assertEqual(ne.mini_factory(self.city), "Portable mini-factory produced.")
        self.assertEqual(ne.keycoin.experience, 75)
        self.assertEqual(self.city.sectors["Energy Grid"], 15)

    def test_cybernetic_operative(self):
        co = CyberneticOperative("Charlie")
        self.assertEqual(co.phase_cloak(self.city), "Became temporarily invisible.")
        self.assertEqual(co.keycoin_disruptor(self.city), "Enemy networks weakened.")
        self.assertEqual(co.neural_jack(self.city), "Abilities stolen from target.")
        self.assertEqual(co.keycoin.experience, 75)
        self.assertLess(self.city.ai_influence, 50)

    def test_bio_integrator(self):
        bi = BioIntegrator("Diana")
        self.assertEqual(bi.symbiotic_merge(self.city), "Merged with drone/beast for power boost.")
        self.assertEqual(bi.keycoin_growth(self.city), "Bio-construct evolved with enhanced traits.")
        self.assertEqual(bi.bio_terraforming(self.city), "Environment manipulated via bio-terraforming.")
        self.assertEqual(bi.keycoin.experience, 75)
        self.assertEqual(self.city.sectors["Arcology District"], 30)

    def test_quantum_trader(self):
        qt = QuantumTrader("Eve")
        self.assertEqual(qt.coin_flux(self.city), "KeyCoin value shifted in zone.")
        self.assertEqual(qt.smart_contract(self.city), "Temporary agreement enforced.")
        self.assertEqual(qt.invest_keycoin(self.city), "Rare items or city-wide events generated.")
        self.assertEqual(qt.keycoin.experience, 75)

if __name__ == '__main__':
    unittest.main()
