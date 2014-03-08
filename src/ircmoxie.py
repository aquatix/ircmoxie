import irc

server = irc.client.IRC().server()
server.buffer_class = irc.buffer.LineBuffer
server.connect()
