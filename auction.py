import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

auctions = []
print('Welcome to the secret auction program. ')
print(logo)
condi = True
while condi == True:
    name = input('What is your name?: ')
    bid = int(input('What\'s your bid?:'))
    ditc = {
        'name': name,
        'bid': bid
    }
    auctions.append(ditc)
    newbid = input('Are there any other bidders? Type \'yes\' or \'no\'.\n')
    clear = lambda: os.system('clear')
    clear()
    if newbid == 'no':
        condi = False
    else:
        continue

num = 0
i = 0
for index, auction in enumerate(auctions):
    if auction['bid'] > num:
        num = auction['bid']
        i = index

print(f"The winner is {auctions[i]['name']} with a bid of {auctions[i]['bid']}")
