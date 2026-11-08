class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} is already in the network.")
            return

        self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        if person1_name == person2_name:
            print("A person cannot be friends with themselves.")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = []

            for friend in person.friends:
                friend_names.append(friend.name)

            print(f"{name} is friends with: {', '.join(friend_names)}")


# Test your social network implementation here.

network = SocialNetwork()

# Add six people.
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Create eight friendships.
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

print("\nOriginal Social Network:")
network.print_network()

# Test adding a friendship with a missing person.
print("\nTesting Missing Person:")
network.add_friendship("Jordan", "Johnny")

# Test adding a duplicate person.
print("\nTesting Duplicate Person:")
network.add_person("Alex")

# Test adding a duplicate friendship.
print("\nTesting Duplicate Friendship:")
network.add_friendship("Alex", "Jordan")

# Test adding a person as their own friend.
print("\nTesting Self Friendship:")
network.add_friendship("Alex", "Alex")

# Print the network again to check for duplicates.
print("\nFinal Social Network:")
network.print_network()
