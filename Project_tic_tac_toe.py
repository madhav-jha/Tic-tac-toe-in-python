
# coding: utf-8

# In[18]:


board = [['empty','empty','empty'],['empty','empty','empty'],['empty','empty','empty']]


# In[2]:


def board_layout():
    print('current status: \n', board[0],board[1],board[2], sep = '\n')


# In[9]:


def check_status(marker):
    if (board[0][0] == board[0][1] == board[0][2] == marker) or         (board[1][0] == board[1][1] == board[1][2] == marker) or         (board[2][0] == board[2][1] == board[2][2] == marker) or         (board[0][0] == board[1][0] == board[2][0] == marker) or         (board[0][1] == board[1][1] == board[2][1] == marker) or         (board[0][2] == board[1][2] == board[2][2] == marker) or         (board[0][0] == board[1][1] == board[2][2] == marker) or         (board[2][0] == board[1][1] == board[0][2] == marker):
            print('='*20)
            print(marker,' has won the game!')
            return True
    else:
        return False


# In[10]:


def make_move(row,pos,mov):
    if row in [0,1,2] and pos in [0,1,2] and mov in ['o','x']: 
        if board[row][pos] == 'empty':
            board[row][pos] = mov
            status = check_status(mov)
            if status:
                return False
            else:
                return True
        
            
        else:
            print('Position is occupied? Select an empty position')
            board_layout()
            return False
        
    else:
        print('Please enter a valid row/position/move...')
        return False


# In[11]:


def take_input():
    mov = input('Your move: ')
    row = int(input('row postion: '))
    pos = int(input('position in a row: '))
    
    success = make_move(row,pos,mov)
    
    return success


# In[14]:


def lets_play():
    
    print('Here you go!')
    print('Enter o/x at row(0,1,2) and pos(0,1,2) to play the game:')
    
    running = True
    while(running):
        board_layout()
        running = take_input()
        
    board_layout()    
    print('Game over!')
    board.clear()
    


# In[ ]:


lets_play()

