from django.shortcuts import render

from articles.models import Article, Scopeship, Scope


def articles_list(request):
	template = 'articles/news.html'

	# используйте этот параметр для упорядочивания результатов
	# https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
	ordering = '-published_at'

	context = {}
	
	articles = Article.objects.order_by(ordering)
	
	for article in articles:  
		print(article)
		for t in article.scopes.all():
			print(t.tag.name)
			print(t.is_main)

	context['object_list'] = articles
	
	return render(request, template, context)
