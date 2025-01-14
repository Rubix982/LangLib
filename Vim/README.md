# Vim

Daily `vim` shortcuts.

## General Navigation

- h → Move left
- l → Move right
- j → Move down
- k → Move up
- w → Move forward to the start of the next word
- e → Move to the end of the word
- b → Move back to the start of the previous word
- 0 → Move to the start of the current line
- ^ → Move to the first non-blank character
- $ → Move to the end of the current line
- gg → Go to the start of the file
- G → Go to the end of the file
- :n → Go to line n
- Ctrl-d → Scroll down half a page
- Ctrl-u → Scroll up half a page
- Ctrl-e → Scroll down by one line
- Ctrl-y → Scroll up by one line

## Editing Text

- i → Insert mode before the cursor
- I → Insert mode at the start of the line
- a → Insert mode after the cursor
- A → Insert mode at the end of the line
- o → Open a new line below the current line
- O → Open a new line above the current line
- s → Delete the character under the cursor and enter insert mode
- S → Delete the entire line and enter insert mode
- r → Replace the character under the cursor
- R → Enter replace mode (overwrite characters)

## Deleting and Cutting (Deleting is Cutting in Vim)

- x → Delete the character under the cursor
- X → Delete the character before the cursor
- dw → Delete from cursor to end of word
- db → Delete from cursor to start of word
- dd → Delete the entire line
- d$ → Delete from cursor to end of line
- d0 → Delete from cursor to start of line
- dgg → Delete from cursor to the start of the file
- dG → Delete from cursor to the end of the file

## Copying (Yanking) and Pasting

- yy → Copy the current line
- y$ → Copy from cursor to the end of the line
- y0 → Copy from cursor to the start of the line
- yw → Copy from cursor to the end of the word
- yb → Copy from cursor to the start of the word
- p → Paste after the cursor
- P → Paste before the cursor

## Undo & Redo

- u → Undo last change
- Ctrl-r → Redo last undone change

## Search and Replace

- /text → Search forward for "text"
- ?text → Search backward for "text"
- n → Repeat the last search forward
- N → Repeat the last search backward
- :%s/old/new/g → Replace all occurrences of "old" with "new"
- :s/old/new/g → Replace "old" with "new" in current line
- :s/old/new/gc → Replace with confirmation
- * → Search for the word under the cursor (forwards)
- # → Search for the word under the cursor (backwards)

## Working with Multiple Files

- :e filename → Open a file
- :w → Save the file
- :wq → Save and quit
- :q → Quit (if no changes)
- :q! → Quit without saving
- :n → Open the next file in the argument list
- :prev → Open the previous file in the argument list

## Splits and Windows

- :vsplit or :vsp → Vertical split
- :split or :sp → Horizontal split
- Ctrl-w w → Switch between splits
- Ctrl-w q → Close the current split
- Ctrl-w h → Move to the left split
- Ctrl-w l → Move to the right split
- Ctrl-w j → Move to the bottom split
- Ctrl-w k → Move to the top split
- Ctrl-w = → Equalize split sizes

## Tabs (Advanced Use)

- :tabnew → Open a new tab
- gt → Next tab
- gT → Previous tab
- :tabclose → Close the current tab

## Visual Mode (Text Selection)

- v → Start visual mode (select text character by character)
- V → Start line visual mode
- Ctrl-v → Start block visual mode
- y → Yank (copy) selected text
- d → Delete selected text
- > → Indent selected text
- < → Unindent selected text

## Productivity Boosters

- . → Repeat the last change
- % → Jump between matching parentheses/braces
- :!command → Run a shell command from Vim
- :set number → Show line numbers
- :set relativenumber → Show relative line numbers
- :set hlsearch → Highlight search results
- :noh → Clear search highlights

## Marks and Jumps

- ma → Set mark a at the cursor position
- 'a → Jump to the start of the line where mark a is set
- `a → Jump to the exact cursor position where mark a is set
- Ctrl-o → Jump to the last cursor position
- Ctrl-i → Jump forward in jump list

## Daily Shortcut Summary for Fast Use

- i → Insert mode
- v → Visual mode
- y → Yank (copy)
- p → Paste
- d → Delete
- u → Undo
- Ctrl-r → Redo
- /text → Search
- :w → Save
- :q → Quit
