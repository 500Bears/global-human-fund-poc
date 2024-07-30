import uuid
import random
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

class Human:
    def __init__(self, name: str):
        self.name = name
        self.id = str(uuid.uuid4())
        self.auth_number = random.randint(100000, 999999)
        self.achievements: List[str] = []

class CentralHumanFund:
    def __init__(self):
        self.balance: float = 0
        self.humans: Dict[str, Human] = {}
        self.achievements: List[Tuple[str, str, float]] = []
        self.last_distribution = datetime.now()

    def register_human(self, human: Human) -> None:
        """Register a new human in the system."""
        if human.id in self.humans:
            raise ValueError(f"Human with ID {human.id} already exists")
        self.humans[human.id] = human
        print(f"Registered {human.name} with ID: {human.id}")

    def add_achievement(self, human_id: str, achievement: str, value: float) -> None:
        """Add an achievement for a registered human and increase the fund balance."""
        if human_id not in self.humans:
            raise ValueError(f"No human found with ID {human_id}")
        if value < 0:
            raise ValueError("Achievement value cannot be negative")
        
        self.humans[human_id].achievements.append(achievement)
        self.balance += value
        self.achievements.append((human_id, achievement, value))
        print(f"Added achievement for {self.humans[human_id].name}: {achievement}, Value: {value}")

    def distribute_funds(self) -> None:
        """Distribute funds to all registered humans if enough time has passed."""
        if datetime.now() - self.last_distribution < timedelta(days=30):
            print("Not yet time for distribution")
            return

        if not self.humans:
            print("No registered humans to distribute funds to")
            return

        distribution_amount = self.balance * 0.5
        per_human_amount = distribution_amount / len(self.humans)

        for human in self.humans.values():
            print(f"Distributing {per_human_amount:.2f} to {human.name}")

        self.balance -= distribution_amount
        self.last_distribution = datetime.now()

    def display_dashboard(self) -> None:
        """Display the current state of the fund."""
        print("\n--- Global Human Fund Dashboard ---")
        print(f"Current Balance: {self.balance:.2f}")
        print(f"Registered Humans: {len(self.humans)}")
        print(f"Total Achievements: {len(self.achievements)}")
        print(f"Next Distribution Target: {self.balance:.2f}")
        print("-----------------------------------\n")

def main():
    """Main function to demonstrate the Global Human Fund system."""
    fund = CentralHumanFund()

    # Register humans
    alice = Human("Alice")
    bob = Human("Bob")
    fund.register_human(alice)
    fund.register_human(bob)

    # Add achievements
    fund.add_achievement(alice.id, "Developed clean energy solution", 10000)
    fund.add_achievement(bob.id, "Volunteered 100 hours", 5000)

    # Display dashboard
    fund.display_dashboard()

    # Attempt distribution
    fund.distribute_funds()

    # Add more achievements
    fund.add_achievement(alice.id, "Published research paper", 7500)

    # Display updated dashboard
    fund.display_dashboard()

    # Simulate time passage and distribute
    fund.last_distribution -= timedelta(days=31)
    fund.distribute_funds()

    # Final dashboard display
    fund.display_dashboard()

if __name__ == "__main__":
    main()
