from django import forms

class ApprovalForm(forms.Form):
    LP_CustomerPrincipalPayments = forms.IntegerField()
    LoanMonthsSinceOrigination = forms.IntegerField()
    LP_CustomerPayments = forms.IntegerField()
    EmploymentStatus_Full_time = forms.ChoiceField(choices = [(0, "Not Full Time"), (1, "Full Time")])
    Investors = forms.IntegerField()
    MonthlyLoanPayment = forms.IntegerField()
    LoanOriginalAmount = forms.IntegerField()