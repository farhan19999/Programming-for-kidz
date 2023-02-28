from django.http import HttpResponse
from django.template import loader
from .models import ReadingMaterial, Course, Mcq
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


def mcq(request,c_id,q_id):
    que_obj = Mcq.objects.get(pk=q_id)
    _course = que_obj.course
    
    next=-1
    for i in (q_id+1,len(Mcq.objects.all())+1):
        if Mcq.objects.filter(pk=i,course=_course).exists():
            next = i
            break
    if next>0 :
        nexturl ="/mcq/"+str(c_id)+"/"+str(next) 
    else :
        nexturl = '../../allreadingmaterials/' 
    template = loader.get_template('mcq.html')
    context = {
        'que_obj' : que_obj,
        'next'     : nexturl,
    }
    return HttpResponse(template.render(context, request))



