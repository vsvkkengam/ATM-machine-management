# ATM-machine-management
The code simulates a basic banking system where users can check their balance, deposit cash, withdraw cash, and exit the system after completing their transactions. It ensures user authentication, handles user inputs, and updates the available balance accordingly.

**The will work as follows**

1. **User Authentication**:
   - The code prompts the user to input their user ID and password.
   - It then compares these inputs with predefined values (`user_id` and `password`) to authenticate the user.

2. **Menu Display**:
   - If the user is authenticated successfully, the code displays a menu with four options:
     - Check Balance
     - Cash Deposit
     - Cash Withdrawal
     - Exit

3. **Option Selection**:
   - The user is prompted to select an option from the menu.
   - Based on the user's choice, the code executes different actions.

4. **Check Balance**:
   - If the user chooses to check the balance (`option == 1`), the code prints the available balance.

5. **Cash Deposit**:
   - If the user chooses to deposit cash (`option == 2`), the code prompts the user to enter the amount they want to deposit.
   - The deposited amount is added to the available balance, and the new balance is displayed.

6. **Cash Withdrawal**:
   - If the user chooses to withdraw cash (`option == 3`), the code prompts the user to enter the amount they want to withdraw.
   - If the withdrawal amount is less than or equal to the available balance, the amount is subtracted from the balance, and the new balance is displayed. Otherwise, it notifies the user of insufficient funds.

7. **Exit**:
   - If the user chooses to exit (`option == 4`), the code displays a farewell message and terminates.

8. **Error Handling**:
   - If the user enters an invalid option or provides incorrect credentials, appropriate error messages are displayed.

9. **Modularity**:
   - The code is divided into functions to improve readability and maintainability. Each function handles a specific task, such as authentication, menu display, balance checking, depositing cash, and withdrawing cash.

10. **Readability**:
    - Variable names and comments are used effectively to make the code easy to understand.

