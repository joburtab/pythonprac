import random 

MAX_LINES =5
MIN_BET=1
MAX_BET=500


ROWS=3
COLS=3


symbole_count={
    "A":1,
    "B":3,
    "C":3,
    "D":0
}

symbole_Value ={
    "A":0,
    "B":4,
    "C":2,
    "D":0
}



def check_winning(columns,lines,bet,values):
    winnings=0
    winning_line=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbole_to_check = column[line]
            if symbol != symbole_to_check:
                break
            else:
              winnings += values[symbol] * bet  
              winning_line.append(line+1)
        return winnings ,winning_line  

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range (symbol_count):
           all_symbols.append(symbol)
    columns = [[],[],[]]
    for  _ in  range(cols):
         column =[]
         for _ in range(rows):
            columns=[]
            current_symbols=all_symbols[:]
            for _ in range(rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
            columns.append(column)
                
         return columns 
                
def print_slot_machine(columns):
   for row in range (len(columns[0])):
       for i, column in  enumerate(columns):
           if i !=len(columns) -1:
                print(column[row],end="| " )
           else:
            print(column[row],end="  ")
       print()

def deposit():
    while True:
        amount=input("what doy want to deposit ?")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("the amount should be grater than 0")
        else:
            print("this value is invalid ")
            
    return amount        



def get_number_of_line():
    while True:
        lines=input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+ ")? ")
        if lines.isdigit():
            lines =int(lines)
            if 1<= MAX_LINES <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("this value is invalid ")
    return lines 
def get_bet():
    while True:
        amount=input("inter the amount of bet ?")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"the amount ${MIN_BET} - ${MAX_BET}.")
        else:
            print("plaese enter a number ")
            
    return amount     
def spin(balance):
    lines=get_number_of_line()
    while True:
        bet=get_bet()
        total_bet= bet * lines
        
        if total_bet > balance:
            print(f"you dont have enough to bet thta amount ,your current balance is {balance} low")
        else:
            break    
    print(f"you are betting ${bet} on {lines} lines.Total bet is equal to : ${total_bet}")
    
    

    slots= get_slot_machine_spin(ROWS,COLS,symbole_count)
    print_slot_machine(slots)
    winnings,winning_line =check_winning(slots,lines,bet,symbole_Value)
    
    
    print(f"you won ${winnings}")
    print(f"You Won on lines : ", * winning_line)  
    return winnings ,total_bet

def main():
    balance=deposit()
    print(f"current balnce is ${balance}")
    spin(balance)
    balance+=winnings
    print(f"you left with ${balance}")
main()

