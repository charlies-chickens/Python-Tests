class KeyCoin:
    def __init__(self):
        self.evolution_level = 1
        self.experience = 0
        self.powers = ["Basic Access"]

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= self.evolution_level * 100:
            self.evolve()

    def evolve(self):
        self.evolution_level += 1
        self.experience = 0
        new_power = f"Enhanced Tier {self.evolution_level}"
        self.powers.append(new_power)
        return new_power

    def __str__(self):
        return f"KeyCoin(Level: {self.evolution_level}, Exp: {self.experience}, Powers: {', '.join(self.powers)})"


class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.keycoin = KeyCoin()

    def use_ability(self, ability_name):
        print(f"{self.name} uses {ability_name}!")
        self.keycoin.gain_experience(25)

    def __str__(self):
        return f"Player(Name: {self.name}, Role: {self.role}, {self.keycoin})"


class ComputingArchitect(Player):
    def __init__(self, name):
        super().__init__(name, "Computing Architect")

    def quantum_hack(self, city):
        self.use_ability("Quantum Hack")
        city.update_sector("AI Core", 10)
        city.ai_influence -= 5
        return "City systems overridden."

    def keycoin_sync(self, city):
        self.use_ability("KeyCoin Sync")
        city.update_sector("AI Core", 5)
        return "KeyCoin linked to AI entities."

    def data_construct(self, city):
        self.use_ability("Data Construct")
        city.update_sector("Arcology District", 5)
        return "Temporary AI minion created."


class NanoEngineer(Player):
    def __init__(self, name):
        super().__init__(name, "Nano-Engineer")

    def nano_swarm(self, city):
        self.use_ability("Nano Swarm")
        city.update_sector("Energy Grid", 10)
        return "Nanobots deployed for repair/damage."

    def key_infusion(self, city):
        self.use_ability("Key Infusion")
        city.update_sector("Energy Grid", 5)
        return "KeyCoin embedded into tech."

    def mini_factory(self, city):
        self.use_ability("Mini-Factory")
        city.update_sector("Arcology District", 10)
        return "Portable mini-factory produced."


class CyberneticOperative(Player):
    def __init__(self, name):
        super().__init__(name, "Cybernetic Operative")

    def phase_cloak(self, city):
        self.use_ability("Phase Cloak")
        city.ai_influence -= 2
        return "Became temporarily invisible."

    def keycoin_disruptor(self, city):
        self.use_ability("KeyCoin Disruptor")
        city.ai_influence -= 10
        return "Enemy networks weakened."

    def neural_jack(self, city):
        self.use_ability("Neural Jack")
        city.ai_influence -= 5
        return "Abilities stolen from target."


class BioIntegrator(Player):
    def __init__(self, name):
        super().__init__(name, "Bio-Integrator")

    def symbiotic_merge(self, city):
        self.use_ability("Symbiotic Merge")
        city.update_sector("Arcology District", 5)
        return "Merged with drone/beast for power boost."

    def keycoin_growth(self, city):
        self.use_ability("KeyCoin Growth")
        city.update_sector("Arcology District", 10)
        return "Bio-construct evolved with enhanced traits."

    def bio_terraforming(self, city):
        self.use_ability("Bio-Terraforming")
        city.update_sector("Arcology District", 15)
        return "Environment manipulated via bio-terraforming."


class QuantumTrader(Player):
    def __init__(self, name):
        super().__init__(name, "Quantum Trader")

    def coin_flux(self, city):
        self.use_ability("Coin Flux")
        city.update_sector("Energy Grid", 5)
        city.update_sector("AI Core", 5)
        return "KeyCoin value shifted in zone."

    def smart_contract(self, city):
        self.use_ability("Smart Contract")
        city.update_sector("Arcology District", 5)
        return "Temporary agreement enforced."

    def invest_keycoin(self, city):
        self.use_ability("Invest KeyCoin")
        city.update_sector("AI Core", 10)
        city.update_sector("Energy Grid", 10)
        city.update_sector("Arcology District", 10)
        return "Rare items or city-wide events generated."
