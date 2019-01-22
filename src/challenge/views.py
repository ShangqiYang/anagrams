from django.shortcuts import render
from django.http import HttpResponse

from .models import Dictionary
from .core import Trie, TrieNode
from .forms import DictionaryForm

# Create your views here.
def application_view(request, *args, **kwargs):

	if request.method == 'POST':
		form = DictionaryForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
			return HttpResponse('success')
		else:
			return HttpResponse('failed')
	else:
		form = DictionaryForm()

	dictionaries = Dictionary.objects.all() # list of objects;
	
	content = {
		'form'			: form,
		'object_list'	: dictionaries,
	}

	return render(request, 'application.html', content)

def check_view(request, *args, **kwargs):

	if request.method == 'POST':
		d_id = request.POST.get('d_id')
		word = request.POST.get('word')

		dictionary = Dictionary.objects.get(id=d_id)
		trie = Trie(dictionary.file.path)

		content = {
			"word"				: word,
			"anagrams_group"	: trie.check(word)
		}
		return render(request, "result.html", content)

