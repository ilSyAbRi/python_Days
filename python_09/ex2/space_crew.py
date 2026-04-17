from datetime import datetime
from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate(self):

        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = False
        for m in self.crew:
            if m.rank == Rank.CAPTAIN:
                has_leader = True
            if m.rank == Rank.COMMANDER:
                has_leader = True

        if not has_leader:
            raise ValueError(
                    "Mission must have at least one Commander or Captain"
                    )

        if self.duration_days > 365:
            experienced_count = 0
            total = len(self.crew)

            for m in self.crew:
                if m.years_experience >= 5:
                    experienced_count += 1

            if (experienced_count / total) < 0.5:
                raise ValueError(
                    "Long missions require at least 50% \
                    experienced crew (5+ years)"
                )

        for m in self.crew:
            if not m.is_active:
                raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    crew = [
        CrewMember(
            member_id="CM001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=42,
            specialization="Mission Command",
            years_experience=20,
        ),
        CrewMember(
            member_id="CM002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=35,
            specialization="Navigation",
            years_experience=10,
        ),
        CrewMember(
            member_id="CM003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=28,
            specialization="Engineering",
            years_experience=5,
        ),
    ]

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 7, 4, 9, 0, 0),
        duration_days=900,
        crew=crew,
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")

    print("Crew members:")
    for m in mission.crew:
        print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    print("=========================================")

    try:
        SpaceMission(
            mission_id="M_BAD_01",
            mission_name="Doomed Mission",
            destination="Jupiter",
            launch_date=datetime(2024, 8, 1, 9, 0, 0),
            duration_days=100,
            crew=[
                CrewMember(
                    member_id="CM010",
                    name="Bob",
                    rank=Rank.CADET,
                    age=22,
                    specialization="Cleaning",
                    years_experience=0,
                )
            ],
            budget_millions=500.0,
        )

    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"].split(", ", 1)[-1])


if __name__ == "__main__":
    main()
