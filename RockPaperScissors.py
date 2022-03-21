_game_setup = {
    "Rock":{
	    "Beats":["Scissors"],
		"Defeated":["Paper"],
		"Null":["Rock"]},
	"Paper":{
	    "Beats":["Rock"],
		"Defeated":["Scissors"],
		"Null":["Paper"]},
	"Scissors":{
	    "Beats":["Paper"],
		"Defeated":["Rock"]
		"Null":["Scissors"]}}

def _init(goes):
	print("Welcome!")
	while True:
		move = input("Choose A Move: ")
		if move in _game_setup:
		recv_move = random.choice(["Rock", "Paper", "Scissors"])
		    if recv_move in _game_setup[move]["Beats"]:
			   
			    
			    
    
	    
		
