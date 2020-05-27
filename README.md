# EmailGetter
This item is used to obtain the user's email address.

## Requirements
The following configuration is required:
- python 3.6 or above.
- personal access token applied from GitHub.
- GitHub API search string that can retrieve all user information

## Usage
First, the terminal is used to execute the following instructions:
```
git clone https://github.com/xf97/EmailGetter
cd EmailGetter
```
Second you should create the following two files under the current folder and write the following to them:
- create a file named **token_win10.txt** (in Linux system, this file is **token_linux.txt'**), and then write the *personal access token* into the file. 
- create a file named **searchStr.txt**, and then write the *search string* into the file.

Third, type the following command in the terminal and press Enter to get the user information list, and then you can see that the **usersList.txt**  has been added to the current folder:
```
python getEmail.py -GL
```

Finally, type the following command in the terminal and press Enter to get the user's mailbox. The mailbox will be stored in the **email.txt** in the current folder (this process is slow, please be patient):
```
pythron getEmail.py -GI
```

## Lisence
This program is issued, reproduced or used under the permission of **MIT**. Please indicate the source.


