# How does git even work?

This is going to get a bit technical very quickly, and is most definitely targeted towards the computer science folk, but Git, at the data structure and algorithms level, uses a [directed acyclic graph](https://en.wikipedia.org/wiki/Directed_acyclic_graph) to store all of its data under the hood.

![](https://www.researchgate.net/profile/Ritu-Kundu-2/publication/276851762/figure/fig5/AS:669689269211149@1536677772684/A-directed-acyclic-graph-G-V-E-The-set-of-nodes-V-v1-v2-v15-Note.png)

The magic of Git too, is that once you enter a directory and run `git init`, all it stores locally is a folder in that directory named `.git`, there is no Git 'server' or even a centralized location where it stores files (other than configuration, but that is optional)

To give an example, the very repository you are viewing as a website right now as seen from the command line:

![](https://i.imgur.com/CTeRtWH.png)

More about said internals can be found [here](https://levelup.gitconnected.com/git-internals-c219521d9f6).
