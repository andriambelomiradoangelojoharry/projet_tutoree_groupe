from django import forms
from .models import Adherent, CompteAdherent

class FormulaireAjoutAdherent(forms.ModelForm):
    class Meta:
        model = Adherent
        fields = '__all__'
        widgets = {
            'matricule' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'nom' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'prenom' : forms.TextInput(attrs={
                'class' : 'form-control'
            }),
            'email' : forms.EmailInput(attrs={
                'class' : 'form-control'
            }),
            'fonctions' : forms.Select(attrs={
                'class' : 'form-control'
            })
        }


class FormulaireInscription(forms.Form):
    matricule = forms.CharField(label='Matricule', 
                                widget=forms.TextInput(attrs={
                                    'class' : 'form-control'
                                }))
    username = forms.CharField(label='Nom d\'utilisateur', 
                               widget=forms.TextInput(attrs={
                                   'class' : 'form-control'
                               }))
    code_otp = forms.CharField(label="Code OTP", 
                               widget=forms.TextInput(attrs={
                                   'class' : 'form-control'
                               }))
    password = forms.CharField(label='Mots de passe',
                               widget=forms.PasswordInput(attrs={
                                   'class' : 'form-control'
                               }))
    password2 = forms.CharField(label='Confirmer mots de passe',
                                widget=forms.PasswordInput(attrs={
                                    'class' : 'form-control'
                                }))
                                
   


    def clean(self):
        cleaned_data = super().clean()
        matricule = cleaned_data.get('matricule')
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        code_otp = cleaned_data.get('code_otp')

        if not Adherent.objects.filter(matricule=matricule).exists():
            raise forms.ValidationError("Votre matricule n'est pas réconnu. Contactez l'administration.")
        
        if CompteAdherent.objects.filter(personne__matricule=matricule).exists():
            raise forms.ValidationError(
                "Un compte existe dejà pour ce matricule"
            )
        
        if password != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas")
        
        return cleaned_data
    
class VerificationParEmail(forms.Form):
    email = forms.EmailField(label="Entrez votre adresse email",
                             widget=forms.EmailInput(attrs={
                                 'class' : 'form-control'
                             }))
    

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        return cleaned_data