
from django.views.generic import TemplateView
from django.contrib import messages
from django.http import HttpResponseRedirect
from .filters import TestFilter
from django.urls import reverse_lazy

class TestView(TemplateView):
  template_name = "test/test.html"
  filterset_class = TestFilter
  
  def get_context_data(self, **kwargs):
    ctx = super(TestView, self).get_context_data(**kwargs)
    # messages.info(self.request, "initial message from messages")
    # print ('123')
    return ctx
  
  
def SomeFunctionView(request):
  messages.error(request, 'New error from messages')
  return HttpResponseRedirect(reverse_lazy('test-list-view'))

  # print('referer', request.META['HTTP_REFERER'])
  # print('query', request.META['QUERY_STRING'])
  # print('query', bool(request.META['QUERY_STRING']))
  # print('full path', request.get_full_path())
  # print('absolute url', request.build_absolute_uri())
  # print('messages', request._messages)
  # return HttpResponseRedirect(reverse_lazy('companyusers-list') + '?' + request.META['QUERY_STRING'])