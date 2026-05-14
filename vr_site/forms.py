from django import forms
from .models import VRReview


class VRReviewForm(forms.ModelForm):
    class Meta:
        model = VRReview
        fields = ["headset_model", "rating", "comment"]
        widgets = {
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
            "comment": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_rating(self):
        rating = self.cleaned_data["rating"]
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Оценка должна быть от 1 до 5!")
        return rating
