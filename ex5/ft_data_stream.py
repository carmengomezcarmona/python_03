import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["bob", "alice", "dylan", "charlie"]

    actions = [
        "run",
        "eat",
        "sleep",
        "grab",
        "move",
        "climb",
        "swim",
        "release",
        "use"
    ]

    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(generator: Generator[tuple[str, str], None, None],
                  count: int) -> None:
    for i in range(count):
        event = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")


def build_event_list(
    generator: Generator[tuple[str, str], None, None],
    count: int
) -> list[tuple[str, str]]:
    event_list = []
    for i in range(count):
        event = next(generator)
        event_list.append(event)
    return event_list


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    event_generator = gen_event()
    consume_event(event_generator, 1000)
    event_list = build_event_list(event_generator, 10)
    print("Built list of 10 events:", event_list)
    for i in range(10):
        event = event_list.pop(0)
        print("Got event form list:", event)
        print("Remains in list: ", event_list)
