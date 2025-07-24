from django.shortcuts import render
from .models import GameState

def game_view(request):
    # Initialize game state with validation
    session_state = request.session.get('game_state')
    if (session_state and isinstance(session_state, dict) and 
        isinstance(session_state.get('boat'), dict) and
        isinstance(session_state.get('left_bank'), dict) and
        isinstance(session_state.get('right_bank'), dict)):
        game = GameState(session_state)
    else:
        game = GameState()
        request.session['game_state'] = game.__dict__

    # Handle actions
    if request.method == 'POST':
        if 'reset' in request.POST:
            game.reset()
        elif 'load' in request.POST:
            try:
                missionaries = int(request.POST.get('missionaries', 0))
                cannibals = int(request.POST.get('cannibals', 0))
                game.load_boat(missionaries, cannibals)
            except ValueError:
                game.message = "Invalid input: Please select valid numbers."
        elif 'move' in request.POST:
            game.move_boat()
        
        # Save updated state
        request.session['game_state'] = game.__dict__
        request.session.modified = True  # Ensure session is marked as modified
    
    # Prepare context
    source_bank = game.left_bank if game.boat['position'] == 'left' else game.right_bank
    context = {
        'left_missionaries': list(range(game.left_bank['missionaries'])),
        'left_cannibals': list(range(game.left_bank['cannibals'])),
        'right_missionaries': list(range(game.right_bank['missionaries'])),
        'right_cannibals': list(range(game.right_bank['cannibals'])),
        'boat_missionaries': list(range(game.boat['missionaries'])),
        'boat_cannibals': list(range(game.boat['cannibals'])),
        'boat_position': game.boat['position'],
        'game_over': game.game_over,
        'message': game.message,
        'won': game.won,
        'available_missionaries': source_bank['missionaries'],
        'available_cannibals': source_bank['cannibals'],
    }
    return render(request, 'game.html', context)