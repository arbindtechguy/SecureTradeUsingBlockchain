import django_tables2 as tables



class CustomTable(tables.Table):

    class Meta:
        template_name = 'django_tables2/semantic.html'