lend2 amount balance = if amount < reserve * 0.5
                       then Just newBalance
                       else Nothing 
                       where reserve = 100
                             newBalance = balance - amount