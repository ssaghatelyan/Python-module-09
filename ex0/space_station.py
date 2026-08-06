from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_lvl: float = Field(ge=0.0, le=100.0)
    oxygen_lvl: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def print_validation_errors(error: ValidationError) -> None:

    for err in error.errors():
        message = err["msg"]
        print(f"{message}")


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_lvl=85.5,
            oxygen_lvl=92.3,
            last_maintenance=datetime.now(),
        )

        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_lvl}%")
        print(f"Oxygen: {station.oxygen_lvl}%")

        if station.is_operational:
            print("Status: Operational")
        else:
            print("Status: Offline")

    except ValidationError as e:
        print("Expected validation error:")
        print_validation_errors(e)

    print("\n========================================")
    try:
        invalid_station = SpaceStation(
            station_id="ISS002",
            name="Broken Station",
            crew_size=30,
            power_lvl=90.0,
            oxygen_lvl=88.0,
            last_maintenance=datetime.now(),
        )

        print("Valid station created:")
        print(f"ID: {invalid_station.station_id}")
        print(f"Name: {invalid_station.name}")
        print(f"Crew: {invalid_station.crew_size} people")
        print(f"Power: {invalid_station.power_lvl}%")
        print(f"Oxygen: {invalid_station.oxygen_lvl}%")

    except ValidationError as e:
        print("Expected validation error:")
        print_validation_errors(e)


if __name__ == "__main__":
    main()
