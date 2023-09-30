from creditagricole_particuliers import Authenticator, Accounts
from dotenv import load_dotenv, dotenv_values

config = dotenv_values()

username = config.get("USER_ID")
password = [int(x) for x in config.get("USER_PIN")]
department = config.get("DEPARTMENT")

session = Authenticator(username=username, password=password, department=department)

# search account
account = Accounts(session=session).search(num=config.get("ACCOUNT_ID"))

# get operations
operations = account.get_operations(count=30)
for op in operations:
    print(op)
