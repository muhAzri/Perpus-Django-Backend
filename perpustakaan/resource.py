from import_export import resources
from perpustakaan.models import Book
from import_export.fields import Field

class BookResource(resources.ModelResource):
    group_id__name = Field(attribute='group_id', column_name='Kelompok')

    class Meta:
        model = Book
        fields = ['title','date','group_id__name', 'writter', 'amount']
        export_order = ['title', 'writter', 'group_id__name', 'date', 'amount']