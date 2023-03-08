class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        for key,value in vars(self).items():
            print(f"{key}: {value}")
        print('-----------------')
    
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else:
            print(f"{self.first_name}, you are already a member.")
    
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print(f"{self.first_name}, you don't have that many points to spend.")

joel = User('Joel', 'Jacobson', 'joel@codingisthebestever.com', 21)
joel.display_info()
joel.enroll()
joel.display_info()

aslan = User('Aslan','','aslan@narnia.com', 457)
mr_tumnus = User('Mr', 'Tumnus', 'mrTum@narnia.com', 25)
lucy = User('Lucy', "Pevensie", 'lucy@narnia.com', 8)

joel.spend_points(50)
aslan.enroll()
aslan.spend_points(80)

joel.display_info()
aslan.display_info()
mr_tumnus.display_info()
lucy.display_info()

mr_tumnus.spend_points(40)
aslan.enroll()