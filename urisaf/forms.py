from django import forms

class UriSAFForm(forms.Form):
    leukocytes = forms.IntegerField(
        label='Leukocytes', 
        widget=forms.NumberInput(
            attrs={'min': 0, 'placeholder': 'Enter Leukocytes values'})
    )
    nitrites = forms.IntegerField(
        label='Nitrites',
        widget=forms.NumberInput(
            attrs={'min': 0, 'placeholder': 'Enter Nitrites values'})
    )
    uribilinogen = forms.IntegerField(
        label='Uribilinogen',
        widget=forms.NumberInput(
            attrs={'min': 0, 'placeholder': 'Enter Uribilinogen values'})
    )
    protein = forms.IntegerField(
        label='Protein',
        widget=forms.NumberInput(
            attrs={'min': 0, 'placeholder': 'Enter Protein values'})
    )
    pH = forms.IntegerField(
        label='pH',
        widget=forms.NumberInput(
            attrs={'min': 0, 'placeholder': 'Enter pH values'})
    )
    blood = forms.IntegerField(
        label='Blood',
        widget=forms.NumberInput(
            attrs={'min': 0, 'placeholder': 'Enter Blood values'})
    )
    specific_gravity = forms.IntegerField(
        label='Specific Gravity',
        widget=forms.NumberInput(
            attrs={'min': 0, 'placeholder': 'Enter Specific Gravity values'})
    )
    ketones = forms.IntegerField(
        label='Ketones',
        widget=forms.NumberInput(
            attrs={'min': 0, 'placeholder': 'Enter Ketones values'})
    )
    bilirubin = forms.IntegerField(
        label='Bilirubin',
        widget=forms.NumberInput(
            attrs={'min': 0, 'placeholder': 'Enter Bilirubin values'})
    )
    glucose = forms.IntegerField(
        label='Glucose',
        widget=forms.NumberInput(
            attrs={'min': 0, 'placeholder': 'Enter Glucose values'})
    )
