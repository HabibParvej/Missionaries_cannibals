class GameState:
    def __init__(self, state=None):
        if state:
            self.__dict__ = state
        else:
            self.reset()
    
    def reset(self):
        self.left_bank = {'missionaries': 3, 'cannibals': 3}
        self.right_bank = {'missionaries': 0, 'cannibals': 0}
        self.boat = {
            'position': 'left',
            'missionaries': 0,
            'cannibals': 0
        }
        self.message = "Welcome! Select passengers and move the boat."
        self.game_over = False
        self.won = False

    def load_boat(self, missionaries, cannibals):
        if self.game_over:
            self.message = "Game over. Please reset to start a new game."
            return False
            
        source = self.left_bank if self.boat['position'] == 'left' else self.right_bank
        
        # Validate input
        if not (isinstance(missionaries, int) and isinstance(cannibals, int)):
            self.message = "Invalid input: Numbers must be integers."
            return False
            
        if missionaries < 0 or cannibals < 0:
            self.message = "Invalid input: Cannot select negative numbers."
            return False
            
        if source['missionaries'] < missionaries:
            self.message = f"Not enough missionaries on {self.boat['position']} bank. Only {source['missionaries']} available."
            return False
            
        if source['cannibals'] < cannibals:
            self.message = f"Not enough cannibals on {self.boat['position']} bank. Only {source['cannibals']} available."
            return False
            
        if missionaries + cannibals > 2 or missionaries + cannibals < 1:
            self.message = "Boat must carry 1-2 people."
            return False
            
        self.boat['missionaries'] = missionaries
        self.boat['cannibals'] = cannibals
        self.message = f"Loaded: {missionaries} missionary(ies) and {cannibals} cannibal(s)"
        return True

    def move_boat(self):
        if self.game_over:
            self.message = "Game over. Please reset to start a new game."
            return False

        if self.boat['missionaries'] + self.boat['cannibals'] == 0:
            self.message = "Load passengers first."
            return False

        source = self.left_bank if self.boat['position'] == 'left' else self.right_bank
        target = self.right_bank if self.boat['position'] == 'left' else self.left_bank
        
        # Remove people from source bank
        source['missionaries'] -= self.boat['missionaries']
        source['cannibals'] -= self.boat['cannibals']
        
        # Add people to target bank
        target['missionaries'] += self.boat['missionaries']
        target['cannibals'] += self.boat['cannibals']
        
        # Move boat to other side
        self.boat['position'] = 'right' if self.boat['position'] == 'left' else 'left'
        
        # Clear boat
        self.boat['missionaries'] = 0
        self.boat['cannibals'] = 0
        
        # Check game state
        self.check_state()
        return True

    def check_state(self):
        # Check left bank
        if self.left_bank['missionaries'] > 0 and \
           self.left_bank['cannibals'] > self.left_bank['missionaries']:
            self.message = "Missionaries eaten on left bank! You lose."
            self.game_over = True
            return False
            
        # Check right bank
        if self.right_bank['missionaries'] > 0 and \
           self.right_bank['cannibals'] > self.right_bank['missionaries']:
            self.message = "Missionaries eaten on right bank! You lose."
            self.game_over = True
            return False
            
        # Check win condition
        if self.right_bank['missionaries'] == 3 and \
           self.right_bank['cannibals'] == 3:
            self.message = "Congratulations! You won!"
            self.game_over = True
            self.won = True
            return True
            
        self.message = "Boat moved successfully! Load passengers for next move."
        return True