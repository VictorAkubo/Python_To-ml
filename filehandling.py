#opening a file

try:
  #reading
  #file = open("text.txt","r")
  #content = file.read()
  
  
 #write
 #filew = open("text.txt","w")
 # contentwrite = filew.write("The street was quiet, but not empty. Somewhere in the distance, a generator hummed like a tired giant refusing to sleep. A single light flickered in a window above, telling stories no one stopped to hear. Time moved differently here. Minutes stretched, folded, and slipped through fingers like warm sand. A boy sat on a broken chair, staring at the sky as if expecting it to answer a question he hadn’t fully formed yet. Footsteps echoed, then vanished. A dog barked once, then thought better of it. The air carried the scent of rain that never quite arrived. And in that strange pause between noise and silence, something shifted. Not loudly, not dramatically, but just enough to remind anyone paying attention that even the quietest places are full of unseen movement.")
  
 # filea = open("text.txt","a")
  #contentappend = filea.write(" do we need the quiet, no the fear increases with the sunden noise of quiet")
  file = open("text.txt","r")
  content = file.read()
  print(content)
  
  content2 = file.read(100)
  print(content2)
finally:
  file.close()

