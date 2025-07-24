from django.shortcuts import render
from .models import GameState

def game_view(request):
    # Initialize game state in session
    if 'game_state' not in request.session:
        game = GameState()
        request.session['game_state'] = game.__dict__
    
    game = GameState()
    game.__dict__ = request.session['game_state']
    
    # Handle actions
    if request.method == 'POST':
        if 'reset' in request.POST:
            game.reset()
        elif 'move' in request.POST:
            move_type = request.POST['move']
            moves = {
                '1m': (1, 0),
                '1c': (0, 1),
                '2m': (2, 0),
                '2c': (0, 2),
                '1m1c': (1, 1),
            }
            if move_type in moves:
                m, c = moves[move_type]
                game.move(m, c)
        
        # Save updated state
        request.session['game_state'] = game.__dict__
    
    context = {
        'game': game,
        'boat_side': game.boat.capitalize(),
        'game_over': game.game_over,
        'message': game.message,
    }
    return render(request, 'game.html', context)