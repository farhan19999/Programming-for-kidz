from django.http import HttpResponse
from django.template import loader
from .models import ReadingMaterial
from django.db.models import Subquery, OuterRef


def members(request):
    distinct_section_ids = (ReadingMaterial.objects.order_by('sectionId').values('sectionId').distinct())
    first_reading_materials = (ReadingMaterial.objects.filter(sectionId=OuterRef('sectionId'))
                                   .order_by('id').values('id')[:1])
    # Annotate the first ReadingMaterial for each distinct sectionId
    distinct_reading_materials = (
        ReadingMaterial.objects
            .filter(id=Subquery(first_reading_materials))
            .order_by('sectionId')
    )
    print(distinct_reading_materials)
    template = loader.get_template('allReadingMaterials.html')
    context = {
        'allcontents': distinct_reading_materials,
    }
    return HttpResponse(template.render(context, request))


def details(request, ID):
    topic = ReadingMaterial.objects.get(id=ID)
    nextTopic = ReadingMaterial.objects.get(id=ID + 1)
    template = loader.get_template('details.html')
    context = {
        'topic': topic,
        'nextTopic': nextTopic
    }
    return HttpResponse(template.render(context, request))
