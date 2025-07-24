class GameState:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.left_bank = {'missionaries': 3, 'cannibals': 3}
        self.right_bank = {'missionaries': 0, 'cannibals': 0}
        self.boat = 'left'  # 'left' or 'right'
        self.message = "Welcome! Move all to the right bank safely."
        self.game_over = False
        self.won = False

    def move(self, missionaries, cannibals):
        if self.game_over:
            return

        # Validate move
        if missionaries + cannibals > 2 or missionaries + cannibals < 1:
            self.message = "Boat can carry 1-2 people"
            return

        # Get current and target banks
        source = self.left_bank if self.boat == 'left' else self.right_bank
        target = self.right_bank if self.boat == 'left' else self.left_bank
        
        # Check available people
        if source['missionaries'] < missionaries or source['cannibals'] < cannibals:
            self.message = "Not enough people on bank"
            return

        # Update counts
        source['missionaries'] -= missionaries
        source['cannibals'] -= cannibals
        target['missionaries'] += missionaries
        target['cannibals'] += cannibals
        
        # Move boat
        self.boat = 'right' if self.boat == 'left' else 'left'
        self.message = "Move successful!"
        
        # Check game state
        self.check_state()

    def check_state(self):
        # Check left bank
        if self.left_bank['missionaries'] > 0 and \
           self.left_bank['cannibals'] > self.left_bank['missionaries']:
            self.message = "Missionaries eaten on left bank!"
            self.game_over = True
            return
            
        # Check right bank
        if self.right_bank['missionaries'] > 0 and \
           self.right_bank['cannibals'] > self.right_bank['missionaries']:
            self.message = "Missionaries eaten on right bank!"
            self.game_over = True
            return
            
        # Check win condition
        if self.right_bank['missionaries'] == 3 and \
           self.right_bank['cannibals'] == 3:
            self.message = "Congratulations! You won!"
            self.game_over = True
            self.won = True