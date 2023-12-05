from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    LOAN_TYPES = {'StudentLoan': StudentLoan, 'MortgageLoan': MortgageLoan}
    CLIENT_TYPES = {'Student': Student, 'Adult': Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOAN_TYPES:
            raise Exception("Invalid loan type!")

        new_loan = self.LOAN_TYPES[loan_type]
        self.loans.append(new_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:

            return "Not enough bank capacity."

        new_client = self.CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(new_client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.find_client_by_id(client_id)
        loan = self.find_loans_by_type(loan_type)[0]
        if not client.LOAN_TYPE == loan_type:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)

        return f'Successfully granted {loan_type} to {client.name} with ID {client_id}.'

    def remove_client(self, client_id: str):
        client = self.find_client_by_id(client_id)
        if client is None:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        filtered_loans = self.find_loans_by_type(loan_type)
        [loan.increase_interest_rate() for loan in filtered_loans]
        return f"Successfully changed {len(filtered_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        clients = [client for client in self.clients if client.interest < min_rate]
        [c.increase_clients_interest() for c in clients]
        return f"Number of clients affected: {len(clients)}."

    def get_statistics(self):
        income = sum([c.income for c in self.clients])
        granted_loans_count = sum([len(client.loans) for client in self.clients])
        granted_amount = sum([sum([loan.amount for loan in client.loans]) for client in self.clients])
        not_granted_sum = sum([loan.amount for loan in self.loans])
        avg_client_rate = sum([client.interest for client in self.clients]) / len(self.clients) if self.clients else 0

        return (f"Active Clients: {len(self.clients)}\n"
                f"Total Income: {income:.2f}\n"
                f"Granted Loans: {granted_loans_count}, Total Sum: {granted_amount:.2f}\n"
                f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum}\n"
                f"Average Client Interest Rate: {avg_client_rate:.2f}")

    # additional methods
    def find_client_by_id(self, client_id):
        client = [c for c in self.clients if client_id == c.client_id]
        if client:
            return client[0]
        return None

    def find_loans_by_type(self, loan_type):
        return [loan for loan in self.loans if loan.LOAN_TYPE == loan_type]
