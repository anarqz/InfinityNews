A small note on online matchmaking, since I can see many of you confused or even angry about not being able to play online.

## Matches run on players' computers

Matchmaking helps players find each other, but it doesn't relay game traffic. In a match, the **host** is the relay: it receives packets from every player and shares them with everyone, so the whole lobby stays in sync.

What Infinity provides is a matchmaking layer. It saves everyone the hassle of knowing your IP address to join you.

That doesn't mean Infinity guarantees a stable online experience or low-latency races. In the end you're still connecting to other people's local servers, and depending on their internet connection and ISP restrictions.

## Hosting needs an open port

- Your router must forward **UDP port 5101** to your computer.
- Your firewall and internet provider must allow incoming connections.
- ISP restrictions such as **CGNAT** can prevent hosting even with port forwarding configured.

Joining and hosting have different network requirements, and both need to be free of restrictions for the online experience to work well.

## Getting disconnected right away?

If you sometimes enter a lobby and get disconnected immediately, that's your ISP or router, not Infinity.

## In short

Without a dedicated official relay carrying the traffic, some player and network combinations simply can't connect. That's how it has been since the dawn of time.
