class User:
    def __init__(self, first_name, last_name, email, age):
        # Passed attributes
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        # Defualt attributes
        self.is_rewards_member = False
        self.gold_card_points = 0


    # Display info
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(f"Rewards Member? {self.is_rewards_member}")
        print(self.gold_card_points)

    # Enroll
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print("User is already a member")

    # Spend Points
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
        else:
            print("Not enough gold card points.")




user1 = User("Peter", "V", "peter@mail.com", 25)
user1.display_info()
user1.enroll()
user1.spend_points(50)
user1.display_info()
user1.enroll()

user2 = User("Paul", "A", "paul@mail.com", "20")
user2.enroll()
user2.spend_points(80)
user2.display_info()

user3 = User("Jessica", "A", "jessica@mail.com", "20")
user3.display_info()
user3.spend_points(40)