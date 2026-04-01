class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for person in people:
        person_instance = Person(name=person["name"], age=person["age"])
        result.append(person_instance)

    for person in people:
        current_person = Person.people[person["name"]]
        if wife_name := person.get("wife"):
            current_person.wife = Person.people[wife_name]
        elif husband_name := person.get("husband"):
            current_person.husband = Person.people[husband_name]
    return result
