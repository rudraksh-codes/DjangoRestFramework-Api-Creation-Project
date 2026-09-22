from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 1
    page_size_query_param = 'page-size'
    page_query_param = 'page-num'

    def get_paginated_response(self, data):
        return Response({
            'count' : self.page.paginator.count, 
            'next' : self.get_next_link(), 
            'previous' : self.get_previous_link(),
            'page_size' : self.page_size, 
            'result' : data #serialized data

        }) 

class CustomLimitOffsetPagination(LimitOffsetPagination):

    default_limit = 2
    max_limit = 5
    limit_query_param = 'page-limit'
    offset_query_param  = 'page-offset'

    def get_paginated_response(self, data):
        return Response(
            {
                'links' : {
                    'next' : self.get_next_link(), 
                    'previous' : self.get_previous_link()
                },
                'count' : self.count, 
                'results' : data, 
            
            }
        )

    