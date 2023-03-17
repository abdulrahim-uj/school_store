from django import forms
from django.forms import TextInput, DateInput, NumberInput, ChoiceField, EmailInput, Textarea, \
    CheckboxSelectMultiple, RadioSelect, ModelChoiceField, Select

from .models import Suggestion, MaterialsChoices, Department, Course
from django.utils.translation import gettext_lazy as _


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        exclude = ['creator', 'updater', 'auto_id', 'is_deleted']
        fields = ['name', 'dob', 'age', 'gender', 'phone', 'email', 'address', 'department', 'course', 'purpose',
                  'materials']

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'dob': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'age': NumberInput(attrs={'class': 'form-control'}),
            'gender': RadioSelect(choices=Suggestion.GENDER_CHOICE),
            'phone': TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'email': EmailInput(attrs={'class': 'form-control', 'required': 'required'}),
            'address': Textarea(attrs={'class': 'form-control', 'cols': '10', 'rows': '5', 'required': 'required', },),
            'department': Select(choices=Department.objects.filter(is_deleted=False), attrs={'class': 'form-select'}),
            'course': Select(choices=Course.objects.all(), attrs={'class': 'form-select'}),
            'purpose': Select(choices=Suggestion.PURPOSES_CHOICE, attrs={'class': 'form-select'}),
            'materials': CheckboxSelectMultiple(choices=MaterialsChoices.objects.all(),
                                                attrs={'class': 'form-check-input'})
        }
        labels = {
            'name': "Name",
            'dob': "Date or Birth",
        }
        error_messages = {
            'name': {
                'required': _('This field is required'),
            },
            'dob': {
                'required': _('This field is required'),
            },
        }

        # Advanced way to set readonly property
    def __init__(self, *args, **kwargs):
        super(SuggestionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            # if field in ['continent', 'country_code', 'country', 'state_code', 'state', 'city',
            #              'district', 'location_type', 'village', 'county', 'pin_code', 'formatted',
            #              'road_info', 'neighbourhood', 'latitude', 'longitude']:
            #     self.fields[field].widget.attrs['readonly'] = 'readonly'

            self.fields['course'].queryset = Course.objects.none()
            if 'course' in self.data:  # checking if we have state in the posted data
                try:
                    department_pk = self.data.get('department')  # get the state ID
                    self.fields['course'].queryset = Course.objects.filter(department__id=department_pk).order_by('course_name')
                    # the above is setting the queryset for the town field by filtering
                    # the Town using the posted state_id.
                except (ValueError, TypeError):
                    pass

            if field == 'age':
                self.fields[field].widget.attrs['readonly'] = 'readonly'
