# WhatsApp-Mass-Messenger
Python code for a WhatsApp mass messenger: https://github.com/Akshayjyoti/WhatsApp-Mass-Messenger/blob/main/whatsapp1.py <br/>
Vesrion 1.0 <br/>
Testing date: September 5, 2021 <br/> <br/>

Working procedure: <br/><br/>

1. Enter the number of people/groups to send the message. <br/>
2. Enter your message. <br/>
3. On pressing Enter, the program will store the required number of names in a list. <br/>
4. Then for each name, it enters the chat and sends the message. <br/><br/>

Note 1: Maximize the Chrome window as soon as it opens. <br/>
Note 2: Do NOT maximize the Command Line window. The pyautogui.click() is used to change focus to Chrome window, so it needs to be visible on screen. <br/>
Note 3: Ignore warnings while entering the number of people or groups. <br/>
Note 4: The program will also store the chats with no name. So if there are non-contact chats on your feed, the message will be sent to them as well. <br/><br/>

Warning 1: Lines 34, 48, 52, 56, 69 and 71 of the code may need to be modified with change in Chrome version. <br/>
Warning 2: The lines 64 to 74 contain the code for mass messaging. Please try the program once without un-commenting these lines to ensure the code is working correctly. <br/><br/>

INVITATION TO MODIFY: <br/> <br/>
The above lines 64 to 74 of the code have not been tested yet. All that has been tested is that names are correctly stored in a list. In case these lines are not working correctly, using pyautogui to scroll back up might work. This is due to the structure of WhatsApp Web: it loads 18 chats at a time before needing to be scrolled to load more (this number was 17 in a previous version). The amount of scroll needed will also vary accordingly. However, this requires a lot of testing and debugging, which has not been done due to lack of a test WhatsApp account. Modifications/suggestions are invited.
