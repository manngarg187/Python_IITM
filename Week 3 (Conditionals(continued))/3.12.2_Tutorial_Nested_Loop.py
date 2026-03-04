empID = input('Enter employee ID: ')
while(empID != '-1'):
  trade = int(input('Enter the trade amount: '))
  profit_loss = 0
  while(trade != 0):
    profit_loss = profit_loss + trade
    trade = int(input('Enter the trade amount: '))
  print(f'Profit/loss for employee {empID} is {profit_loss}')
  empID = input('\nEnter employee ID: ')