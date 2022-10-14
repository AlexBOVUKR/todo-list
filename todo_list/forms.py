import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.forms import SelectDateWidget

from todo_list.models import Task, Tag


class TaskForm(forms.ModelForm):
    content = forms.CharField(
        label="Name(short content)"
    )
    deadline = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
        ),
        required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        fields = ["content", "deadline", "tags", "detail"]

    def clean_deadline(self):
        return validate_deadline(self.cleaned_data["deadline"])


def validate_deadline(deadline):
    today = datetime.datetime.now()
    if deadline:
        if deadline < today:
            raise ValidationError("You try to set date in the past")
        return deadline
    return deadline
