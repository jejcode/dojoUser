class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print('-----------------')
        for key,value in vars(self).items():
            print(f"{key}: {value}")
        print('-----------------')
        return self
    
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print(f"{self.first_name}, you are already a member.")
        return self
    
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print(f"{self.first_name}, you don't have that many points to spend.")
        return self

joel = User('Joel', 'Jacobson', 'joel@codingisthebestever.com', 21)
joel.display_info()

aslan = User('Aslan','','aslan@narnia.com', 457)
mr_tumnus = User('Mr', 'Tumnus', 'mrTum@narnia.com', 25)
lucy = User('Lucy', "Pevensie", 'lucy@narnia.com', 8)

joel.enroll().spend_points(50).display_info()
aslan.enroll().spend_points(80).display_info().enroll()
mr_tumnus.display_info().spend_points(40)
lucy.display_info()