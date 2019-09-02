from django.urls import path

from posts.views import PostPageView

urlpatterns = [
  path('', PostPageView.as_view(), name='posts')
]