from django import forms
from django.core.validators import RegexValidator

class Contact(forms.Form):
	choices=['Servicio Técnico', 
			'Cotización', 
			'Solicitud de Información']
	for i in range(0,len(choices)):
		choices[i]=(choices[i],choices[i])
	asunto=forms.ChoiceField(label='Asunto*',choices=choices,widget=forms.Select(attrs=
                                {'class':'btn btn-primary dropdown-header',
                                'style':'background-color:#090C7B;color:#FF8000;font-weight: bold'}))
	nombre=forms.CharField(label='Nombre*',widget=forms.TextInput(attrs=
            {'class':'form-control',
            'placeholder':'Nombres y Apellidos',
            'style':'width:50%'}))

	empresa=forms.CharField(label='Empresa',required=False,
			widget=forms.TextInput(attrs=
            {'class':'form-control',
            'placeholder':'Empresa',
            'style':'width:50%'}))

	ciudad=forms.CharField(label='Ciudad*',widget=forms.TextInput(attrs=
            {'class':'form-control',
            'placeholder':'Ciudad',
            'style':'width:50%'}))

	email= forms.EmailField(label='Correo electrónico*',max_length=40,
            error_messages={'invalid': 'Ingrese una direción de Correo válida'},
            widget=forms.TextInput(attrs=
            {'class':'form-control',
            'placeholder':'E-mail',
            'style':'width:50%'}))

	mensaje=forms.CharField(label='Mensaje*',widget=forms.Textarea(attrs=
                                {'class':'form-control',
                                'placeholder':'Deje su mensaje',
                                'style':'width:50%', 'rows':'5'}))

