def calculations_after_certain_period_fn(p, r, years, m_pay):
    interest_paid_after_certain_years = (((p * (r / 100/ 12) - m_pay) * (((1 + (r/ 100/ 12)) ** (years * 12)) - 1)) / (r/ 100/ 12)) + (m_pay * years * 12)
    total_pay_after_certain_years = m_pay * 12 * years
    total_principal_paid_after_certain_years = total_pay_after_certain_years - interest_paid_after_certain_years
    remaining_balance = 250000 - total_principal_paid_after_certain_years
    return {
    "years": years,
    "interest_paid": interest_paid_after_certain_years,
    "total_paid": total_pay_after_certain_years,
    "total_principal_paid": total_principal_paid_after_certain_years,
    "remaining_balance": remaining_balance
    }


print("Welcome to easy mortgage payment solution!!!^_^")
res = input("We have built a simple software for laymen to calculate their mortgage plans with ease.Do you want to try?(yes/no):")
m_pay = 0
if res == 'yes':
    print("Enter your principal:")
    p_input = input()
    p = float(p_input)
    print("Enter your interest rate:")
    r_input = input()
    r = float(r_input)
    print("Enter your time duration in years:")
    y_input = input()
    y = float(y_input)
    print("Enter certain period in years to get estimated calculations: ")
    years_input = input()
    years = float(years_input)
    print(p, r, y)
    m_pay = ((r / 100/ 12) * p) / (1 - ((1 + (r / 100/ 12)) ** (-y * 12)))
    total_pay = m_pay * y * 12
    total_int_pay = total_pay - p
    calculations_after_certain_period = calculations_after_certain_period_fn(p, r, years, m_pay)
else:
    print("Okay!We look forward to have you again...")
    
print(f"Monthly Payment: {m_pay},\n Total Payment: {total_pay},\nTotal Interest Paid: {total_int_pay},\ncalculations_after_certain_period: {calculations_after_certain_period} ")