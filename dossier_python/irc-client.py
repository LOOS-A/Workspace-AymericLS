import socket
import sys

server = "irc.root-me.org"
channel = "#root-me_challenge"
botNickName = "candy"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server,6667))
irc.send("USER" + botNickName + " " + botNickName + " " + botNickName + ":candy-test\n")
irc.send("NICK" + botNickName + "\n")
irc.send("JOIN" + channel)
irc.send("PRIVMSG" + channel + ":!ep1")

while 1:    #puts it in a loop
   text=irc.recv(2040)  #receive the text
   print(text)   #print text to console

   if text.find('PING') != -1:                          #check if 'PING' is found
      irc.send('PONG ' + text.split() [1] + '\r\n') #returnes 'PONG' back to the server (prevents pinging out!)