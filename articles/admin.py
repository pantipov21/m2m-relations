from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scopeship, Scope


class ScopeshipInlineFormset(BaseInlineFormSet):
	def clean(self):
		counter_topics = 0
		for form in self.forms:
			if form.cleaned_data and form.cleaned_data['is_main']:
				counter_topics = counter_topics + 1
		
		if counter_topics == 0:
			raise ValidationError('Необходимо выбрать основной раздел статьи')
		if counter_topics > 1:
			raise ValidationError('Только один раздел может быть основным')
		
		return super().clean()
		

class ScopeshipInline(admin.TabularInline):
	model = Scopeship
	formset = ScopeshipInlineFormset
	

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeshipInline]

    
@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
	ordering = ['name']
