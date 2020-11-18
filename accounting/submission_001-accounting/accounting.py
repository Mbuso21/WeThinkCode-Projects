from user import authentication
from transactions import journal
#from banking import reconciliation
from banking.fvb import reconciliation 
# from banking.ubsa import reconciliation as recon_ubsa
import sys
# from banking.online import reconciliation as recon_online


def print_argv():

    #if len(sys.argv) > 1:
    for out in sys.argv[1:]:
        print(out)

if __name__ == "__main__":

    print_argv()

    authentication.authenticate_user()
    
    journal.receive_income(100.00)
    journal.pay_expense(100.00)

    reconciliation.do_reconciliation()
    # recon_ubsa.do_reconciliation()
    # recon_online.do_reconciliation()

    #help('modules')

