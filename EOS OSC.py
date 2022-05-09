from pythonosc.udp_client import SimpleUDPClient
targetIP = "192.168.0.103"
TargetPort = 8000
FaderPage = "1"

client = SimpleUDPClient(targetIP, TargetPort)
client.send_message("/eos/fader/1/config/"+FaderPage+"/10", 1)
client.send_message("/eos/fader/1/1", 1)