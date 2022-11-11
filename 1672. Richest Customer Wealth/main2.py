def main(accounts):
    richest = 0
    for account in accounts:
        if sum(account)>richest:
            richest = sum(account)
    return richest


accounts = [[1,5],[7,3],[3,5]]

print(main(accounts))