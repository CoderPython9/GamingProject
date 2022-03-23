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

def init():
	print("Welcome!")
	playerscore = 0
	computerscore = 0
	game_running = True
	while game_running:
		move = input("Choose A Move: ")
		if move in _game_setup:
		recv_move = random.choice(["Rock", "Paper", "Scissors"])
		    if recv_move in _game_setup[move]["Beats"]:
				print("You Won with", move, "against", recv_move)
				playerscore += 1
				print("You now have", playerscore, "points!")
				go = input("Do You Want To Have ANOTHER GO? (y/n)")
				if go != "y":
					game_running = False
			elif recv_move in _game_setup[move]["Defeated"]:
				print("You lost with", move, "against", recv_move)
				computerscore += 1
				print("You have", playerscore, "points!")
				print("Computer now has", computerscore, "points!")
				go = input("Do You Want To Have ANOTHER GO? (y/n)")
				if go != "y":
					game_running = False
			else:
				print("Draw!", move, "and", move)
				print("You have", playerscore, "points")
				print("Computer has", computerscore, "point")
				go = input("Do You Want To Have ANOTHER GO? (y/n)")
				if go != "y":
					game_running = False
				
				
			   
			    
			    
    
	    
		
