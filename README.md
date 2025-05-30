<b><h2>Readme RvTools v2:</h2></b>
To fix the issues in the Node Library of ComfyUI i had to change all node names which leads to this version but that also allows me to updated some of the names for a cleaner look and do some other clean ups.<br><br>
![Screenshot 2024-11-28 100306](https://github.com/user-attachments/assets/ab68ad18-a057-4834-ba28-8fcb377578b1)
<br><br>

i created this set of nodes because some nodes did not exist or do not exist in the other sets, starting with the passers and switches. 
Also, the comfyui manager quite often had problems displaying the correct nodes I used in my workflows, which caused problems for the users. 
so in the end I just adopted some of them to avoid messages like “the workflow doesn't work”.<br><br>
![rvt](https://github.com/user-attachments/assets/072a48de-3c27-4dd9-9b7f-a9af11ede3e3)

<b><h2>Passers:</h2></b>
the passers have several uses. originally they were created to be placed in front of nodes that had problems getting information from bypassed nodes. 
like the node 'rgthree display anything' still has today. However, they can also be used in managed groups. 
firstly because you need at least two nodes to create such a group and secondly to distribute an input to several nodes in the group. 
creating such a group offers the possibility to “hide” inputs/outputs or widgets, e.g. to reduce the size.

<b><h2>Switches:</h2></b>
image switch, a masterpiece imo i like to use a lot of them xd found and shamelessly taken from the comfyroll node set and altered to all the switches in this set. 
i think i've asked the creator once for an integer switch but that request was ignored so here we are^^
when bypassed, this node sends what ever is connected to input 1 to the target, if the standard value is 2 and it is enabled it sends what ever is connected to input 2. 
very helpful in workflows with a lot of groups that can be bypassed (not muted) like mine.

![iswitch](https://github.com/user-attachments/assets/c87cac6b-5205-4423-8d32-933d31343f2f)

<b><h2>Multi Switches:</h2></b>
these switches return the first Slot that is not none. helpful if you have different clip models to choose from that can be bypassed via an options menu. 
e.g. the clip from the checkpoint loader, a dual clip loader (flux) and a triple clip loader (sd3). <br>
for the switch to work, the nodes that can be bypassed should be connected to the first slots and the clip from the checkpoint loader last because this node 
is always enabled and a node that is always enabled and connected to the first slot will never be none and the other slots are ignored.

![multi_switches](https://github.com/user-attachments/assets/bda901ca-287b-4fc0-879a-3778ef893387)

<b><h2>Project Folder, Checkpoint Loader, Save Image with Generation Data, Sampler Settings, Aspect Ratio:</h2></b>

![Save_GenData](https://github.com/user-attachments/assets/666dfd84-8501-46a7-9760-45115d73cf6b)


<b><h2>...to be continued</h2></b>
